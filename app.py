from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Wafaa ❤️</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: 'Poppins', sans-serif;
            background: radial-gradient(circle at top, #ff9a9e, #fad0c4);
            transition: background 2s ease;
        }

        .heart {
            position: absolute;
            color: #ff4d6d;
            font-size: 24px;
            animation: floatUp 6s linear infinite;
            opacity: 0.8;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-800px) scale(1.8); opacity: 0; }
        }

        .shooting-star {
            position: absolute;
            width: 3px;
            height: 80px;
            background: white;
            transform: rotate(45deg);
            animation: shoot 2s ease-out forwards;
        }

        @keyframes shoot {
            0% { opacity: 1; transform: translate(-200px, -200px) rotate(45deg); }
            100% { opacity: 0; transform: translate(800px, 800px) rotate(45deg); }
        }

        h1 {
            text-align: center;
            margin-top: 80px;
            font-size: 60px;
            color: white;
            text-shadow: 0 0 20px #ff4d6d;
        }

        h2 {
            text-align: center;
            font-size: 32px;
            color: white;
            margin-top: -10px;
        }

        .buttons {
            text-align: center;
            margin-top: 40px;
        }

        button {
            padding: 18px 40px;
            font-size: 24px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            margin: 20px;
            transition: 0.3s;
        }

        .yes {
            background: #4CAF50;
            color: white;
            box-shadow: 0 0 15px #4CAF50;
        }

        .yes:hover {
            transform: scale(1.2);
        }

        .no {
            background: #f44336;
            color: white;
            position: absolute;
        }

        #message {
            text-align: center;
            margin-top: 40px;
            color: white;
            font-size: 28px;
            opacity: 0;
            transition: opacity 1s ease;
        }

        .typewriter {
            display: inline-block;
            border-right: 3px solid white;
            white-space: nowrap;
            overflow: hidden;
            animation: typing 3s steps(40), blink 0.7s infinite;
            font-size: 32px;
        }

        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }

        @keyframes blink {
            50% { border-color: transparent; }
        }
    </style>
</head>
<body>

<h1>WAFAA ❤️</h1>
<h2>You mean the world to me</h2>

<div class="buttons">
    <button class="yes" onclick="love()">I love you too</button>
    <button class="no" id="noBtn" onmouseover="runAway()">I don't love you</button>
</div>

<div id="message"></div>

<script>
setInterval(() => {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * window.innerWidth + "px";
    heart.style.top = window.innerHeight + "px";
    heart.style.fontSize = (20 + Math.random() * 30) + "px";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 6000);
}, 500);

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
    btn.style.left = Math.random() * (window.innerWidth - 200) + "px";
    btn.style.top = Math.random() * (window.innerHeight - 200) + "px";
}

function confetti() {
    for (let i = 0; i < 80; i++) {
        let conf = document.createElement("div");
        conf.style.position = "absolute";
        conf.style.width = "10px";
        conf.style.height = "10px";
        conf.style.background = "#" + Math.floor(Math.random()*16777215).toString(16);
        conf.style.left = Math.random() * window.innerWidth + "px";
        conf.style.top = "-20px";
        conf.style.opacity = 0.9;
        conf.style.transform = "rotate(" + Math.random()*360 + "deg)";
        conf.style.animation = "fall 2s linear forwards";
        document.body.appendChild(conf);
        setTimeout(() => conf.remove(), 2000);
    }
}

function love() {
    confetti();
    document.body.style.background = "linear-gradient(135deg, #ff758c, #ff7eb3)";
    document.getElementById("message").innerHTML = `
        <div class='typewriter'>Wafaa… you just made my whole world brighter ❤️</div>
        <br><br>
        <img src='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif' width='280'>
    `;
    document.getElementById("message").style.opacity = 1;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE
