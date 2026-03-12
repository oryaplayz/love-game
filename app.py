from flask import Flask

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Wafaa ❤️</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: 'Poppins', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            background: radial-gradient(circle at top, #ff9a9e, #fad0c4);
            transition: background 2s ease;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            text-align: center;
            color: white;
            padding: 20px;
            max-width: 480px;
        }
        h1 {
            font-size: 42px;
            margin-bottom: 10px;
            text-shadow: 0 0 20px #ff4d6d;
        }
        h2 {
            font-size: 22px;
            margin-top: 0;
            margin-bottom: 25px;
        }
        .buttons {
            margin-top: 10px;
            position: relative;
            height: 120px;
        }
        button {
            padding: 14px 26px;
            font-size: 18px;
            border: none;
            border-radius: 999px;
            cursor: pointer;
            margin: 10px;
            transition: 0.25s;
        }
        .yes {
            background: #4CAF50;
            color: white;
            box-shadow: 0 0 15px #4CAF50;
        }
        .yes:hover {
            transform: scale(1.1);
        }
        .no {
            background: #f44336;
            color: white;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
        }
        #message {
            margin-top: 25px;
            font-size: 18px;
            opacity: 0;
            transition: opacity 1s ease;
        }
        .typewriter {
            display: inline-block;
            border-right: 3px solid white;
            white-space: nowrap;
            overflow: hidden;
            animation: typing 3s steps(40), blink 0.7s infinite;
            font-size: 20px;
        }
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        @keyframes blink {
            50% { border-color: transparent; }
        }
        .heart {
            position: fixed;
            color: #ff4d6d;
            font-size: 20px;
            animation: floatUp 6s linear infinite;
            opacity: 0.8;
            pointer-events: none;
        }
        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-800px) scale(1.8); opacity: 0; }
        }
        .shooting-star {
            position: fixed;
            width: 3px;
            height: 80px;
            background: white;
            transform: rotate(45deg);
            animation: shoot 2s ease-out forwards;
            pointer-events: none;
        }
        @keyframes shoot {
            0% { opacity: 1; transform: translate(-200px, -200px) rotate(45deg); }
            100% { opacity: 0; transform: translate(800px, 800px) rotate(45deg); }
        }
        .letter-btn {
            margin-top: 20px;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 999px;
            border: none;
            background: #ff4d6d;
            color: white;
            cursor: pointer;
            box-shadow: 0 0 15px #ff4d6d;
            display: none;
        }
        .letter-btn:hover {
            transform: scale(1.05);
        }
        .secret {
            margin-top: 15px;
            font-size: 16px;
            opacity: 0;
            transition: opacity 0.8s ease;
        }
        .secret-btn {
            margin-top: 10px;
            padding: 8px 18px;
            font-size: 14px;
            border-radius: 999px;
            border: 1px solid white;
            background: transparent;
            color: white;
            cursor: pointer;
        }
        .music-note {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 12px;
            opacity: 0.7;
        }
        @media (max-width: 480px) {
            h1 { font-size: 34px; }
            h2 { font-size: 18px; }
            button { font-size: 16px; padding: 12px 20px; }
            .container { max-width: 360px; }
        }
    </style>
</head>
<body>

<div class="container">
    <h1>WAFAA ❤️</h1>
    <h2>I LOVE YOU</h2>

    <div class="buttons">
        <button class="yes" onclick="love()">I love you too</button>
        <button class="no" id="noBtn" onmouseover="runAway()">I don't love you</button>
    </div>

    <div id="message"></div>

    <button class="letter-btn" id="letterBtn" onclick="goToLetter()">Open my letter to you 💌</button>

    <div class="secret" id="secretText">
        <strong>Secret:</strong> I was nervous making this… but you were worth every second. 💖
    </div>
    <button class="secret-btn" id="secretBtn" onclick="revealSecret()">Tap for a secret</button>
</div>

<!-- Background music (Love Story – Indila via YouTube embed) -->
<div style="position: fixed; top: 10px; left: 10px; width: 0; height: 0; overflow: hidden;">
    <iframe width="0" height="0"
        src="https://www.youtube.com/embed/SX_ViT4Ra7k?autoplay=1&loop=1&playlist=SX_ViT4Ra7k"
        title="Love Story - Indila"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
</div>

<div class="music-note">🎵 Love Story – Indila</div>

<script>
setInterval(() => {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * window.innerWidth + "px";
    heart.style.bottom = "-40px";
    heart.style.fontSize = (18 + Math.random() * 24) + "px";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 6000);
}, 600);

function shootingStar() {
    let star = document.createElement("div");
    star.className = "shooting-star";
    star.style.top = Math.random() * 200 + "px";
    star.style.left = Math.random() * 200 + "px";
    document.body.appendChild(star);
    setTimeout(() => star.remove(), 2000);
}
setInterval(shootingStar, 5000);

function runAway() {
    let btn = document.getElementById("noBtn");
    let x = Math.random() * (window.innerWidth - 160);
    let y = Math.random() * (window.innerHeight - 220) + 80;
    btn.style.left = x + "px";
    btn.style.top = y + "px";
}

function confetti() {
    for (let i = 0; i < 70; i++) {
        let conf = document.createElement("div");
        conf.style.position = "fixed";
        conf.style.width = "8px";
        conf.style.height = "14px";
        conf.style.background = "#" + Math.floor(Math.random()*16777215).toString(16);
        conf.style.left = Math.random() * window.innerWidth + "px";
        conf.style.top = "-20px";
        conf.style.opacity = 0.9;
        conf.style.transform = "rotate(" + Math.random()*360 + "deg)";
        conf.style.transition = "transform 2s linear, top 2s linear, opacity 2s linear";
        document.body.appendChild(conf);
        setTimeout(() => {
            conf.style.top = window.innerHeight + "px";
            conf.style.transform += " translateY(20px)";
            conf.style.opacity = 0;
        }, 10);
        setTimeout(() => conf.remove(), 2100);
    }
}

function love() {
    confetti();
    document.body.style.background = "linear-gradient(135deg, #ff758c, #ff7eb3)";
    document.getElementById("message").innerHTML = `
        <div class='typewriter'>Wafaa… you just made my whole world brighter ❤️</div>
        <br><br>
        <img src='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif' width='220' style='border-radius: 16px; box-shadow: 0 0 20px #ffffff55;'>
    `;
    document.getElementById("message").style.opacity = 1;
    document.getElementById("letterBtn").style.display = "inline-block";
}

function goToLetter() {
    window.location.href = "/letter";
}

function revealSecret() {
    document.getElementById("secretText").style.opacity = 1;
    document.getElementById("secretBtn").style.display = "none";
}
</script>

</body>
</html>
"""

LETTER_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>For Wafaa 💌</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Poppins', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            background: radial-gradient(circle at top, #2b1055, #7597de);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .card {
            max-width: 520px;
            padding: 24px 20px 28px;
            background: rgba(0, 0, 0, 0.35);
            border-radius: 18px;
            box-shadow: 0 0 30px #00000088;
            text-align: left;
        }
        h1 {
            text-align: center;
            margin-top: 0;
            margin-bottom: 10px;
            font-size: 30px;
        }
        p {
            line-height: 1.6;
            font-size: 16px;
        }
        .back-btn {
            margin-top: 18px;
            display: inline-block;
            padding: 10px 20px;
            border-radius: 999px;
            border: none;
            background: #ff4d6d;
            color: white;
            cursor: pointer;
            font-size: 14px;
        }
        .secret-final {
            margin-top: 14px;
            font-size: 15px;
            opacity: 0.9;
        }
        @media (max-width: 480px) {
            .card { margin: 0 14px; }
            h1 { font-size: 24px; }
            p { font-size: 15px; }
        }
    </style>
</head>
<body>

<div class="card">
    <h1>For you, Wafaa 💌</h1>
    <p>
        I didn’t just make a page… I made a little world where it’s just you and me.
        Every color, every heart, every tiny detail here is because you matter to me
        more than I can explain in one sentence.
    </p>
    <p>
        If you’re reading this, it already means so much. It means you cared enough
        to click, to see what I made, to step into this small universe I built for you.
    </p>
    <p>
        I love you — not just in a cute way, but in a real way. In the
        “you’re on my mind when I wake up and before I sleep” kind of way.
        In the “I want to see you happy, always” kind of way.
    </p>
    <p>
        This isn’t perfect, and neither am I. But my feelings for you are real,
        and this page is just one tiny way of showing it. ❤️
    </p>

    <div class="secret-final">
        Secret message:  
        <strong>You’re my favorite part of every day. Even the bad ones feel lighter when I think of you.</strong>
    </div>

    <button class="back-btn" onclick="goBack()">⬅ Back to the main page</button>
</div>

<script>
function goBack() {
    window.location.href = "/";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HOME_PAGE

@app.route("/letter")
def letter():
    return LETTER_PAGE
