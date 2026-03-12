from flask import Flask, render_template_string

app = Flask(__name__)

LOVE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Love Game</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin-top: 80px;
    }

    h1 {
        margin-bottom: 40px;
    }

    .btn-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }

    button {
        padding: 12px 25px;
        font-size: 18px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.2s;
    }

    #yesBtn {
        background-color: #ff4d6d;
        color: white;
    }

    #noBtn {
        background-color: #444;
        color: white;
        position: absolute;
    }
</style>
</head>
<body>

<h1>Do you love me?</h1>

<div class="btn-container">
    <button id="yesBtn">I love you too ❤️</button>
    <button id="noBtn">I don't love you 💔</button>
</div>

<script>
    const noBtn = document.getElementById("noBtn");
    const yesBtn = document.getElementById("yesBtn");

    function moveButton() {
        const padding = 20;

        const maxX = window.innerWidth - noBtn.offsetWidth - padding;
        const maxY = window.innerHeight - noBtn.offsetHeight - padding;

        let newX = Math.random() * maxX;
        let newY = Math.random() * maxY;

        if (newY < 120) newY = 150;

        noBtn.style.left = newX + "px";
        noBtn.style.top = newY + "px";
    }

    noBtn.addEventListener("mouseenter", moveButton);

    yesBtn.addEventListener("click", () => {
        alert("Awwww I love you too 😳❤️");
    });
</script>

</body>
</html>
"""

@app.route("/love")
def love_game():
    return render_template_string(LOVE_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
