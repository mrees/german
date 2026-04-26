/**
 * SpeakGerman — Shared Engine
 * Handles: progress tracking, speech synthesis, speech recognition,
 *          exercise scoring, conversation practice
 */

// ── PROGRESS STORAGE ──────────────────────────────────────────────────────────
const SG = {
  version: '1.0',

  /** Load full progress object from localStorage */
  loadProgress() {
    try {
      return JSON.parse(localStorage.getItem('sg_progress') || '{}');
    } catch { return {}; }
  },

  /** Save full progress object */
  saveProgress(p) {
    localStorage.setItem('sg_progress', JSON.stringify(p));
  },

  /** Get data for one lesson (creates default if missing) */
  getLesson(num) {
    const p = this.loadProgress();
    if (!p[num]) p[num] = { completed: false, score: 0, attempts: 0, lastDate: null };
    return p[num];
  },

  /** Mark lesson as complete with score */
  completeLesson(num, score) {
    const p = this.loadProgress();
    if (!p[num]) p[num] = {};
    p[num].completed = true;
    p[num].score = Math.max(p[num].score || 0, score);
    p[num].attempts = (p[num].attempts || 0) + 1;
    p[num].lastDate = new Date().toISOString().slice(0, 10);
    this.saveProgress(p);
    this.updateXPDisplay();
  },

  /** Total XP earned */
  totalXP() {
    const p = this.loadProgress();
    return Object.values(p).reduce((sum, l) => sum + (l.score || 0), 0);
  },

  /** Count completed lessons */
  completedCount() {
    const p = this.loadProgress();
    return Object.values(p).filter(l => l.completed).length;
  },

  /** Suggest lessons to repeat (score < 80 or not done) */
  suggestRepeat() {
    const p = this.loadProgress();
    const suggestions = [];
    for (let i = 1; i <= 30; i++) {
      const l = p[i];
      if (!l || !l.completed) { suggestions.push(i); continue; }
      if (l.score < 80) suggestions.push(i);
    }
    return suggestions.slice(0, 5);
  },

  /** Update XP chip in nav */
  updateXPDisplay() {
    const el = document.getElementById('sg-xp');
    if (el) el.textContent = '⭐ ' + this.totalXP() + ' XP';
  }
};

// ── SPEECH SYNTHESIS ──────────────────────────────────────────────────────────
function sgSpeak(text, lang = 'de-DE', rate = 0.85) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = lang;
  u.rate = rate;
  u.pitch = 1;
  // Prefer a German voice if available
  const voices = window.speechSynthesis.getVoices();
  const german = voices.find(v => v.lang.startsWith('de'));
  if (german) u.voice = german;
  window.speechSynthesis.speak(u);
}

// Ensure voices are loaded (async on some browsers)
if (window.speechSynthesis) {
  window.speechSynthesis.getVoices();
  window.speechSynthesis.onvoiceschanged = () => window.speechSynthesis.getVoices();
}

// ── SPEECH RECOGNITION ───────────────────────────────────────────────────────
function sgListen(onResult, onError) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) {
    if (onError) onError('Speech recognition is not supported in this browser. Please use Chrome or Edge.');
    return null;
  }
  const rec = new SR();
  rec.lang = 'de-DE';
  rec.interimResults = false;
  rec.maxAlternatives = 3;
  rec.onresult = e => {
    const results = Array.from(e.results[0]).map(r => r.transcript.toLowerCase().trim());
    onResult(results);
  };
  rec.onerror = e => { if (onError) onError(e.error); };
  rec.start();
  return rec;
}

/** Compare spoken result to expected text (fuzzy) */
function sgCheckPronunciation(heard, expected) {
  const norm = s => s.toLowerCase().replace(/[.,!?]/g, '').trim();
  const e = norm(expected);
  if (heard.some(h => norm(h) === e)) return { pass: true, score: 100 };
  // partial match
  const words = e.split(' ');
  const best = heard.reduce((best, h) => {
    const hw = norm(h).split(' ');
    const matches = words.filter(w => hw.includes(w)).length;
    return Math.max(best, Math.round(matches / words.length * 100));
  }, 0);
  return { pass: best >= 60, score: best };
}

// ── EXERCISE ENGINE ───────────────────────────────────────────────────────────
/**
 * Render a multiple-choice exercise.
 * cfg = { question, choices: [{text, correct}], onDone(correct) }
 */
function sgMultiChoice(container, cfg) {
  const fb = container.querySelector('.sg-feedback');
  const choices = container.querySelectorAll('.sg-choice');
  choices.forEach(btn => {
    btn.onclick = () => {
      choices.forEach(b => { b.disabled = true; });
      const isCorrect = btn.dataset.correct === 'true';
      btn.classList.add(isCorrect ? 'correct' : 'wrong');
      if (!isCorrect) {
        choices.forEach(b => { if (b.dataset.correct === 'true') b.classList.add('correct'); });
      }
      if (fb) {
        fb.className = 'sg-feedback show ' + (isCorrect ? 'correct' : 'wrong');
        fb.textContent = isCorrect ? '✅ Correct! Well done.' : '❌ Not quite. The correct answer is highlighted.';
      }
      if (cfg.onDone) cfg.onDone(isCorrect);
    };
  });
}

/**
 * Wire up a fill-in-the-blank input.
 * cfg = { answer (string or array), onDone(correct) }
 */
function sgFillBlank(input, btn, feedbackEl, cfg) {
  const check = () => {
    const val = input.value.toLowerCase().trim().replace(/[.,!?]/g, '');
    const answers = Array.isArray(cfg.answer)
      ? cfg.answer.map(a => a.toLowerCase().trim().replace(/[.,!?]/g, ''))
      : [cfg.answer.toLowerCase().trim().replace(/[.,!?]/g, '')];
    const correct = answers.includes(val);
    input.disabled = true;
    if (btn) btn.disabled = true;
    input.classList.add(correct ? 'correct' : 'wrong');
    if (feedbackEl) {
      feedbackEl.className = 'sg-feedback show ' + (correct ? 'correct' : 'wrong');
      feedbackEl.textContent = correct
        ? '✅ Correct!'
        : `❌ Correct answer: "${answers[0]}"`;
    }
    if (cfg.onDone) cfg.onDone(correct);
  };
  if (btn) btn.onclick = check;
  input.onkeydown = e => { if (e.key === 'Enter') check(); };
}

// ── LESSON CONTROLLER ─────────────────────────────────────────────────────────
/**
 * LessonController — attach to a lesson page.
 * Usage: new LessonController(lessonNum, totalExercises)
 */
class LessonController {
  constructor(lessonNum, totalExercises) {
    this.num = lessonNum;
    this.total = totalExercises;
    this.correct = 0;
    this.done = 0;
    this._updateBar();
    SG.updateXPDisplay();
  }

  record(isCorrect) {
    this.done++;
    if (isCorrect) this.correct++;
    this._updateBar();
    if (this.done >= this.total) {
      setTimeout(() => this._showComplete(), 600);
    }
  }

  _updateBar() {
    const bar = document.getElementById('sg-progress-fill');
    if (bar) bar.style.width = (this.total > 0 ? (this.done / this.total * 100) : 0) + '%';
  }

  _showComplete() {
    const score = Math.round(this.correct / this.total * 100);
    SG.completeLesson(this.num, score);
    const panel = document.getElementById('sg-complete');
    if (!panel) return;
    const stars = score >= 90 ? '⭐⭐⭐' : score >= 70 ? '⭐⭐' : '⭐';
    document.getElementById('sg-score-stars').textContent = stars;
    document.getElementById('sg-score-pct').textContent = score + '%';
    document.getElementById('sg-score-xp').textContent = score + ' XP earned';
    panel.style.display = 'block';
    panel.scrollIntoView({ behavior: 'smooth' });
  }
}

// ── CONVERSATION ENGINE ───────────────────────────────────────────────────────
class ConversationPractice {
  constructor(containerId, script) {
    this.container = document.getElementById(containerId);
    this.script = script; // [{role:'tutor'|'student', text, translation}]
    this.idx = 0;
    this.log = this.container.querySelector('.sg-convo-log');
    this.input = this.container.querySelector('.sg-convo-input input');
    this.sendBtn = this.container.querySelector('.sg-convo-input button');
    this.micBtn = this.container.querySelector('.sg-mic-convo');
    this._bind();
    this._next();
  }

  _bind() {
    if (this.sendBtn) this.sendBtn.onclick = () => this._submit();
    if (this.input) this.input.onkeydown = e => { if (e.key === 'Enter') this._submit(); };
    if (this.micBtn) this.micBtn.onclick = () => this._listen();
  }

  _next() {
    if (this.idx >= this.script.length) return;
    const line = this.script[this.idx];
    if (line.role === 'tutor') {
      this._addBubble('tutor', line.text + (line.translation ? `<br><small style="opacity:.65">${line.translation}</small>` : ''));
      setTimeout(() => sgSpeak(line.text), 400);
      this.idx++;
      // if next line is also tutor, continue
      if (this.idx < this.script.length && this.script[this.idx].role === 'tutor') {
        setTimeout(() => this._next(), 2200);
      }
    }
  }

  _submit() {
    const val = this.input?.value.trim();
    if (!val) return;
    this._addBubble('student', val);
    this.input.value = '';
    this.idx++;
    setTimeout(() => this._next(), 800);
  }

  _listen() {
    if (this.micBtn) this.micBtn.textContent = '🎙️ Listening…';
    sgListen(
      results => {
        if (this.micBtn) this.micBtn.textContent = '🎤 Speak';
        const spoken = results[0];
        this._addBubble('student', spoken);
        this.idx++;
        setTimeout(() => this._next(), 800);
      },
      err => {
        if (this.micBtn) this.micBtn.textContent = '🎤 Speak';
        this._addBubble('tutor', `(Mic error: ${err})`);
      }
    );
  }

  _addBubble(role, html) {
    const div = document.createElement('div');
    div.className = 'sg-bubble ' + role;
    div.innerHTML = html;
    this.log.appendChild(div);
    this.log.scrollTop = this.log.scrollHeight;
  }
}

// ── NAV HELPERS ───────────────────────────────────────────────────────────────
function sgNavLesson(num) {
  const prev = num > 1 ? `<a href="lesson${String(num-1).padStart(2,'0')}.html">← Lesson ${num-1}</a>` : '';
  const next = num < 30 ? `<a href="lesson${String(num+1).padStart(2,'0')}.html">Lesson ${num+1} →</a>` : '';
  const el = document.getElementById('sg-lesson-nav');
  if (el) el.innerHTML = prev + next;
}
