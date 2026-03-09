from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Wafaa Is My Love</title>
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 60px;
        }
        h1 {
            font-size: 60px;
            color: white;
            text-shadow: 2px 2px 5px #00000055;
            margin-bottom: 10px;
        }
        h2 {
            font-size: 40px;
            color: white;
            text-shadow: 2px 2px 5px #00000055;
            margin-top: 0;
        }
        button {
            padding: 20px 40px;
            margin: 20px;
            font-size: 24px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: 0.2s;
        }
        .yes {
            background-color: #4CAF50;
            color: white;
        }
        .yes:hover {
            background-color: #45a049;
        }
        .no {
            background-color: #f44336;
            color: white;
        }
        .no:hover {
            background-color: #da190b;
        }
        #message {
            margin-top: 30px;
        }
    </style>
</head>
<body>

<h1>WAFAA ❤️</h1>
<h2>I Love You!</h2>

<button class="yes" onclick="love()">I love you too</button>
<button class="no" onclick="error()">I don't love you</button>

<div id="message"></div>

<script>
function love() {
    document.getElementById("message").innerHTML = `
        <h2 style='color:white;'>YAY!!! 🎉❤️</h2>
        <img src='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif' width='300'>
        <audio autoplay>
            <source src='https://www.myinstants.com/media/sounds/tada-fanfare.mp3'>
        </audio>
    `;
}

function error() {
    document.getElementById("message").innerHTML = `
        <h2 style='color:white;'>❌ ERROR ❌</h2>
        <h3 style='color:white;'>Wrong answer. You HAVE to pick "I love you too" 😌</h3>
        <img src='https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif' width='300'>
    `;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE
