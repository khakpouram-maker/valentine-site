from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title> 💘 For My Remah :) </title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background-image: url('/static/background.png');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Aptos', sans-serif;
            overflow: hidden;
        }

        .card {
            background: rgba(255,255,255,0.85);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            max-width: 420px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        h1 {
            color: #ff4d6d;
        }

        button {
            font-size: 20px;
            padding: 12px 30px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            margin: 10px;
        }

        #yes {
            background: #ff4d6d;
            color: white;
        }

        #no {
            background: #999;
            color: white;
            position: absolute;
        }

        .heart, .balloon {
            position: fixed;
            bottom: -50px;
            font-size: 30px;
            animation: floatUp 5s linear infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-120vh); opacity: 0; }
        }
    </style>
</head>

<body>

<div class="card" id="question">
    <h1>Will you be my Valentine Date Remah (My Princess)? 💖</h1>
    <button id="yes" onclick="sayYes()">YES Amir 💘</button>
    <button id="no">No wtf?</button>

    <!-- Spotify player (hidden but plays) -->
    <iframe style="display:none"
        src="https://open.spotify.com/embed/track/3Y2x4rJYqVZxG7mH2W9p8k?autoplay=1"
        width="300" height="80" frameborder="0"
        allow="autoplay; clipboard-write; encrypted-media">
    </iframe>
</div>

<script>
    const noBtn = document.getElementById("no");

    noBtn.addEventListener("mouseover", () => {
        noBtn.style.left = Math.random() * 80 + "vw";
        noBtn.style.top = Math.random() * 80 + "vh";
    });

    function sayYes() {
        document.getElementById("question").innerHTML = `
            <h1>YAAAAAY!!! 🎉💖</h1>
            <p style="font-size:18px;">
                From Amir to Remah: My love, I can't express my feelings about you through words. You're amazing, sweet, smart, sooo fucking pretty, and if I want to say more, I can write a book with it. Whenever you smile, whenever you look at me, it's like my heart, my hands, my body, no wait, my sould is shaking. I love you my Remah, my pretty princess :)  💕
            </p>
        `;
        launchLove();
        alert("I LOVE YOU BABE KISS KISS ❤️ - Click on the close bottom I gotta tell u sth");
    }

    function launchLove() {
        for (let i = 0; i < 30; i++) {
            create("❤️", "heart");
            create("🎈", "balloon");
        }
    }

    function create(symbol, cls) {
        const el = document.createElement("div");
        el.className = cls;
        el.innerText = symbol;
        el.style.left = Math.random() * 100 + "vw";
        el.style.animationDuration = (Math.random() * 3 + 3) + "s";
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 6000);
    }
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run()
