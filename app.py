from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>💘 For My Remah :)</title>

    <style>
        body {
            margin: 0;
            height: 100vh;
            background-image: url('{{ url_for("static", filename="background.png") }}');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Aptos', sans-serif;
            overflow: hidden;
        }

        .card {
            background: rgba(255,255,255,0.88);
            padding: 30px;
            border-radius: 22px;
            text-align: center;
            max-width: 440px;
            box-shadow: 0 20px 45px rgba(0,0,0,0.35);
        }

        h1 {
            color: #ff4d6d;
        }

        button {
            font-size: 20px;
            padding: 12px 32px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            margin: 12px;
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
            bottom: -60px;
            font-size: 32px;
            animation: floatUp linear infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-120vh); opacity: 0; }
        }
    </style>
</head>

<body>

<div class="card" id="question">
    <h1>Will you be my Valentine date, Remah (my princess)? 💖</h1>

    <button id="yes" onclick="sayYes()">YES Amir 💘</button>
    <button id="no">No wtf?</button>
</div>

<script>
    const noBtn = document.getElementById("no");

    // NO button runs away 😈
    noBtn.addEventListener("mouseover", () => {
        noBtn.style.left = Math.random() * 80 + "vw";
        noBtn.style.top = Math.random() * 80 + "vh";
    });

    function sayYes() {
        document.getElementById("question").innerHTML = `
            <h1>YAAAAAY!!! 🎉💖</h1>
            <p style="font-size:18px; line-height:1.4;">
                From Amir to Remah ❤️<br><br>
                My love, I can’t express my feelings about you with words.
                You’re amazing, sweet, smart, and sooo unbelievably pretty.
                If I wanted to say everything about you, I’d need a whole book.
                Every time you smile or look at me, my heart — no, my soul —
                literally shakes. I love you, my Remah, my beautiful princess. 💕
            </p>
        `;

        playSong();
        launchLove();

        alert("I LOVE YOU BABE ❤️ KISS KISS — click close, I gotta tell you something 😘");
    }

    // 🎵 Spotify starts AFTER clicking YES (browser-safe)
    function playSong() {
        const iframe = document.createElement("iframe");
        iframe.src = "https://open.spotify.com/embed/track/0p6I1Kc5V4YqFlvZ3dZ1iM";
        iframe.style.display = "none";
        iframe.allow = "autoplay; clipboard-write; encrypted-media";
        document.body.appendChild(iframe);
    }

    // 🎈❤️ Hearts + balloons
    function launchLove() {
        for (let i = 0; i < 35; i++) {
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
        setTimeout(() => el.remove(), 6500);
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
