# Generates landing/site/index.html (static HTML, so every feature is in the markup for SEO).
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'site' / 'index.html'

# Bump when the light clips are re-cut under the same file names (browser cache busting).
LIGHT_V = '4'

def video(name, label, cls='phone'):
    return (f'<figure class="{cls}"><div class="screen">'
            f'<video muted loop playsinline preload="none" data-clip="{name}" poster="media/{name}.jpg?v={LIGHT_V}" aria-label="{escape(label)}">'
            f'<source src="media/{name}.webm?v={LIGHT_V}" type="video/webm"><source src="media/{name}.mp4?v={LIGHT_V}" type="video/mp4"></video>'
            f'</div></figure>')

def row(i, tab, name, title, body, ticks):
    side = 'left' if i % 2 == 0 else 'right'
    lis = ''.join(f'<li style="--i:{k}"><i class="ph ph-check-circle" aria-hidden="true"></i><span>{t}</span></li>' for k, t in enumerate(ticks))
    return f'''
    <article class="feat" data-side="{side}">
      <div class="feat-media"><div class="fill blue" aria-hidden="true"></div>{video(name, title)}</div>
      <div class="feat-copy">
        <p class="caption-3 eyebrow">{tab}</p>
        <h3 class="heading-4">{title}</h3>
        <p class="body-3 muted">{body}</p>
        <ul class="ticks body-6">{lis}</ul>
      </div>
    </article>'''

def mini(i, name, title, body):
    return f'''
      <article class="mini" style="--i:{i}" data-from="{'left' if i % 2 == 0 else 'right'}">
        {video(name, title, 'phone phone-sm')}
        <h4 class="title-2">{title}</h4>
        <p class="body-6 muted">{body}</p>
      </article>'''

CHAPTERS = [
    dict(id='plan', num='01', tab='Blueprint', icon='ph-calendar-check', title='A week planned around you',
         lead='Tensora builds your training week from your height, weight, goal, experience, days per week and session length. Open the app and today is already laid out.',
         rows=[
            ('blueprint-today', 'Today, ready when you are',
             'Today’s session card shows where the workout came from, how long it takes and which regions it trains. Your weekly volume target sits right underneath, so you always know how far into the week you are.',
             ['Session length, exercise count and total sets at a glance', 'A source chip for program, routine or generated sessions', 'Weekly sets against your target, with the top muscles']),
            ('blueprint-swap-day', 'Change the whole day in one sheet',
             'Not feeling push day? Swap today for a rest day, another day of your program, one of your own routines, a generated session or any routine from the Coach library.',
             ['Recharge turns today into a rest day', 'Coach routines grouped in eight categories, with search', 'The swap lasts for today and survives an app restart']),
         ],
         minis=[]),
    dict(id='train', num='02', tab='Grind', icon='ph-barbell', title='Log sets without breaking focus',
         lead='Grind is the live workout screen. Big steppers, a rest timer that starts on its own and instructions one scroll away.',
         rows=[
            ('grind-log-set', 'Log a set in a few taps',
             'Pick the set type, step the weight and reps, tap Log set. The rest timer starts straight away and the set lands in the list below.',
             ['Working, warm up, drop and failure sets', 'Weight in kilograms or pounds, reps and optional effort', 'Every exercise keeps its own timer, so your workout time stays honest']),
            ('grind-how-to', 'Form cues and alternatives on the same screen',
             'Each exercise has numbered steps and a carousel of alternatives that hit the same muscle with other equipment. Bench taken? Swap to the cable version and keep going.',
             ['Step by step “How to perform” instructions', 'Alternatives for the same muscle and movement', 'Target muscles shown on the body']),
         ],
         minis=[]),
    dict(id='physique', num='03', tab='Physique', icon='ph-person-simple', title='See where your training actually lands',
         lead='Every working set is mapped onto the muscles it trains. Turn the body in 3D, switch the period and see what is growing and what is falling behind.',
         rows=[
            ('physique-3d', 'A muscle map you can turn in your hand',
             'Body distribution colours each muscle by the training it got against ideal training over the same period. Drag to rotate the full 3D model, or flip to the 2D front and back view.',
             ['2D or 3D, front and back', '100% means five hard sets, three times a week', 'Last week, last month or last year']),
            ('physique-recovery', 'Know what is ready to train',
             'The recovery estimate colours the body by how rested each muscle is and suggests what to train today instead.',
             ['Under 50%, recovering and ready states', 'Tap a muscle or a row for its estimate', 'A tip card names the muscles that are ready']),
            ('physique-strength', 'Strength and records from your own logs',
             'Below the map, a per muscle recovery list leads into Performance: a strength score with a running sparkline, weekly volume bars and a wall of records by body region.',
             ['Ready in times for muscles still recovering', 'Weekly volume bars', 'A PR wall grouped by body region']),
         ],
         minis=[]),
    dict(id='history', num='04', tab='Pivot', icon='ph-chart-bar', title='Every workout, every number, every streak',
         lead='Pivot is your training history. Charts, calendars, measurements and the full detail of every session you have logged.',
         rows=[
            ('pivot-training-chart', 'One chart, three ways to read it',
             'The Training card switches between duration, volume and reps, for this week, this month or this year, with the change against the previous period.',
             ['Duration, volume or reps', 'Week, month or year', 'A monthly summary of workouts, volume and streak']),
            ('pivot-workout-detail', 'The full story of each session',
             'Open any workout to see its time, volume, sets and reps, a muscle mix bar, and every set with its estimated one rep max and record badges.',
             ['Estimated one rep max on every set', 'Weight, one rep max and volume record badges', 'Jump to the previous or next workout']),
            ('pivot-calendar-month', 'A calendar that keeps you honest',
             'Training days are marked with a flame and joined by streak bars. Scroll back through months and see exactly how consistent you have been.',
             ['Week streaks and runs within the month', 'Days and sessions per month', 'Tap a day to open its workouts']),
            ('pivot-measures', 'Measurements beyond body weight',
             'Track 16 kinds of measurement, from body weight and body fat to neck, chest and arm circumferences, each with its own trend chart and history.',
             ['A trend chart with a change pill', 'Tap an entry to edit it', 'Weight and height stay in sync with your profile']),
         ],
         minis=[
            ('pivot-stats-calendar', 'Balance radar and streaks', 'A hexagon radar shows how balanced your physique work is, next to the streak calendar.'),
            ('pivot-exercise-detail', 'Exercise pages', 'Progress charts, full history and how to notes for every exercise you have done.'),
            ('pivot-log-past-workout', 'Log a workout you forgot', 'Tap any past day and fill in the session you did not record at the time.'),
            ('pivot-year-heatmap', 'A year at a glance', 'Twelve monthly heatmaps shaded by sets, volume or duration.'),
         ]),
    dict(id='coach', num='05', tab='Coach', icon='ph-clipboard-text', title='Programs when you want structure',
         lead='Fifteen programs and thirty standalone routines, for the gym, for dumbbells only, for bodyweight, bands, suspension trainers and hotel rooms.',
         rows=[
            ('coach-program', 'Programs for every level and setup',
             'Browse fifteen programs, from Starter Full Body to Upper / Lower Hypertrophy. Each one shows its day routines and how to progress. Follow one and its days land on your training week, and Blueprint and Grind follow along.',
             ['Filters for goal, level, days per week and equipment', 'Day routines with time and muscles worked', 'Follow a program and Coach tracks the week for you']),
            ('coach-routine', 'Routines you can read before you start',
             'Each routine shows its time, exercise and set counts, a body map of the muscles it works, the equipment it needs and every exercise with sets, reps and rest.',
             ['Muscles worked on a front and back body map', 'Supersets grouped together', 'Start it now or save it to My routines']),
         ],
         minis=[]),
]

ALSO = [
    ('ph-ruler', 'Set up in four steps', 'Height and weight on ruler pickers, your goal (Aesthetic, Athletic or Powerlifter), your training setup and an optional baseline photo.'),
    ('ph-camera', 'A proper workout summary', 'Name the session, see duration, volume and sets, add photos from the camera or library and choose who can see it.'),
    ('ph-cloud-check', 'Works without signal', 'Workouts, measurements and photos save on the phone first and sync when you are back online.'),
    ('ph-arrow-counter-clockwise', 'Nothing lost mid workout', 'The workout in progress is saved as you go and restored if the app is closed.'),
    ('ph-moon', 'Light and dark', 'Follow the phone or pick a theme. Contrast is checked on every screen.'),
    ('ph-scales', 'Metric or imperial', 'Kilograms or pounds, centimetres or inches, everywhere in the app.'),
]

FAQ = [
    ('Do I need to create an account?', 'No. Each phone gets its own account automatically, so you can start training straight after the four setup steps. There is no login screen.'),
    ('Does it work in a gym with no signal?', 'Yes. Workouts, measurements and photos are saved on the phone first and sent to the server with retries once you are back online.'),
    ('What happens if the app closes during a workout?', 'The workout in progress is saved continuously. Open the app again and it picks up where you left off, with every logged set in place.'),
    ('Do I need a full gym?', 'No. There are programs and routines for dumbbells only, bodyweight, resistance bands, suspension trainers and travel, as well as full gym setups.'),
    ('How is the muscle map percentage worked out?', 'Each muscle compares the training it got with ideal training over the same period. 100% means five hard sets, three times a week.'),
    ('Can I follow a program and still change a day?', 'Yes. You follow one program at a time, and swapping today’s workout overrides that single day without changing the program.'),
    ('Can I add a workout I forgot to log?', 'Yes. Tap the day in the Pivot calendar and choose Log workout to fill it in.'),
    ('Kilograms or pounds?', 'Either. Metric and imperial units work across the whole app.'),
]

def form(fid):
    return f'''
      <form class="signup" novalidate data-signup>
        <label class="sr-only" for="{fid}">Email address</label>
        <input id="{fid}" class="body-3" type="email" name="email" placeholder="you@example.com" autocomplete="email" required aria-describedby="{fid}-msg">
        <button class="btn btn-primary button-md" type="submit"><span>Get early access</span><i class="ph ph-arrow-right" aria-hidden="true"></i></button>
        <p id="{fid}-msg" class="caption-2 form-msg" role="status" aria-live="polite"></p>
      </form>'''

chapters_html = ''
for ch in CHAPTERS:
    rows = ''.join(row(i, f'{ch["tab"]} · {ch["num"]}', *r) for i, r in enumerate(ch['rows']))
    minis = ''  # small cards are gathered into one gallery after the chapters
    chapters_html += f'''
  <section class="chapter" id="{ch['id']}" aria-labelledby="{ch['id']}-title">
    <header class="chapter-head">
      <div class="rule" aria-hidden="true"><span class="half l"></span><span class="badge"><i class="ph {ch['icon']}"></i></span><span class="half r"></span></div>
      <p class="caption-3 eyebrow">{ch['num']} · {ch['tab']}</p>
      <h2 id="{ch['id']}-title" class="heading-2">{ch['title']}</h2>
      <p class="body-3 muted lead">{ch['lead']}</p>
    </header>
    {rows}
    {minis}
  </section>'''

ALL_MINIS = [m for ch in CHAPTERS for m in ch['minis']]
more_html = f'<div class="minis" data-count="{len(ALL_MINIS)}">' + ''.join(mini(i, *m) for i, m in enumerate(ALL_MINIS)) + '</div>'

also_html = ''.join(f'''
      <article class="tile" data-from="{'left' if i % 2 == 0 else 'right'}" style="--i:{i}">
        <span class="tile-icon"><i class="ph {ic}" aria-hidden="true"></i></span>
        <h3 class="title-2">{t}</h3>
        <p class="body-6 muted">{b}</p>
      </article>''' for i, (ic, t, b) in enumerate(ALSO))

faq_html = ''.join(f'''
      <details class="qa"><summary class="title-2"><span>{q}</span><i class="ph ph-plus" aria-hidden="true"></i></summary><p class="body-3 muted">{a}</p></details>''' for q, a in FAQ)

faq_schema = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ','.join(
    '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (__import__('json').dumps(q), __import__('json').dumps(a)) for q, a in FAQ) + ']}'

import json as _json
_manifest = _json.loads((OUT.parent / 'media' / 'manifest.json').read_text())
# Dark takes that do not show what the copy describes stay on the light clip in dark mode:
# swap exercise (black-demo-no-icon.mp4 never completes a swap; the old dark take is partial and has the gear icon).
DARK_SKIP = {'blueprint-swap-exercise'}
DARK_CLIPS = sorted(c['file'][:-4] for c in _manifest['clips']
                    if c.get('dark') and c['file'][:-4] not in DARK_SKIP
                    and (OUT.parent / 'media' / (c['file'][:-4] + '-dark.mp4')).exists())

TAGLINE = 'Every set you log lands on a muscle you can see. Every week shows you where to aim next.'
tag_words = ' '.join(f'<span class="w">{w}</span>' for w in TAGLINE.split())

html = (Path(__file__).with_name('landing_template.html').read_text()
        .replace('%%CHAPTERS%%', chapters_html)
        .replace('%%ALSO%%', also_html)
        .replace('%%MORE%%', more_html)
        .replace('%%FAQ%%', faq_html)
        .replace('%%FAQ_SCHEMA%%', faq_schema)
        .replace('%%TAGLINE%%', tag_words)
        .replace('%%DARK_CLIPS%%', _json.dumps(DARK_CLIPS))
        .replace('%%LIGHT_V%%', LIGHT_V)
        .replace('%%FORM_TOP%%', form('email-top'))
        .replace('%%FORM_BOTTOM%%', form('email-bottom'))
        .replace('%%HERO_LEFT%%', video('physique-3d', '3D muscle map rotating', 'phone phone-side side-l'))
        .replace('%%HERO_CENTER%%', video('blueprint-today', 'Today’s planned session', 'phone phone-main'))
        .replace('%%HERO_RIGHT%%', video('pivot-calendar-month', 'Training calendar with streaks', 'phone phone-side side-r')))
OUT.write_text(html)
print('wrote', OUT, len(html), 'bytes;', len(DARK_CLIPS), 'dark clips wired')
