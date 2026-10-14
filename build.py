#!/usr/bin/env python3
"""Builds the Dominion Restored website: every page shares one header and footer.

Edit the page bodies below, then run `python3 build.py` from this folder. It writes index.html, faq.html,
support.html, about.html and privacy.html next to it. No packages needed."""
import pathlib

HERE = pathlib.Path(__file__).parent
SITE = 'Dominion Restored'
COMPANY = 'Kingdom Management Solutions, LLC'
EMAIL = 'kingdommanagementsolutions@gmail.com'
NAV = [('index.html', 'Home'), ('faq.html', 'FAQ'), ('support.html', 'Support'), ('about.html', 'About'), ('privacy.html', 'Privacy')]


def page(file, title, description, body):
    cur = ' aria-current="page"'
    nav = '\n'.join(f'        <li><a href="{href}"{cur if href == file else ""}>{label}</a></li>' for href, label in NAV)
    full_title = SITE if file == 'index.html' else f'{title} | {SITE}'
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#0b0b14">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/title.webp">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/silkscreen-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/icon.svg" alt="" width="32" height="32">DOMINION RESTORED</a>
    <nav aria-label="Main">
      <ul>
{nav}
      </ul>
    </nav>
  </div>
</header>
<main id="main">
{body.strip()}
</main>
<footer>
  <div class="wrap">
    <div>&copy; {COMPANY}. All rights reserved.<br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <ul>
{''.join(f'      <li><a href="{h}">{l}</a></li>{chr(10)}' for h, l in NAV)}    </ul>
  </div>
</footer>
</body>
</html>
'''
    (HERE / file).write_text(html)


# ---------------------------------------------------------------- home
LANDS = [
    ('Garden of Eden', 'Genesis 3', 'The Serpent'),
    ('The Ark', 'Genesis 6-8', 'Leviathan'),
    ('Tower of Babel', 'Genesis 11', 'Nimrod the Hunter'),
    ("Pharaoh's Pyramid", 'Exodus 7-14', 'Pharaoh'),
    ('Walls of Jericho', 'Joshua 6', 'The Colossus of Jericho'),
    ('Valley of Elah', '1 Samuel 17', 'Goliath of Gath'),
    ('Furnace of Babylon', 'Daniel 2-3', 'The Great Image'),
    ('The Temptation', 'Matthew 4', 'The Tempter'),
    ('The Empty Tomb', 'Matthew 28', 'Death'),
    ('The Abyss', 'Revelation 12', 'The Dragon'),
]
MINIS = ['Fleeing the Garden', "Noah's Ark", "Job's Servants", 'The Ten Plagues', 'March on Jericho', 'Shepherd David',
         'Daniel in Babylon', 'Prepare the Way', 'Healing at Sundown', "Paul's Journeys", 'Mountain-Moving Faith',
         'The Fishing Hole', 'The Shooting Range', 'The Puzzle Cube']
SHOTS = [
    ('eden', 'The Garden of Eden'), ('boss-serpent', 'The Serpent'), ('overworld-battle', 'Battles in every land'),
    ('dungeon', 'Ten dungeons'), ('boss-goliath', 'Goliath of Gath'), ('boss-dragon', 'The Dragon'),
    ('mini-ark', "Noah's Ark"), ('mini-plagues', 'The Ten Plagues'), ('mini-jericho', 'March on Jericho'),
    ('mini-paul', "Paul's Journeys"), ('mini-fishing', 'The Fishing Hole'), ('mini-cube', 'The Puzzle Cube'),
    ('throne-room', 'The throne room'), ('new-earth', 'The new earth'), ('new-earth-praise', 'Praise with the saints'),
]
STORES = [('App Store', 'iPhone and iPad'), ('Mac App Store', 'Mac'), ('Google Play', 'Android phones and tablets'), ('Microsoft Store', 'Windows PCs')]

lands = '\n'.join(f'        <li><span class="n">{i + 1}</span><div><b>{n}</b><span>{ref} &middot; {boss}</span></div></li>' for i, (n, ref, boss) in enumerate(LANDS))
minis = '\n'.join(f'        <li>{m}</li>' for m in MINIS)
shots = '\n'.join(f'''        <figure><img src="assets/img/{f}.webp" alt="{c}" width="768" height="672" loading="lazy"><figcaption>{c}</figcaption></figure>''' for f, c in SHOTS)
# When a store link is live, replace that store's <span class="soon"> with <a class="btn" href="...">GET IT</a>
# and the QR placeholder's text with <img src="assets/img/qr-<store>.png" alt="QR code for the <store>">.
stores = '\n'.join(f'''        <div class="store"><h3>{s}</h3><p>{d}</p><span class="soon">COMING SOON</span><div class="qr" aria-hidden="true">QR CODE<br>COMING SOON</div></div>''' for s, d in STORES)

page('index.html', 'Home', 'An 8-bit Bible adventure from Eden to Revelation: ten dungeons, ten bosses, fourteen mini-games and the new earth. For iPhone, iPad, Mac, Android and Windows.', f'''
<section class="hero">
  <div class="wrap">
    <div>
      <p class="kicker">An 8-bit Bible adventure</p>
      <h1>DOMINION RESTORED</h1>
      <p class="lede">Journey through the whole story of Scripture, from the Garden of Eden to the book of Revelation, in a classic action adventure made for the whole family.</p>
      <div class="btns">
        <a class="btn" href="#get">GET THE GAME</a>
        <a class="btn ghost" href="#gallery">SEE IT IN ACTION</a>
      </div>
    </div>
    <div class="frame"><img src="assets/img/title.webp" alt="The Dominion Restored title screen" width="768" height="672"></div>
  </div>
</section>

<section class="alt" id="story">
  <div class="wrap">
    <div class="head">
      <p class="kicker">The story</p>
      <h2>From Eden to Revelation</h2>
      <p class="dim">Dominion was given in the garden and lost at the fall. Win it back across ten lands of the Bible, each with its own dungeon, its own treasure and its own guardian to overcome.</p>
    </div>
    <ol class="lands">
{lands}
    </ol>
  </div>
</section>

<section id="features">
  <div class="wrap">
    <div class="head">
      <p class="kicker">What's inside</p>
      <h2>A big adventure in a small package</h2>
    </div>
    <div class="grid g3">
      <div class="card"><div class="ico">10</div><h3>Dungeons and bosses</h3><p>Locked doors, keys, treasure rooms and a boss in every land, each fought the way the story tells it.</p></div>
      <div class="card"><div class="ico">14</div><h3>Mini-games</h3><p>Circus tents across the world hold a game from each story, open from the start. Replay them any time from the Arcade.</p></div>
      <div class="card"><div class="ico">KJV</div><h3>Scripture throughout</h3><p>Signs, treasures and battles carry verses from the King James Bible, so the story is told in its own words.</p></div>
      <div class="card"><div class="ico">2D/3D</div><h3>Two ways to see it</h3><p>Play in classic 8-bit 2D, or switch to a 3D diorama of the same pixel art at any time.</p></div>
      <div class="card"><div class="ico">+</div><h3>Weapons of the faith</h3><p>The Flaming Sword, the Dove, the Rod of Moses, the Shofar, David's sling, the Shield of Faith, the Armor of Light and more.</p></div>
      <div class="card"><div class="ico">&#9733;</div><h3>The new earth</h3><p>Beyond the final battle lies a world made new, full of saints, angels and friendly animals. We'll let you discover it.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="minigames">
  <div class="wrap">
    <div class="head">
      <p class="kicker">Step right up</p>
      <h2>Fourteen mini-games</h2>
      <p class="dim">Flee the garden, fill Noah's ark two by two, march around Jericho to the beat, sail with Paul through the storm, cast your net on the right side of the boat, or solve a puzzle cube, with a step-by-step solver to learn from.</p>
    </div>
    <ul class="chips">
{minis}
    </ul>
  </div>
</section>

<section id="gallery">
  <div class="wrap">
    <div class="head">
      <p class="kicker">Gallery</p>
      <h2>See it in action</h2>
    </div>
    <div class="gallery">
{shots}
    </div>
  </div>
</section>

<section class="alt" id="family">
  <div class="wrap">
    <div class="head">
      <p class="kicker">For the whole family</p>
      <h2>Just the game</h2>
    </div>
    <ul class="ticks">
      <li><b>No ads</b><span>Nothing interrupts the story.</span></li>
      <li><b>No in-app purchases</b><span>Buy it once and everything is yours.</span></li>
      <li><b>No data collected</b><span>No accounts, no tracking. <a href="privacy.html">Privacy policy</a></span></li>
      <li><b>Plays offline</b><span>No internet connection needed.</span></li>
    </ul>
  </div>
</section>

<section id="get">
  <div class="wrap">
    <div class="head">
      <p class="kicker">Get the game</p>
      <h2>Coming soon to your device</h2>
      <p class="dim">Dominion Restored is on its way to iPhone, iPad, Mac, Android and Windows. Links and QR codes will appear here as each store goes live.</p>
    </div>
    <div class="stores">
{stores}
    </div>
  </div>
</section>
''')

# ---------------------------------------------------------------- FAQ
def qa(q, a):
    return f'''  <details>
    <summary>{q}</summary>
    <div>{a.strip()}</div>
  </details>'''

FAQ = [
    ('About the game', [
        ('What is Dominion Restored?', '<p>An 8-bit action adventure that travels through the story of the Bible, from the Garden of Eden to the book of Revelation. You explore ten lands, each with a dungeon, a treasure and a boss, plus fourteen mini-games in circus tents along the way.</p>'),
        ('Which devices can I play on?', '<p>iPhone, iPad, Mac, Android phones and tablets, and Windows PCs. See <a href="index.html#get">Get the game</a> for the stores.</p>'),
        ('Are there ads, in-app purchases or subscriptions?', '<p>No. You buy the game once and everything in it is yours. There are no ads, no in-app purchases and no subscriptions.</p>'),
        ('Is it suitable for children?', '<p>It is made for families. The combat is classic 8-bit action against creatures and Bible-story foes, with no gore. Enemies simply vanish when defeated. Check the age rating shown on your store for the official rating, and as always, parents know their children best.</p>'),
        ('Which Bible translation does the game quote?', '<p>The King James Version.</p>'),
        ('Does it need an internet connection?', '<p>No. Once installed, it plays completely offline.</p>'),
        ('Is there anything after the final battle?', '<p>Yes. We will let you discover it.</p>'),
    ]),
    ('Playing', [
        ('How do I control the game?', '''<p>On a phone or tablet, use the on-screen stick to move, <b>A</b> to use your sword, <b>B</b> to use your item, <b>ITEM</b> to switch items and <b>START</b> to pause. On a Mac or PC you can use the keyboard:</p>
<table>
  <tr><th>Action</th><th>Keys</th></tr>
  <tr><td>Move</td><td><kbd>&larr;</kbd> <kbd>&uarr;</kbd> <kbd>&rarr;</kbd> <kbd>&darr;</kbd> or <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd></td></tr>
  <tr><td>Sword (A)</td><td><kbd>Z</kbd>, <kbd>J</kbd> or <kbd>Space</kbd></td></tr>
  <tr><td>Item (B)</td><td><kbd>X</kbd> or <kbd>K</kbd></td></tr>
  <tr><td>Switch item</td><td><kbd>C</kbd> or <kbd>Q</kbd></td></tr>
  <tr><td>Pause</td><td><kbd>Enter</kbd>, <kbd>P</kbd> or <kbd>Esc</kbd></td></tr>
  <tr><td>Sound on and off</td><td><kbd>M</kbd></td></tr>
</table>'''),
        ('How do I save?', '<p>The game saves automatically as you go: when you move to a new screen, find a treasure or defeat a boss. Choose CONTINUE on the title screen to pick up where you left off.</p>'),
        ('Can I switch between 2D and 3D?', '<p>Yes. Open OPTIONS on the title screen or in the pause menu and change VIEW. In 3D, CAMERA lets you follow the hero up close or see the whole room. The game plays the same either way.</p>'),
        ('Can I change how my hero looks?', '<p>Yes. OPTIONS has four looks to choose from, and the game remembers your choice.</p>'),
        ('What are the circus tents?', '<p>Each land has a circus tent with a mini-game from its story, and a few extra tents hold bonus games. They are open from the start, before or after you beat that land\'s dungeon. Once you have found a tent, you can replay its game from ARCADE on the title screen without touching your saved game.</p>'),
        ("I'm stuck. Any hints?", '''<ul>
  <li>Read the signs. They often point the way.</li>
  <li>Each dungeon has a locked treasure room guarded by a mini-boss. Its treasure also opens the boss door.</li>
  <li>Small keys open locked doors. Clear a room of enemies to find them.</li>
  <li>Some bosses can only be hurt in a particular way. Think about how the Bible story goes.</li>
  <li>Your Faith meter (the blue bar) powers your items and refills over time.</li>
</ul>'''),
    ]),
    ('Your saved game', [
        ('Can I move my save to another device?', '<p>Not at this time. Your progress is stored only on the device you play on, which is part of how the game keeps your information private.</p>'),
        ('What happens to my save if I delete the app?', '<p>Deleting the app deletes your saved game with it, and it cannot be recovered, so keep the app installed if you want to keep your progress.</p>'),
    ]),
    ('Help', [
        ('I found a bug. How do I report it?', '<p>Thank you! Please email us. The <a href="support.html">support page</a> lists what to include so we can fix it quickly.</p>'),
        ('How do I get a refund?', '<p>Purchases are handled by the store you bought from, so refunds are requested through that store. The <a href="support.html#refunds">support page</a> has the links.</p>'),
    ]),
]
faq = '\n'.join(f'  <h2>{sec}</h2>\n' + '\n'.join(qa(q, a) for q, a in items) for sec, items in FAQ)
page('faq.html', 'FAQ', 'Answers to common questions about Dominion Restored: devices, controls, saving, mini-games and more.', f'''
<div class="page">
<div class="wrap">
  <p class="kicker">Help</p>
  <h1>Frequently asked questions</h1>
  <p class="lede">Can't find your answer here? <a href="support.html">Contact support</a>.</p>
{faq}
</div>
</div>
''')

# ---------------------------------------------------------------- support
page('support.html', 'Support', 'Get help with Dominion Restored: contact support, report a bug, or request a refund.', f'''
<div class="page">
<div class="wrap">
  <p class="kicker">Help</p>
  <h1>Support</h1>
  <p class="lede">We're glad to help. Many questions are answered in the <a href="faq.html">FAQ</a>. For anything else, write to us.</p>

  <div class="contact">
    <div><b>Email support</b><span class="dim">We read every message.</span></div>
    <a class="btn" href="mailto:{EMAIL}?subject=Dominion%20Restored%20support">{EMAIL}</a>
  </div>

  <h2>Reporting a problem</h2>
  <p>To help us track it down quickly, please include:</p>
  <ul>
    <li>your device (for example, iPhone 15 or Samsung Galaxy S24) and its system version</li>
    <li>where you were in the game: the land, the dungeon or the mini-game</li>
    <li>what happened, and what you expected to happen</li>
    <li>a screenshot or a short screen recording, if you can</li>
  </ul>

  <h2 id="refunds">Refunds</h2>
  <p>Purchases are made through the app stores, so refunds are requested from the store you bought the game from:</p>
  <ul>
    <li><b>App Store</b> (iPhone, iPad and Mac): <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a></li>
    <li><b>Google Play</b>: <a href="https://support.google.com/googleplay/answer/2479637" rel="noopener">Google Play refund help</a></li>
    <li><b>Microsoft Store</b>: request it from your <a href="https://account.microsoft.com/billing/orders" rel="noopener">Microsoft account order history</a></li>
  </ul>

  <h2>Privacy</h2>
  <p>Dominion Restored collects no personal information. Read the <a href="privacy.html">privacy policy</a>.</p>
</div>
</div>
''')

# ---------------------------------------------------------------- about
page('about.html', 'About', f'About {COMPANY}, the publisher of Dominion Restored.', f'''
<div class="page">
<div class="wrap">
  <p class="kicker">About us</p>
  <h1>{COMPANY}</h1>
  <p class="lede">{COMPANY} is the independent publisher of Dominion Restored.</p>

  <h2>Why Dominion Restored</h2>
  <p>In the beginning, God gave mankind dominion over the earth. It was lost in the garden, and the rest of Scripture tells how it is won back. Dominion Restored follows that story from Genesis to Revelation, through the lands, battles and promises of the Bible, and ends where the Bible ends: with all things made new.</p>
  <blockquote class="verse">"And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth."<cite>GENESIS 1:28</cite></blockquote>
  <blockquote class="verse">"And hast made us unto our God kings and priests: and we shall reign on the earth."<cite>REVELATION 5:10</cite></blockquote>

  <h2>What we believe a game should be</h2>
  <ul>
    <li><b>Something to share.</b> Made so parents, children and grandparents can all enjoy it together.</li>
    <li><b>Honest.</b> One purchase, no ads, no in-app purchases, and no data collected.</li>
    <li><b>True to the story.</b> Scripture quoted in its own words, from the King James Version.</li>
  </ul>

  <h2>Contact</h2>
  <p>For support, press or business enquiries, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
</div>
''')

# ---------------------------------------------------------------- privacy
page('privacy.html', 'Privacy Policy', 'The Dominion Restored privacy policy: the game collects no personal information.', f'''
<div class="page">
<div class="wrap">
  <p class="kicker">Legal</p>
  <h1>Privacy policy</h1>
  <p class="updated">EFFECTIVE OCTOBER 14, 2026</p>

  <div class="summary"><p><strong>In short:</strong> Dominion Restored does not collect, store, share or sell any personal information. It has no accounts, no ads, no analytics and no tracking, and it never sends anything over the internet. Your progress is saved only on your own device.</p></div>

  <h2>Who we are</h2>
  <p>Dominion Restored is published by {COMPANY} ("we", "us"). This policy covers the Dominion Restored apps for iPhone, iPad, Mac, Android and Windows, and this website.</p>

  <h2>What the game collects</h2>
  <p>Nothing. The game does not ask for your name, email address, location, contacts, photos or any other personal information, and it does not use your camera or microphone. It contains no advertising, analytics, crash-reporting or tracking tools, and no third-party code that collects data. It makes no network requests while you play.</p>

  <h2>What stays on your device</h2>
  <p>So that you can pick up where you left off, the game stores a few things on your device:</p>
  <ul>
    <li>your saved game (progress, items and hearts)</li>
    <li>the look you chose for your hero</li>
    <li>which mini-game tents you have found, for the Arcade</li>
    <li>your best score at the shooting range</li>
  </ul>
  <p>This information never leaves your device, and we cannot see it. You can erase all of it at any time by deleting the app.</p>

  <h2>This website</h2>
  <p>This website uses no cookies, analytics or advertising, and loads nothing from other companies. It is hosted by GitHub Pages; like most web hosts, GitHub may record technical information such as IP addresses to keep its service secure. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub General Privacy Statement</a>.</p>

  <h2>Sharing</h2>
  <p>Because we collect nothing, we have nothing to share or sell, and we share nothing with anyone.</p>

  <h2>Children</h2>
  <p>Dominion Restored is made for families. We do not knowingly collect personal information from anyone, including children under 13, and the game has no chat, no accounts and no way to contact other players.</p>

  <h2>App stores</h2>
  <p>You download the app through Apple's App Store, Google Play or the Microsoft Store. Those stores may collect information about your purchase and download under their own privacy policies, which we do not control.</p>

  <h2>Changes to this policy</h2>
  <p>If the game ever changes in a way that affects your privacy, we will update this page and its effective date before that change is released.</p>

  <h2>Contact us</h2>
  <p>Questions about this policy can be sent to {COMPANY} at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
</div>
''')

print('built', ', '.join(f for f, _ in NAV))
