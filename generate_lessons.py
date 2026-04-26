#!/usr/bin/env python3
"""Generate all 30 SpeakGerman lesson HTML files."""
import os

OUT = "/sessions/focused-tender-meitner/mnt/German/lessons"
os.makedirs(OUT, exist_ok=True)

def pad(n):
    return str(n).zfill(2)

def lesson_shell(num, title, level, body_html):
    prev_link = '<a href="lesson%s.html">← Lesson %d</a>' % (pad(num-1), num-1) if num > 1 else ''
    next_link = '<a href="lesson%s.html">Lesson %d →</a>' % (pad(num+1), num+1) if num < 30 else ''
    if num < 30:
        next_btn = '<a href="lesson%s.html" class="sg-btn sg-btn-primary">Next Lesson →</a>' % pad(num+1)
    else:
        next_btn = '<a href="../index.html" class="sg-btn sg-btn-primary">🏆 All Done!</a>'

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SpeakGerman — Lesson %(num)d: %(title)s</title>
<link rel="stylesheet" href="../speakgerman.css">
</head>
<body>
<nav class="sg-nav">
  <span class="logo"><a href="../index.html" style="color:#fff;text-decoration:none">Speak<span style="color:#ffe14d">German</span></a></span>
  <span style="font-size:0.8rem;opacity:0.85">%(level)s</span>
  <span id="sg-xp" class="sg-xp">⭐ 0 XP</span>
</nav>

<div class="sg-wrap">
  <div class="sg-lesson-header">
    <div class="sg-lesson-num">Lesson %(num)d of 30</div>
    <div class="sg-lesson-title">%(title)s</div>
  </div>

  <div class="sg-progress-bar-outer">
    <div class="sg-progress-bar-inner" id="sg-progress-fill" style="width:0%%"></div>
  </div>

%(body)s

  <!-- Completion Panel -->
  <div class="sg-card" id="sg-complete" style="display:none">
    <div class="sg-score-panel">
      <div class="sg-score-title">Lesson Complete! 🎉</div>
      <div class="sg-score-stars" id="sg-score-stars">⭐⭐⭐</div>
      <div class="sg-score-text" id="sg-score-pct"></div>
      <div class="sg-score-text" id="sg-score-xp"></div>
      <div class="sg-btn-row" style="justify-content:center;margin-top:16px">
        <a href="../index.html" class="sg-btn sg-btn-secondary">🏠 Home</a>
        %(next_btn)s
      </div>
    </div>
  </div>

  <div style="display:flex;justify-content:space-between;margin-top:20px;font-size:0.9rem">
    %(prev_link)s
    <a href="../index.html">🏠 All Lessons</a>
    %(next_link)s
  </div>
</div>

<script src="../speakgerman.js"></script>
<script>
SG.updateXPDisplay();
</script>
</body>
</html>""" % {'num': num, 'title': title, 'level': level, 'body': body_html,
              'prev_link': prev_link, 'next_link': next_link, 'next_btn': next_btn}


# ─────────────────────────────────────────────────────────────────────────────
# LESSON DATA: each lesson has vocab, grammar note, exercises, speaking task
# ─────────────────────────────────────────────────────────────────────────────

lessons_data = {

1: ("Greetings & Farewells", "Level A1", """
  <div class="sg-card">
    <div class="sg-section-title">📚 Vocabulary</div>
    <table class="sg-vocab">
      <tr><th>German</th><th>Pronunciation</th><th>English</th><th></th></tr>
      <tr><td class="german">Hallo</td><td class="phonetic">HAH-lo</td><td>Hello</td><td><button class="sg-play-btn" onclick="sgSpeak('Hallo')">▶ Play</button></td></tr>
      <tr><td class="german">Guten Morgen</td><td class="phonetic">GOO-ten MOR-gen</td><td>Good morning</td><td><button class="sg-play-btn" onclick="sgSpeak('Guten Morgen')">▶ Play</button></td></tr>
      <tr><td class="german">Guten Tag</td><td class="phonetic">GOO-ten TAHK</td><td>Good day</td><td><button class="sg-play-btn" onclick="sgSpeak('Guten Tag')">▶ Play</button></td></tr>
      <tr><td class="german">Guten Abend</td><td class="phonetic">GOO-ten AH-bent</td><td>Good evening</td><td><button class="sg-play-btn" onclick="sgSpeak('Guten Abend')">▶ Play</button></td></tr>
      <tr><td class="german">Tschüss</td><td class="phonetic">CHÜSS</td><td>Bye</td><td><button class="sg-play-btn" onclick="sgSpeak('Tschüss')">▶ Play</button></td></tr>
      <tr><td class="german">Auf Wiedersehen</td><td class="phonetic">owf VEE-der-zayn</td><td>Goodbye (formal)</td><td><button class="sg-play-btn" onclick="sgSpeak('Auf Wiedersehen')">▶ Play</button></td></tr>
      <tr><td class="german">Wie geht es Ihnen?</td><td class="phonetic">vee GAYT es EE-nen</td><td>How are you? (formal)</td><td><button class="sg-play-btn" onclick="sgSpeak('Wie geht es Ihnen?')">▶ Play</button></td></tr>
      <tr><td class="german">Danke, gut</td><td class="phonetic">DAN-ke GOOT</td><td>Fine, thank you</td><td><button class="sg-play-btn" onclick="sgSpeak('Danke, gut')">▶ Play</button></td></tr>
      <tr><td class="german">Bitte</td><td class="phonetic">BIT-te</td><td>Please / You're welcome</td><td><button class="sg-play-btn" onclick="sgSpeak('Bitte')">▶ Play</button></td></tr>
      <tr><td class="german">Entschuldigung</td><td class="phonetic">ent-SHUL-di-gung</td><td>Excuse me / Sorry</td><td><button class="sg-play-btn" onclick="sgSpeak('Entschuldigung')">▶ Play</button></td></tr>
    </table>
  </div>

  <div class="sg-card">
    <div class="sg-grammar">
      <h4>📖 Grammar: Formal vs Informal</h4>
      <p>German has <strong>two</strong> ways to say "you":</p>
      <ul>
        <li><strong>du</strong> — informal, for friends, family, children</li>
        <li><strong>Sie</strong> (capital S) — formal, for strangers, bosses, older people</li>
      </ul>
      <p style="margin-top:8px">Example: <em>Wie geht es <strong>dir</strong>?</em> (informal) vs <em>Wie geht es <strong>Ihnen</strong>?</em> (formal)</p>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 1 — Choose the correct answer</div>
    <div class="sg-exercise" id="ex1">
      <div class="sg-question">How do you say "Good morning" in German?</div>
      <div class="sg-choices">
        <button class="sg-choice" data-correct="false">Guten Abend</button>
        <button class="sg-choice" data-correct="true">Guten Morgen</button>
        <button class="sg-choice" data-correct="false">Tschüss</button>
        <button class="sg-choice" data-correct="false">Auf Wiedersehen</button>
      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 2 — Fill in the blank</div>
    <div class="sg-exercise">
      <div class="sg-question">Complete: "_______, gut!" (Fine, thank you)</div>
      <input class="sg-fill" id="fill2" placeholder="Type the missing word…" autocomplete="off">
      <div class="sg-btn-row"><button class="sg-btn sg-btn-primary" id="fill2-btn">Check ✓</button></div>
      <div class="sg-feedback" id="fill2-fb"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 3 — Translate</div>
    <div class="sg-exercise">
      <div class="sg-question">How do you say "Excuse me" in German?</div>
      <input class="sg-fill" id="fill3" placeholder="Type in German…" autocomplete="off">
      <div class="sg-btn-row"><button class="sg-btn sg-btn-primary" id="fill3-btn">Check ✓</button></div>
      <div class="sg-feedback" id="fill3-fb"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">🎤 Speaking Practice — Say it aloud!</div>
    <div class="sg-speak-card">
      <div class="sg-speak-phrase">Guten Morgen!</div>
      <div class="sg-speak-translation">Good morning!</div>
      <button class="sg-btn sg-btn-audio" style="margin-bottom:10px" onclick="sgSpeak('Guten Morgen')">🔊 Hear it</button><br>
      <button class="sg-mic-btn" id="mic1" onclick="startMic('Guten Morgen','mic1','mic1-result')">🎤 Speak Now</button>
      <div class="sg-mic-result" id="mic1-result"></div>
    </div>
    <div class="sg-speak-card" style="margin-top:14px">
      <div class="sg-speak-phrase">Wie geht es Ihnen?</div>
      <div class="sg-speak-translation">How are you? (formal)</div>
      <button class="sg-btn sg-btn-audio" style="margin-bottom:10px" onclick="sgSpeak('Wie geht es Ihnen?')">🔊 Hear it</button><br>
      <button class="sg-mic-btn" id="mic2" onclick="startMic('Wie geht es Ihnen','mic2','mic2-result')">🎤 Speak Now</button>
      <div class="sg-mic-result" id="mic2-result"></div>
    </div>
  </div>

  <script>
  const lc = new LessonController(1, 3);
  sgMultiChoice(document.getElementById('ex1'), { onDone: ok => lc.record(ok) });
  sgFillBlank(document.getElementById('fill2'), document.getElementById('fill2-btn'), document.getElementById('fill2-fb'),
    { answer: 'danke', onDone: ok => lc.record(ok) });
  sgFillBlank(document.getElementById('fill3'), document.getElementById('fill3-btn'), document.getElementById('fill3-fb'),
    { answer: 'entschuldigung', onDone: ok => lc.record(ok) });

  function startMic(phrase, btnId, resultId) {
    const btn = document.getElementById(btnId);
    const res = document.getElementById(resultId);
    btn.classList.add('listening');
    btn.textContent = '🎙️ Listening…';
    sgListen(
      results => {
        btn.classList.remove('listening'); btn.textContent = '🎤 Speak Now';
        const check = sgCheckPronunciation(results, phrase);
        res.innerHTML = check.pass
          ? '✅ Great pronunciation! (' + check.score + '% match)'
          : '❌ You said: "' + results[0] + '" — try again! (' + check.score + '% match)';
      },
      err => { btn.classList.remove('listening'); btn.textContent = '🎤 Speak Now'; res.textContent = '⚠️ ' + err; }
    );
  }
  </script>
"""),

2: ("Numbers 1–20", "Level A1", """
  <div class="sg-card">
    <div class="sg-section-title">📚 Numbers</div>
    <table class="sg-vocab">
      <tr><th>Number</th><th>German</th><th>Pronunciation</th><th></th></tr>
      <tr><td>1</td><td class="german">eins</td><td class="phonetic">ayns</td><td><button class="sg-play-btn" onclick="sgSpeak('eins')">▶</button></td></tr>
      <tr><td>2</td><td class="german">zwei</td><td class="phonetic">tsvay</td><td><button class="sg-play-btn" onclick="sgSpeak('zwei')">▶</button></td></tr>
      <tr><td>3</td><td class="german">drei</td><td class="phonetic">dry</td><td><button class="sg-play-btn" onclick="sgSpeak('drei')">▶</button></td></tr>
      <tr><td>4</td><td class="german">vier</td><td class="phonetic">feer</td><td><button class="sg-play-btn" onclick="sgSpeak('vier')">▶</button></td></tr>
      <tr><td>5</td><td class="german">fünf</td><td class="phonetic">fünf</td><td><button class="sg-play-btn" onclick="sgSpeak('fünf')">▶</button></td></tr>
      <tr><td>6</td><td class="german">sechs</td><td class="phonetic">zeks</td><td><button class="sg-play-btn" onclick="sgSpeak('sechs')">▶</button></td></tr>
      <tr><td>7</td><td class="german">sieben</td><td class="phonetic">ZEE-ben</td><td><button class="sg-play-btn" onclick="sgSpeak('sieben')">▶</button></td></tr>
      <tr><td>8</td><td class="german">acht</td><td class="phonetic">aht</td><td><button class="sg-play-btn" onclick="sgSpeak('acht')">▶</button></td></tr>
      <tr><td>9</td><td class="german">neun</td><td class="phonetic">noyn</td><td><button class="sg-play-btn" onclick="sgSpeak('neun')">▶</button></td></tr>
      <tr><td>10</td><td class="german">zehn</td><td class="phonetic">tsayn</td><td><button class="sg-play-btn" onclick="sgSpeak('zehn')">▶</button></td></tr>
      <tr><td>11</td><td class="german">elf</td><td class="phonetic">elf</td><td><button class="sg-play-btn" onclick="sgSpeak('elf')">▶</button></td></tr>
      <tr><td>12</td><td class="german">zwölf</td><td class="phonetic">tsvölf</td><td><button class="sg-play-btn" onclick="sgSpeak('zwölf')">▶</button></td></tr>
      <tr><td>13</td><td class="german">dreizehn</td><td class="phonetic">DRY-tsayn</td><td><button class="sg-play-btn" onclick="sgSpeak('dreizehn')">▶</button></td></tr>
      <tr><td>15</td><td class="german">fünfzehn</td><td class="phonetic">FÜNF-tsayn</td><td><button class="sg-play-btn" onclick="sgSpeak('fünfzehn')">▶</button></td></tr>
      <tr><td>20</td><td class="german">zwanzig</td><td class="phonetic">TSVAN-tsig</td><td><button class="sg-play-btn" onclick="sgSpeak('zwanzig')">▶</button></td></tr>
    </table>
    <div style="margin-top:12px">
      <button class="sg-btn sg-btn-audio" onclick="countUp()">🔊 Count 1→10</button>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-grammar">
      <h4>📖 Grammar: Numbers Pattern</h4>
      <ul>
        <li>13–19: add <strong>-zehn</strong> (like English -teen): dreizehn, vierzehn, fünfzehn…</li>
        <li>20 = zwanzig, 30 = dreißig, 40 = vierzig</li>
        <li>21 = einundzwanzig (one-and-twenty — reversed!)</li>
      </ul>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 1 — What number is this?</div>
    <div class="sg-exercise" id="ex1">
      <div class="sg-question">Which number is <em>sieben</em>?</div>
      <div class="sg-choices">
        <button class="sg-choice" data-correct="false">6</button>
        <button class="sg-choice" data-correct="true">7</button>
        <button class="sg-choice" data-correct="false">8</button>
        <button class="sg-choice" data-correct="false">17</button>
      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 2 — Type the German word</div>
    <div class="sg-exercise">
      <div class="sg-question">How do you write 12 in German?</div>
      <input class="sg-fill" id="fill2" placeholder="Type the German word…" autocomplete="off">
      <div class="sg-btn-row"><button class="sg-btn sg-btn-primary" id="fill2-btn">Check ✓</button></div>
      <div class="sg-feedback" id="fill2-fb"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 3 — Multiple choice</div>
    <div class="sg-exercise" id="ex3">
      <div class="sg-question">What does <em>zwanzig</em> mean?</div>
      <div class="sg-choices">
        <button class="sg-choice" data-correct="false">12</button>
        <button class="sg-choice" data-correct="false">12</button>
        <button class="sg-choice" data-correct="true">20</button>
        <button class="sg-choice" data-correct="false">2</button>
      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">🎤 Speaking Practice</div>
    <div class="sg-speak-card">
      <div class="sg-speak-phrase">fünf</div>
      <div class="sg-speak-translation">five</div>
      <button class="sg-btn sg-btn-audio" style="margin-bottom:10px" onclick="sgSpeak('fünf')">🔊 Hear it</button><br>
      <button class="sg-mic-btn" id="mic1" onclick="startMic('fünf','mic1','mic1-result')">🎤 Speak Now</button>
      <div class="sg-mic-result" id="mic1-result"></div>
    </div>
  </div>

  <script>
  const lc = new LessonController(2, 3);
  sgMultiChoice(document.getElementById('ex1'), { onDone: ok => lc.record(ok) });
  sgFillBlank(document.getElementById('fill2'), document.getElementById('fill2-btn'), document.getElementById('fill2-fb'),
    { answer: 'zwölf', onDone: ok => lc.record(ok) });
  sgMultiChoice(document.getElementById('ex3'), { onDone: ok => lc.record(ok) });

  function countUp() {
    const nums = ['eins','zwei','drei','vier','fünf','sechs','sieben','acht','neun','zehn'];
    nums.forEach((n, i) => setTimeout(() => sgSpeak(n), i * 900));
  }

  function startMic(phrase, btnId, resultId) {
    const btn = document.getElementById(btnId);
    const res = document.getElementById(resultId);
    btn.classList.add('listening'); btn.textContent = '🎙️ Listening…';
    sgListen(
      results => {
        btn.classList.remove('listening'); btn.textContent = '🎤 Speak Now';
        const check = sgCheckPronunciation(results, phrase);
        res.innerHTML = check.pass ? '✅ Excellent! (' + check.score + '%)' : '❌ Try again — you said: "' + results[0] + '"';
      },
      err => { btn.classList.remove('listening'); btn.textContent = '🎤 Speak Now'; res.textContent = '⚠️ ' + err; }
    );
  }
  </script>
"""),

3: ("Colours & Shapes", "Level A1", """
  <div class="sg-card">
    <div class="sg-section-title">📚 Colours (die Farben)</div>
    <table class="sg-vocab">
      <tr><th>German</th><th>English</th><th>Pronunciation</th><th></th></tr>
      <tr><td class="german" style="color:red">rot</td><td>red</td><td class="phonetic">rote</td><td><button class="sg-play-btn" onclick="sgSpeak('rot')">▶</button></td></tr>
      <tr><td class="german" style="color:blue">blau</td><td>blue</td><td class="phonetic">blau</td><td><button class="sg-play-btn" onclick="sgSpeak('blau')">▶</button></td></tr>
      <tr><td class="german" style="color:green">grün</td><td>green</td><td class="phonetic">grühn</td><td><button class="sg-play-btn" onclick="sgSpeak('grün')">▶</button></td></tr>
      <tr><td class="german" style="color:#DAA520">gelb</td><td>yellow</td><td class="phonetic">gelp</td><td><button class="sg-play-btn" onclick="sgSpeak('gelb')">▶</button></td></tr>
      <tr><td class="german">weiß</td><td>white</td><td class="phonetic">vice</td><td><button class="sg-play-btn" onclick="sgSpeak('weiß')">▶</button></td></tr>
      <tr><td class="german" style="color:#333">schwarz</td><td>black</td><td class="phonetic">shvarts</td><td><button class="sg-play-btn" onclick="sgSpeak('schwarz')">▶</button></td></tr>
      <tr><td class="german" style="color:orange">orange</td><td>orange</td><td class="phonetic">or-AHN-zhe</td><td><button class="sg-play-btn" onclick="sgSpeak('orange')">▶</button></td></tr>
      <tr><td class="german" style="color:purple">lila</td><td>purple/violet</td><td class="phonetic">LEE-la</td><td><button class="sg-play-btn" onclick="sgSpeak('lila')">▶</button></td></tr>
      <tr><td class="german" style="color:brown">braun</td><td>brown</td><td class="phonetic">brown</td><td><button class="sg-play-btn" onclick="sgSpeak('braun')">▶</button></td></tr>
      <tr><td class="german" style="color:gray">grau</td><td>grey</td><td class="phonetic">grau</td><td><button class="sg-play-btn" onclick="sgSpeak('grau')">▶</button></td></tr>
    </table>
  </div>

  <div class="sg-card">
    <div class="sg-grammar">
      <h4>📖 Grammar: Adjective Endings</h4>
      <p>When a colour comes before a noun, it takes an ending:</p>
      <table>
        <tr><th>Article</th><th>Example</th></tr>
        <tr><td>der (m)</td><td>der rote Hut (the red hat)</td></tr>
        <tr><td>die (f)</td><td>die blaue Tasse (the blue cup)</td></tr>
        <tr><td>das (n)</td><td>das grüne Auto (the green car)</td></tr>
      </table>
      <p style="margin-top:8px">After <em>sein</em> (to be), no ending needed: <em>Das Auto ist grün.</em></p>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 1</div>
    <div class="sg-exercise" id="ex1">
      <div class="sg-question">What colour is "gelb"?</div>
      <div class="sg-choices">
        <button class="sg-choice" data-correct="false">green</button>
        <button class="sg-choice" data-correct="true">yellow</button>
        <button class="sg-choice" data-correct="false">blue</button>
        <button class="sg-choice" data-correct="false">red</button>
      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 2</div>
    <div class="sg-exercise">
      <div class="sg-question">How do you say "black" in German?</div>
      <input class="sg-fill" id="fill2" placeholder="Type in German…" autocomplete="off">
      <div class="sg-btn-row"><button class="sg-btn sg-btn-primary" id="fill2-btn">Check ✓</button></div>
      <div class="sg-feedback" id="fill2-fb"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 3</div>
    <div class="sg-exercise" id="ex3">
      <div class="sg-question">Which sentence means "The car is red"?</div>
      <div class="sg-choices">
        <button class="sg-choice" data-correct="false">Das Auto ist blau.</button>
        <button class="sg-choice" data-correct="true">Das Auto ist rot.</button>
        <button class="sg-choice" data-correct="false">Die Auto ist rot.</button>
        <button class="sg-choice" data-correct="false">Das Rot ist Auto.</button>
      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">🎤 Speaking Practice</div>
    <div class="sg-speak-card">
      <div class="sg-speak-phrase">Das Auto ist rot.</div>
      <div class="sg-speak-translation">The car is red.</div>
      <button class="sg-btn sg-btn-audio" style="margin-bottom:10px" onclick="sgSpeak('Das Auto ist rot.')">🔊 Hear it</button><br>
      <button class="sg-mic-btn" id="mic1" onclick="startMic('Das Auto ist rot','mic1','mic1-result')">🎤 Speak Now</button>
      <div class="sg-mic-result" id="mic1-result"></div>
    </div>
  </div>

  <script>
  const lc = new LessonController(3, 3);
  sgMultiChoice(document.getElementById('ex1'), { onDone: ok => lc.record(ok) });
  sgFillBlank(document.getElementById('fill2'), document.getElementById('fill2-btn'), document.getElementById('fill2-fb'),
    { answer: 'schwarz', onDone: ok => lc.record(ok) });
  sgMultiChoice(document.getElementById('ex3'), { onDone: ok => lc.record(ok) });
  function startMic(phrase, btnId, resultId) {
    const btn=document.getElementById(btnId),res=document.getElementById(resultId);
    btn.classList.add('listening');btn.textContent='🎙️ Listening…';
    sgListen(r=>{btn.classList.remove('listening');btn.textContent='🎤 Speak Now';const c=sgCheckPronunciation(r,phrase);res.innerHTML=c.pass?'✅ Great! ('+c.score+'%)':'❌ You said: "'+r[0]+'" — try again!';},
    e=>{btn.classList.remove('listening');btn.textContent='🎤 Speak Now';res.textContent='⚠️ '+e;});
  }
  </script>
"""),

}

# ─── GENERIC LESSON TEMPLATE (for lessons without custom content) ─────────────
def generic_lesson(num, title, level, vocab_rows, grammar_html, ex1_q, ex1_choices, ex1_correct,
                   fill2_q, fill2_ans, ex3_q, ex3_choices, ex3_correct, speak_phrase, speak_trans):
    choices_html = ""
    for i, c in enumerate(ex1_choices):
        corr = "true" if i == ex1_correct else "false"
        choices_html += '        <button class="sg-choice" data-correct="%s">%s</button>\n' % (corr, c)
    choices3_html = ""
    for i, c in enumerate(ex3_choices):
        corr = "true" if i == ex3_correct else "false"
        choices3_html += '        <button class="sg-choice" data-correct="%s">%s</button>\n' % (corr, c)
    vocab_html = ""
    for row in vocab_rows:
        g, ph, en = row
        g_safe = g.replace("'", "\\'")
        vocab_html += '      <tr><td class="german">%s</td><td class="phonetic">%s</td><td>%s</td><td><button class="sg-play-btn" onclick="sgSpeak(\'%s\')">▶</button></td></tr>\n' % (g, ph, en, g_safe)

    sp_safe = speak_phrase.replace("'", "\\'")

    return """
  <div class="sg-card">
    <div class="sg-section-title">📚 Vocabulary</div>
    <table class="sg-vocab">
      <tr><th>German</th><th>Pronunciation</th><th>English</th><th></th></tr>
%(vocab)s    </table>
  </div>

  <div class="sg-card">
    <div class="sg-grammar">
%(grammar)s
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 1</div>
    <div class="sg-exercise" id="ex1">
      <div class="sg-question">%(ex1_q)s</div>
      <div class="sg-choices">
%(choices1)s      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 2 — Fill in the blank</div>
    <div class="sg-exercise">
      <div class="sg-question">%(fill2_q)s</div>
      <input class="sg-fill" id="fill2" placeholder="Type in German…" autocomplete="off">
      <div class="sg-btn-row"><button class="sg-btn sg-btn-primary" id="fill2-btn">Check ✓</button></div>
      <div class="sg-feedback" id="fill2-fb"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">✏️ Exercise 3</div>
    <div class="sg-exercise" id="ex3">
      <div class="sg-question">%(ex3_q)s</div>
      <div class="sg-choices">
%(choices3)s      </div>
      <div class="sg-feedback"></div>
    </div>
  </div>

  <div class="sg-card">
    <div class="sg-section-title">🎤 Speaking Practice</div>
    <div class="sg-speak-card">
      <div class="sg-speak-phrase">%(speak_phrase)s</div>
      <div class="sg-speak-translation">%(speak_trans)s</div>
      <button class="sg-btn sg-btn-audio" style="margin-bottom:10px" onclick="sgSpeak('%(sp_safe)s')">🔊 Hear it</button><br>
      <button class="sg-mic-btn" id="mic1" onclick="startMic('%(sp_safe)s','mic1','mic1-result')">🎤 Speak Now</button>
      <div class="sg-mic-result" id="mic1-result"></div>
    </div>
  </div>

  <script>
  const lc = new LessonController(%(num)d, 3);
  sgMultiChoice(document.getElementById('ex1'), { onDone: ok => lc.record(ok) });
  sgFillBlank(document.getElementById('fill2'), document.getElementById('fill2-btn'), document.getElementById('fill2-fb'),
    { answer: '%(fill2_ans)s', onDone: ok => lc.record(ok) });
  sgMultiChoice(document.getElementById('ex3'), { onDone: ok => lc.record(ok) });
  function startMic(phrase,btnId,resultId){
    const btn=document.getElementById(btnId),res=document.getElementById(resultId);
    btn.classList.add('listening');btn.textContent='🎙️ Listening…';
    sgListen(r=>{btn.classList.remove('listening');btn.textContent='🎤 Speak Now';const c=sgCheckPronunciation(r,phrase);res.innerHTML=c.pass?'✅ Great! ('+c.score+'%%)':'❌ You said: "'+r[0]+'" — try again!';
    },e=>{btn.classList.remove('listening');btn.textContent='🎤 Speak Now';res.textContent='⚠️ '+e;});
  }
  </script>
""" % {'vocab': vocab_html, 'grammar': grammar_html, 'ex1_q': ex1_q,
       'choices1': choices_html, 'fill2_q': fill2_q, 'fill2_ans': fill2_ans,
       'ex3_q': ex3_q, 'choices3': choices3_html,
       'speak_phrase': speak_phrase, 'speak_trans': speak_trans,
       'sp_safe': sp_safe, 'num': num}

# Add generic lessons 4–30
generic_params = {
4: ("Family Members","Level A1",
    [("die Mutter","MOO-ter","mother"),("der Vater","FAH-ter","father"),("die Schwester","SHVES-ter","sister"),
     ("der Bruder","BROO-der","brother"),("die Großmutter","GROHSS-moo-ter","grandmother"),
     ("der Großvater","GROHSS-fah-ter","grandfather"),("das Kind","kint","child"),("die Familie","fah-MEE-lee-eh","family")],
    "<h4>📖 Grammar: Possessive Pronouns</h4><p>Use <strong>mein/meine</strong> (my) with family members:<br>mein Vater (m), meine Mutter (f), mein Kind (n).<br>The ending changes based on gender and case.</p>",
    "What does 'die Schwester' mean?",["brother","mother","sister","daughter"],2,
    "How do you say 'my father' in German (masculine)?","mein Vater",
    "Which is correct for 'my grandmother'?",
    ["mein Großmutter","meine Großmutter","meine Großvater","meinen Großmutter"],1,
    "Meine Mutter ist sehr nett.","My mother is very nice."),

5: ("Days, Months & Seasons","Level A1",
    [("Montag","MON-tahk","Monday"),("Dienstag","DEENS-tahk","Tuesday"),("Mittwoch","MIT-vokh","Wednesday"),
     ("Donnerstag","DON-ners-tahk","Thursday"),("Freitag","FRY-tahk","Friday"),
     ("Januar","YAN-oo-ar","January"),("Juni","YOO-nee","June"),("Dezember","deh-TSEM-ber","December"),
     ("der Frühling","FRÜH-ling","spring"),("der Sommer","ZOM-mer","summer"),("der Herbst","hairbst","autumn"),("der Winter","VIN-ter","winter")],
    "<h4>📖 Grammar: Days and Months</h4><ul><li>Days are all <strong>masculine</strong>: der Montag, der Freitag…</li><li>Months are also masculine: der Januar, der März…</li><li>Use <em>am</em> for days: <em>am Montag</em> (on Monday)</li><li>Use <em>im</em> for months: <em>im Januar</em> (in January)</li></ul>",
    "Which day comes after Mittwoch?",["Dienstag","Freitag","Donnerstag","Montag"],2,
    "How do you say 'on Monday' in German?","am Montag",
    "What does 'der Herbst' mean?",["spring","summer","autumn","winter"],2,
    "Heute ist Montag.","Today is Monday."),

6: ("Food & Drink","Level A1",
    [("das Brot","broht","bread"),("die Milch","milkh","milk"),("das Wasser","VAS-ser","water"),
     ("der Kaffee","KAF-fay","coffee"),("der Tee","tay","tea"),("das Fleisch","flysh","meat"),
     ("das Gemüse","geh-MÜ-ze","vegetables"),("der Käse","KAY-ze","cheese"),
     ("das Obst","ohpst","fruit"),("die Suppe","ZOO-pe","soup")],
    "<h4>📖 Grammar: Ich möchte (I would like)</h4><p>Use <strong>ich möchte</strong> to order or request politely:<br><em>Ich möchte ein Brot, bitte.</em> (I would like a bread, please.)<br><em>Ich möchte einen Kaffee.</em> (I would like a coffee.)</p>",
    "What is 'das Wasser'?",["milk","coffee","water","tea"],2,
    "How do you say 'I would like' in German?","ich möchte",
    "Which phrase correctly orders coffee?",
    ["Ich möchte einen Kaffee.","Ich will Kaffee jetzt.","Kaffee ich bitte.","Möchte ich Kaffee?"],0,
    "Ich möchte ein Wasser, bitte.","I would like a water, please."),

7: ("German Articles (der/die/das)","Level A1",
    [("der Mann","man","the man (m)"),("die Frau","frow","the woman (f)"),("das Kind","kint","the child (n)"),
     ("der Tisch","tish","the table (m)"),("die Tür","tür","the door (f)"),("das Buch","bookh","the book (n)"),
     ("der Hund","hoont","the dog (m)"),("die Katze","KAT-se","the cat (f)")],
    "<h4>📖 Grammar: der / die / das</h4><p>Every German noun has a gender — masculine (<strong>der</strong>), feminine (<strong>die</strong>), or neuter (<strong>das</strong>). You must learn the article with each noun.</p><table><tr><th>Gender</th><th>Article</th><th>Example</th></tr><tr><td>Masculine</td><td>der</td><td>der Hund</td></tr><tr><td>Feminine</td><td>die</td><td>die Katze</td></tr><tr><td>Neuter</td><td>das</td><td>das Buch</td></tr></table><p style='margin-top:8px'>Plural is always <strong>die</strong>: die Männer, die Frauen…</p>",
    "Which article goes with 'Frau' (woman)?",["der","die","das","ein"],1,
    "Write the correct article for 'Buch' (book):","das",
    "Which is correct?",["der Katze","das Katze","die Katze","ein Katze"],2,
    "Der Hund ist groß.","The dog is big."),

8: ("Basic Verbs","Level A1",
    [("sein","zayn","to be"),("haben","HAH-ben","to have"),("machen","MAKH-en","to do/make"),
     ("gehen","GAY-en","to go"),("kommen","KOM-en","to come"),("sehen","ZAY-en","to see"),
     ("essen","ES-en","to eat"),("trinken","TRIN-ken","to drink"),("sprechen","SHPREKH-en","to speak"),
     ("lernen","LERN-en","to learn")],
    "<h4>📖 Grammar: Present Tense of 'sein' (to be)</h4><table><tr><th>Pronoun</th><th>Form</th></tr><tr><td>ich</td><td>bin</td></tr><tr><td>du</td><td>bist</td></tr><tr><td>er/sie/es</td><td>ist</td></tr><tr><td>wir</td><td>sind</td></tr><tr><td>ihr</td><td>seid</td></tr><tr><td>Sie/sie</td><td>sind</td></tr></table>",
    "What does 'trinken' mean?",["to eat","to see","to drink","to go"],2,
    "How do you say 'I am' in German?","ich bin",
    "Which is correct for 'We are students'?",
    ["Wir bin Studenten.","Wir sind Studenten.","Wir seid Studenten.","Ich sind Studenten."],1,
    "Ich lerne Deutsch.","I am learning German."),

9: ("Asking Questions","Level A1",
    [("wer","vair","who"),("was","vas","what"),("wo","voh","where"),("wann","van","when"),
     ("warum","va-ROOM","why"),("wie","vee","how"),("wie viel","vee feel","how much"),
     ("welche","VEL-kheh","which")],
    "<h4>📖 Grammar: Question Words (W-Fragen)</h4><p>German question words mostly start with <strong>W</strong>. The verb comes second:<br><em>Wo wohnst du?</em> (Where do you live?)<br><em>Was machst du?</em> (What are you doing?)<br><em>Wie heißt du?</em> (What is your name?)</p>",
    "What does 'warum' mean?",["where","when","why","how"],2,
    "How do you ask 'Where do you live?' in German?","wo wohnst du",
    "Which question asks for a name?",
    ["Wo heißt du?","Was heißt du?","Wie heißt du?","Wer heißt du?"],2,
    "Wie heißt du?","What is your name?"),

10: ("Introducing Yourself","Level A1",
    [("ich heiße","ICH HY-se","my name is"),("ich komme aus","ICH KOM-e ows","I come from"),
     ("ich wohne in","ICH VOH-ne in","I live in"),("ich bin … Jahre alt","","I am … years old"),
     ("ich spreche","ICH SHPREKH-e","I speak"),("schön, Sie kennenzulernen","","nice to meet you (formal)")],
    "<h4>📖 Grammar: Talking About Yourself</h4><p>Key phrases for introductions:<br><em>Ich heiße Maria.</em> (My name is Maria.)<br><em>Ich komme aus England.</em> (I come from England.)<br><em>Ich bin dreißig Jahre alt.</em> (I am 30 years old.)<br><em>Ich spreche ein bisschen Deutsch.</em> (I speak a little German.)</p>",
    "How do you say 'My name is …'?",["Ich bin…","Ich heiße…","Ich habe…","Ich komme…"],1,
    "Translate: 'I come from England'","ich komme aus England",
    "Which phrase means 'nice to meet you'?",
    ["Auf Wiedersehen","Schön, Sie kennenzulernen","Wie geht es?","Tschüss"],1,
    "Ich heiße Michael. Ich komme aus England.","My name is Michael. I come from England."),

11: ("Simple Sentences","Level A2",
    [("das ist","das ist","this is"),("es gibt","es gipt","there is/are"),
     ("ich habe","ICH HAH-be","I have"),("ich mag","ICH mahk","I like"),
     ("ich brauche","ICH BROW-khe","I need"),("ich verstehe","ICH fer-SHTAY-e","I understand")],
    "<h4>📖 Grammar: German Sentence Structure</h4><p>Basic German word order: <strong>Subject – Verb – Object</strong><br><em>Ich esse Brot.</em> (I eat bread.)<br>With time expressions, the verb still stays second:<br><em>Heute esse ich Brot.</em> (Today I eat bread.)<br>Negation: add <strong>nicht</strong> (not) or <strong>kein/keine</strong> before nouns.</p>",
    "Which sentence has correct word order?",
    ["Ich Brot esse.","Brot esse ich.","Ich esse Brot.","Esse Brot ich."],2,
    "How do you say 'I need water'?","ich brauche Wasser",
    "Which is correct negation for 'I don't have a cat'?",
    ["Ich habe nicht eine Katze.","Ich habe keine Katze.","Ich keine habe Katze.","Ich habe Katze nicht."],1,
    "Ich verstehe das nicht.","I don't understand that."),

12: ("Present Tense Conjugation","Level A2",
    [("lernen","LERN-en","to learn"),("wohnen","VOH-nen","to live"),("spielen","SHPEE-len","to play"),
     ("kaufen","KOW-fen","to buy"),("arbeiten","AR-by-ten","to work"),("schreiben","SHRY-ben","to write")],
    "<h4>📖 Grammar: Regular Verb Endings (Präsens)</h4><table><tr><th>Pronoun</th><th>Ending</th><th>lernen</th></tr><tr><td>ich</td><td>-e</td><td>lerne</td></tr><tr><td>du</td><td>-st</td><td>lernst</td></tr><tr><td>er/sie/es</td><td>-t</td><td>lernt</td></tr><tr><td>wir</td><td>-en</td><td>lernen</td></tr><tr><td>ihr</td><td>-t</td><td>lernt</td></tr><tr><td>Sie/sie</td><td>-en</td><td>lernen</td></tr></table>",
    "What is the correct form of 'lernen' for 'du'?",
    ["lerne","lernst","lernt","lernen"],1,
    "Conjugate 'wohnen' for 'er' (he):","wohnt",
    "Which is correct for 'We play'?",
    ["Wir spielst.","Wir spiele.","Wir spielen.","Wir spielet."],2,
    "Er arbeitet in Berlin.","He works in Berlin."),

13: ("Directions & Places","Level A2",
    [("links","links","left"),("rechts","rekhts","right"),("geradeaus","ge-RAH-de-ows","straight ahead"),
     ("die Straße","SHTRAHS-e","street"),("die Ampel","AM-pel","traffic light"),("das Rathaus","RAHT-hows","town hall"),
     ("der Bahnhof","BAHN-hof","train station"),("weit von hier","vayt fon heer","far from here"),
     ("nah bei","nah by","close to"),("gegenüber","gay-gen-Ü-ber","opposite")],
    "<h4>📖 Grammar: Asking for Directions</h4><p><em>Entschuldigung, wo ist der Bahnhof?</em> (Where is the station?)<br><em>Biegen Sie links ab.</em> (Turn left — formal)<br><em>Gehen Sie geradeaus.</em> (Go straight ahead.)<br>Use <strong>Wie weit ist es?</strong> to ask how far something is.</p>",
    "What does 'geradeaus' mean?",["turn right","turn left","straight ahead","behind you"],2,
    "Translate: 'the train station'","der Bahnhof",
    "How do you ask 'Where is the town hall?'",
    ["Wie ist das Rathaus?","Wo ist das Rathaus?","Was ist das Rathaus?","Wann ist das Rathaus?"],1,
    "Gehen Sie geradeaus, dann links.","Go straight ahead, then turn left."),

14: ("Shopping & Prices","Level A2",
    [("Was kostet…?","vas KOS-tet","How much does … cost?"),("Es kostet…","es KOS-tet","It costs…"),
     ("das Geschäft","ghe-SHEFT","the shop"),("der Supermarkt","ZOO-per-markt","supermarket"),
     ("teuer","TOY-er","expensive"),("billig","BIL-ig","cheap"),("der Euro","OY-ro","euro"),
     ("die Quittung","KVIT-ung","receipt"),("kaufen","KOW-fen","to buy"),("verkaufen","fer-KOW-fen","to sell")],
    "<h4>📖 Grammar: Prices</h4><p>Prices in German: <em>Es kostet fünf Euro.</em> (It costs 5 euros.)<br>Cents: <em>neunzig Cent</em> (90 cents)<br>Ask: <em>Haben Sie…?</em> (Do you have…?)<br>Say: <em>Ich nehme das.</em> (I'll take it.)</p>",
    "What does 'teuer' mean?",["cheap","free","expensive","sale"],2,
    "How do you ask the price?","Was kostet das",
    "Which phrase means 'I'll take it'?",
    ["Ich kaufe nicht.","Ich nehme das.","Das ist teuer.","Ich brauche das."],1,
    "Was kostet das Buch?","How much does the book cost?"),

15: ("Telling the Time","Level A2",
    [("Wie spät ist es?","vee shpayt ist es","What time is it?"),("Es ist … Uhr","es ist … oor","It is … o'clock"),
     ("halb","halp","half past"),("Viertel vor","FEER-tel for","quarter to"),
     ("Viertel nach","FEER-tel nakh","quarter past"),("morgens","MOR-gens","in the morning"),
     ("abends","AH-bents","in the evening"),("mittags","MIT-tahks","at midday")],
    "<h4>📖 Grammar: Telling the Time</h4><table><tr><th>German</th><th>English</th></tr><tr><td>Es ist drei Uhr.</td><td>It is 3 o'clock.</td></tr><tr><td>Es ist halb vier.</td><td>It is 3:30 (half four).</td></tr><tr><td>Viertel nach zwei.</td><td>Quarter past two.</td></tr><tr><td>Viertel vor sechs.</td><td>Quarter to six.</td></tr></table><p style='margin-top:8px'>⚠️ <em>halb vier</em> means 3:30, not 4:30 — it means 'half of four'!</p>",
    "What does 'halb vier' mean?",["4:30","3:30","4:15","3:15"],1,
    "How do you ask 'What time is it?'","Wie spät ist es",
    "Which says 'quarter past five'?",
    ["Viertel vor fünf","Viertel nach fünf","halb fünf","fünf Uhr"],1,
    "Es ist halb neun.","It is half past eight."),

16: ("Weather","Level A2",
    [("das Wetter","VET-er","the weather"),("Es regnet.","es RAYG-net","It is raining."),
     ("Es schneit.","es SHNAYT","It is snowing."),("Es ist sonnig.","es ist ZON-ig","It is sunny."),
     ("Es ist bewölkt.","es ist be-VÖLKT","It is cloudy."),("Es ist kalt.","es ist kalt","It is cold."),
     ("Es ist warm.","es ist varm","It is warm."),("der Regen","RAY-gen","rain"),
     ("der Schnee","shnay","snow"),("die Sonne","ZON-e","sun")],
    "<h4>📖 Grammar: Weather Sentences</h4><p>Weather in German uses <strong>es</strong> (it) as the subject:<br><em>Es regnet.</em> (It rains / is raining.)<br><em>Es ist heiß.</em> (It is hot.)<br>Ask: <em>Wie ist das Wetter heute?</em> (What is the weather today?)</p>",
    "What does 'Es schneit' mean?",["It is sunny","It is raining","It is snowing","It is windy"],2,
    "Translate: 'It is cold'","Es ist kalt",
    "How do you ask about the weather?",
    ["Was ist das Wetter?","Wie ist das Wetter?","Wo ist das Wetter?","Wann ist das Wetter?"],1,
    "Wie ist das Wetter heute?","What is the weather today?"),

17: ("Home & Rooms","Level A2",
    [("das Haus","hows","house"),("die Wohnung","VOH-nung","flat/apartment"),
     ("die Küche","KÜ-khe","kitchen"),("das Wohnzimmer","VOHN-tsim-er","living room"),
     ("das Schlafzimmer","SHLAHF-tsim-er","bedroom"),("das Badezimmer","BAH-de-tsim-er","bathroom"),
     ("der Garten","GAR-ten","garden"),("der Keller","KEL-er","cellar"),
     ("das Fenster","FEN-ster","window"),("die Tür","tür","door")],
    "<h4>📖 Grammar: Location with 'in'</h4><p>Use <strong>im</strong> (in dem) with rooms:<br><em>Ich bin im Schlafzimmer.</em> (I am in the bedroom.)<br><em>Das Buch liegt im Wohnzimmer.</em> (The book is in the living room.)<br>Use <strong>ins</strong> (in das) for movement into: <em>Ich gehe ins Badezimmer.</em></p>",
    "What is 'die Küche'?",["bedroom","bathroom","kitchen","living room"],2,
    "How do you say 'the living room'?","das Wohnzimmer",
    "Which sentence means 'I am in the garden'?",
    ["Ich bin im Garten.","Ich bin in Garten.","Ich gehe im Garten.","Ich bin der Garten."],0,
    "Mein Schlafzimmer ist groß.","My bedroom is big."),

18: ("Transport & Travel","Level A2",
    [("der Zug","tsook","train"),("der Bus","boos","bus"),("das Auto","OW-to","car"),
     ("das Flugzeug","FLOOK-tsoyk","plane"),("das Fahrrad","FAR-raht","bicycle"),
     ("der Bahnhof","BAHN-hof","train station"),("das Ticket","TIK-et","ticket"),
     ("abfahren","AP-far-en","to depart"),("ankommen","AN-kom-en","to arrive"),
     ("der Flughafen","FLOOK-hah-fen","airport")],
    "<h4>📖 Grammar: Separable Verbs</h4><p>Some German verbs split in a sentence — the prefix goes to the end:<br><em>abfahren</em> → Der Zug <strong>fährt</strong> um 8 Uhr <strong>ab</strong>.<br><em>ankommen</em> → Wir <strong>kommen</strong> um 10 Uhr <strong>an</strong>.<br>This is common in travel vocabulary.</p>",
    "What is 'das Flugzeug'?",["train","bus","plane","ship"],2,
    "Translate: 'the train station'","der Bahnhof",
    "Which sentence has correct separable verb placement?",
    ["Der Zug abfährt um acht.","Der Zug fährt ab um acht.","Der Zug fährt um acht ab.","Ab fährt der Zug um acht."],2,
    "Wann fährt der nächste Zug ab?","When does the next train depart?"),

19: ("Body Parts & Health","Level A2",
    [("der Kopf","kopf","head"),("der Arm","arm","arm"),("das Bein","bayn","leg"),
     ("die Hand","hant","hand"),("der Fuß","foos","foot"),("der Rücken","RÜ-ken","back"),
     ("der Bauch","bowkh","stomach"),("Ich bin krank.","ICH bin krank","I am ill."),
     ("Ich habe Schmerzen.","ICH HAH-be SHMERTS-en","I have pain."),
     ("der Arzt","artst","doctor")],
    "<h4>📖 Grammar: Saying You Feel Ill</h4><p><em>Mir ist schlecht.</em> (I feel sick.)<br><em>Ich habe Kopfschmerzen.</em> (I have a headache.)<br><em>Ich habe Bauchschmerzen.</em> (I have a stomachache.)<br>Body part + <strong>-schmerzen</strong> = that body part hurts.</p>",
    "What is 'der Rücken'?",["arm","leg","back","head"],2,
    "How do you say 'I have pain'?","Ich habe Schmerzen",
    "Which means 'I have a headache'?",
    ["Ich habe Beinschmerzen.","Ich habe Rückenschmerzen.","Ich habe Kopfschmerzen.","Ich habe Bauchschmerzen."],2,
    "Ich habe Kopfschmerzen.","I have a headache."),

20: ("Adjectives & Descriptions","Level A2",
    [("groß","grohss","big/tall"),("klein","klayn","small"),("schön","shön","beautiful"),
     ("alt","alt","old"),("jung","yung","young"),("schnell","shnel","fast"),
     ("langsam","LANG-zahm","slow"),("laut","lowt","loud"),("leise","LY-ze","quiet"),
     ("freundlich","FROYND-likh","friendly")],
    "<h4>📖 Grammar: Adjective Position</h4><p><strong>After</strong> the verb (predicative): no ending needed.<br><em>Das Haus ist groß.</em> (The house is big.)<br><strong>Before</strong> the noun (attributive): endings added.<br><em>das große Haus</em> (the big house)<br><em>ein großes Haus</em> (a big house)</p>",
    "What does 'freundlich' mean?",["unfriendly","fast","friendly","loud"],2,
    "Translate: 'The house is big'","Das Haus ist groß",
    "Which sentence means 'The dog is small'?",
    ["Der Hund ist klein.","Der Hund ist groß.","Die Hund ist klein.","Das Hund ist klein."],0,
    "Der Mann ist sehr freundlich.","The man is very friendly."),

21: ("Past Tense (Perfekt)","Level B1",
    [("haben + Partizip","","have + past participle"),("sein + Partizip","","be + past participle"),
     ("gegessen","ge-ES-en","eaten"),("getrunken","ge-TRUNK-en","drunk"),
     ("gegangen","ge-GANG-en","gone"),("gekauft","ge-KOWFT","bought"),
     ("gesehen","ge-ZAY-en","seen"),("gemacht","ge-MAKHT","done/made")],
    "<h4>📖 Grammar: The Perfekt Tense</h4><p>German uses <em>Perfekt</em> for everyday past conversation:<br><strong>haben/sein + past participle</strong><br><em>Ich habe Brot gegessen.</em> (I ate bread.)<br><em>Ich bin nach Hause gegangen.</em> (I went home.)<br>Motion/change verbs use <strong>sein</strong>; most others use <strong>haben</strong>.<br>Regular participles: ge- + stem + -t: kaufen → <em>gekauft</em></p>",
    "Which auxiliary verb is used with movement verbs?",["haben","sein","werden","mögen"],1,
    "What is the past participle of 'kaufen'?","gekauft",
    "Which is correct for 'I ate pizza'?",
    ["Ich bin Pizza gegessen.","Ich habe Pizza gegessen.","Ich habe Pizza essen.","Ich hatte Pizza gegessen."],1,
    "Ich habe heute Kaffee getrunken.","I drank coffee today."),

22: ("Modal Verbs","Level B1",
    [("können","KÖN-en","can / to be able to"),("müssen","MÜS-en","must / to have to"),
     ("wollen","VOL-en","to want to"),("dürfen","DÜR-fen","may / to be allowed to"),
     ("sollen","ZOL-en","should / to be supposed to"),("mögen","MÖ-gen","to like")],
    "<h4>📖 Grammar: Modal Verbs</h4><p>Modal verbs pair with an <strong>infinitive at the end</strong>:<br><em>Ich <strong>kann</strong> Deutsch <strong>sprechen</strong>.</em> (I can speak German.)<br><em>Du <strong>musst</strong> das <strong>lernen</strong>.</em> (You must learn that.)<br>Conjugation: modals are irregular and drop umlaut in most forms:<br>können → ich kann, du kannst, er kann, wir können…</p>",
    "Which modal means 'must'?",["können","dürfen","müssen","wollen"],2,
    "Complete: 'Ich ___ Deutsch sprechen.' (I can speak German)","kann",
    "Which is a correct modal verb sentence?",
    ["Ich will gehen.","Ich will gehe.","Will ich gehen.","Ich gehe will."],0,
    "Ich kann ein bisschen Deutsch sprechen.","I can speak a little German."),

23: ("Opinions & Preferences","Level B1",
    [("Ich finde…","ICH FIN-de","I find / think…"),("Ich mag…","ICH mahk","I like…"),
     ("Ich mag … nicht","","I don't like…"),("Ich denke, dass…","ICH DEN-ke das","I think that…"),
     ("Meiner Meinung nach…","MY-ner MY-nung nakh","In my opinion…"),
     ("Das gefällt mir.","das ge-FÄLT meer","I like that. (lit: it pleases me)")],
    "<h4>📖 Grammar: Saying Opinions with 'dass'</h4><p>After <em>ich denke, dass</em> the verb goes to the END:<br><em>Ich denke, dass Deutsch schwer <strong>ist</strong>.</em><br><em>Ich glaube, dass er Recht <strong>hat</strong>.</em><br>This is called a <strong>subordinate clause</strong> — the verb always comes last.</p>",
    "What does 'Meiner Meinung nach' mean?",["I think","I know","In my opinion","I prefer"],2,
    "Translate: 'I like music'","Ich mag Musik",
    "Which is correct? 'I think that German is interesting.'",
    ["Ich denke, dass ist Deutsch interessant.","Ich denke, dass Deutsch interessant ist.","Ich denke Deutsch ist interessant dass.","Deutsch interessant ist, ich denke."],1,
    "Ich finde Deutsch sehr interessant.","I find German very interesting."),

24: ("Travel & Accommodation","Level B1",
    [("das Hotel","ho-TEL","hotel"),("das Zimmer","TSIM-er","room"),
     ("reservieren","re-zer-VEER-en","to reserve"),("einchecken","AYN-chek-en","to check in"),
     ("auschecken","OWS-chek-en","to check out"),("der Reisepass","RY-ze-pas","passport"),
     ("der Koffer","KOF-er","suitcase"),("die Unterkunft","UN-ter-kunft","accommodation"),
     ("das Frühstück","FRÜ-shtük","breakfast"),("pro Nacht","pro nakht","per night")],
    "<h4>📖 Grammar: Polite Requests with 'ich hätte gern'</h4><p><em>Ich hätte gern ein Zimmer.</em> (I would like a room.)<br><em>Haben Sie ein Zimmer frei?</em> (Do you have a room free?)<br><em>Für wie viele Nächte?</em> (For how many nights?)<br><em>Mit Frühstück, bitte.</em> (With breakfast, please.)</p>",
    "What is 'der Reisepass'?",["suitcase","passport","hotel","room"],1,
    "How do you ask 'Do you have a room free?'","Haben Sie ein Zimmer frei",
    "Which phrase books a room politely?",
    ["Ich will ein Zimmer.","Gib mir ein Zimmer.","Ich hätte gern ein Zimmer.","Zimmer, bitte sofort."],2,
    "Ich hätte gern ein Zimmer für zwei Nächte.","I would like a room for two nights."),

25: ("At the Restaurant","Level B1",
    [("der Tisch","tish","table"),("die Speisekarte","SHPY-ze-kar-te","menu"),
     ("bestellen","be-SHTEL-en","to order"),("empfehlen","em-PFAY-len","to recommend"),
     ("die Vorspeise","FOR-shpy-ze","starter"),("das Hauptgericht","HOWPT-ge-rikht","main course"),
     ("der Nachtisch","NAKHT-ish","dessert"),("die Rechnung","REKH-nung","the bill"),
     ("Es schmeckt gut.","es shmekt goot","It tastes good."),("zum Wohl!","tsoom vohl","Cheers!")],
    "<h4>📖 Grammar: Ordering Food</h4><p><em>Einen Tisch für zwei, bitte.</em> (A table for two, please.)<br><em>Ich nehme die Suppe.</em> (I'll have the soup.)<br><em>Was empfehlen Sie?</em> (What do you recommend?)<br><em>Die Rechnung, bitte.</em> (The bill, please.)</p>",
    "What is 'die Speisekarte'?",["the bill","the menu","the dessert","the table"],1,
    "How do you ask for the bill?","Die Rechnung bitte",
    "Which phrase orders a starter?",
    ["Ich nehme das Hauptgericht.","Ich nehme die Vorspeise.","Ich hätte gern den Nachtisch.","Die Rechnung, bitte."],1,
    "Die Rechnung, bitte.","The bill, please."),

26: ("Health & Doctor Visit","Level B1",
    [("Ich bin krank.","ICH bin krank","I am ill."),("Ich habe Fieber.","","I have a fever."),
     ("Ich habe Schmerzen.","","I have pain."),("der Arzt / die Ärztin","artst / ERTS-tin","doctor (m/f)"),
     ("das Rezept","re-TSEPT","prescription"),("die Apotheke","a-po-TAY-ke","pharmacy"),
     ("der Krankenwagen","KRAN-ken-vah-gen","ambulance"),("allergisch gegen","a-LER-gish GAY-gen","allergic to"),
     ("Nehmen Sie…","NAY-men zee","Take…"),("Wie lange schon?","vee LAN-ge shon","How long already?")],
    "<h4>📖 Grammar: 'seit' (since / for)</h4><p>Use <strong>seit</strong> to say how long you have had a symptom:<br><em>Ich habe seit drei Tagen Kopfschmerzen.</em><br>(I have had a headache for three days.)<br>Note: German uses <strong>present tense</strong> + seit (not past tense like English).</p>",
    "What is 'die Apotheke'?",["hospital","doctor's office","pharmacy","ambulance"],2,
    "How do you say 'I have a fever'?","Ich habe Fieber",
    "Which correctly says 'I have had a cold for two days'?",
    ["Ich hatte zwei Tage Erkältung.","Ich habe seit zwei Tagen eine Erkältung.","Ich bin seit zwei Tage krank.","Ich habe zwei Tage Erkältung gehabt."],1,
    "Ich habe seit zwei Tagen Fieber.","I have had a fever for two days."),

27: ("Hobbies & Free Time","Level B1",
    [("das Hobby","HOB-ee","hobby"),("lesen","LAY-zen","to read"),("Musik hören","moo-ZEEK HÖ-ren","to listen to music"),
     ("Sport treiben","sport TRY-ben","to do sport"),("reisen","RY-zen","to travel"),
     ("kochen","KOKH-en","to cook"),("zeichnen","TSAYKH-nen","to draw"),
     ("wandern","VAN-dern","to hike"),("tanzen","TAN-tsen","to dance"),
     ("in meiner Freizeit","in MY-ner FRY-tsayt","in my free time")],
    "<h4>📖 Grammar: 'gern' — Expressing Likes</h4><p>Add <strong>gern</strong> after the verb to say you like doing something:<br><em>Ich lese gern.</em> (I like reading.)<br><em>Er kocht gern.</em> (He likes cooking.)<br>For dislike: <em>nicht gern</em><br><em>Ich tanze nicht gern.</em> (I don't like dancing.)</p>",
    "What does 'wandern' mean?",["to dance","to swim","to hike","to travel"],2,
    "How do you say 'I like cooking'?","Ich koche gern",
    "Which means 'She likes reading'?",
    ["Sie liest nicht gern.","Sie liest gern.","Sie gern liest.","Gern sie liest."],1,
    "In meiner Freizeit lese ich gern.","In my free time I like reading."),

28: ("Work & Professions","Level B1",
    [("der Beruf","be-ROOF","profession"),("der Lehrer / die Lehrerin","","teacher (m/f)"),
     ("der Arzt / die Ärztin","","doctor (m/f)"),("der Ingenieur","in-zhe-NYÖR","engineer"),
     ("arbeiten","AR-by-ten","to work"),("die Firma","FIR-ma","company"),
     ("das Büro","bü-ROH","office"),("der Kollege","kol-LAY-ge","colleague"),
     ("die Besprechung","be-SHPREKH-ung","meeting"),("das Gehalt","ge-HALT","salary")],
    "<h4>📖 Grammar: Professions — No Article After 'sein'</h4><p>Unlike English, German does NOT use an article after <em>sein</em> for professions:<br>✅ <em>Ich bin Lehrer.</em> (I am a teacher.)<br>❌ <em>Ich bin ein Lehrer.</em> — incorrect<br>Female forms: add <strong>-in</strong>: Lehrer → Lehrerin, Arzt → Ärztin</p>",
    "What does 'das Büro' mean?",["factory","shop","office","company"],2,
    "Correctly say 'I am a doctor' (male):","Ich bin Arzt",
    "How do you say 'She is a teacher'?",
    ["Sie ist eine Lehrerin.","Sie ist Lehrerin.","Sie ist der Lehrer.","Sie sind Lehrerin."],1,
    "Ich arbeite in einem Büro in Berlin.","I work in an office in Berlin."),

29: ("German Culture & Customs","Level B1",
    [("das Oktoberfest","ok-TOH-ber-fest","Oktoberfest beer festival"),("der Weihnachtsmarkt","VY-nakhts-markt","Christmas market"),
     ("der Karneval","KAR-ne-val","carnival"),("Prosit!","PROH-zit","Cheers!"),
     ("Mahlzeit!","MAHL-tsayt","Enjoy your meal!"),("Guten Appetit!","GOO-ten a-pe-TEET","Bon appétit!"),
     ("das Bundesland","BOON-des-lant","federal state"),("die Autobahn","OW-to-bahn","motorway"),
     ("pünktlich","PÜNGKT-likh","punctual"),("das Pfand","pfant","bottle deposit")],
    "<h4>📖 Culture Notes</h4><ul><li>Germany has 16 <em>Bundesländer</em> (federal states)</li><li>The <em>Autobahn</em> has no general speed limit</li><li>Germans value <em>Pünktlichkeit</em> (punctuality)</li><li><em>Pfand</em> — you pay a deposit on bottles and get it back when you return them</li><li>Shops are closed on Sundays in most of Germany</li></ul>",
    "What is 'pünktlich'?",["friendly","punctual","reliable","formal"],1,
    "What is the Pfand system?","bottle deposit",
    "What does 'Mahlzeit' mean?",
    ["Good morning","Cheers","Enjoy your meal","Good night"],2,
    "Guten Appetit! Das Essen schmeckt sehr gut.","Bon appétit! The food tastes very good."),

30: ("Review & Conversation","Level B1",
    [("Können Sie das wiederholen?","","Can you repeat that?"),("Ich habe eine Frage.","","I have a question."),
     ("Wie sagt man … auf Deutsch?","","How do you say … in German?"),
     ("Ich verstehe nicht ganz.","","I don't fully understand."),
     ("Sprechen Sie bitte langsamer.","","Please speak more slowly."),
     ("Das macht Spaß!","","That is fun!"),("Ich lerne gern Deutsch.","","I like learning German.")],
    "<h4>📖 Grammar Review: Key Rules</h4><ul><li><strong>Articles</strong>: der (m), die (f), das (n)</li><li><strong>Verb position</strong>: verb is always 2nd in a main clause</li><li><strong>Perfekt</strong>: haben/sein + past participle</li><li><strong>Modals</strong>: modal verb 2nd, infinitive last</li><li><strong>Subordinate clauses</strong>: verb goes to the end after dass/weil/wenn</li></ul>",
    "How do you ask 'Can you repeat that?'",
    ["Wie bitte?","Können Sie das wiederholen?","Sprechen Sie langsamer.","Ich verstehe nicht."],1,
    "Translate: 'That is fun!'","Das macht Spaß",
    "Which sentence is correct?",
    ["Ich weil lerne Deutsch gern.","Ich lerne, weil Deutsch gern.","Ich lerne Deutsch, weil es Spaß macht.","Weil Deutsch Spaß macht ich lerne."],2,
    "Ich lerne gern Deutsch, weil es Spaß macht.","I like learning German because it is fun."),
}

# Add generic lessons
for num, params in generic_params.items():
    title, level, vocab_rows, grammar_html, ex1_q, ex1_choices, ex1_correct, \
        fill2_q, fill2_ans, ex3_q, ex3_choices, ex3_correct, speak_phrase, speak_trans = params
    lessons_data[num] = (title, level,
        generic_lesson(num, title, level, vocab_rows, grammar_html,
                       ex1_q, ex1_choices, ex1_correct,
                       fill2_q, fill2_ans,
                       ex3_q, ex3_choices, ex3_correct,
                       speak_phrase, speak_trans))

# Write all lesson files
for num in range(1, 31):
    if num not in lessons_data:
        print(f"WARNING: Lesson {num} missing!")
        continue
    title, level, body = lessons_data[num]
    html = lesson_shell(num, title, level, body)
    fname = os.path.join(OUT, f"lesson{pad(num)}.html")
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Written lesson {pad(num)}: {title}")

print("\n🎉 All 30 lessons generated!")
