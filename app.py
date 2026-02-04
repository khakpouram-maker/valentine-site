from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>💘 A Question for You</title>
    <style>
        body {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
        }
        .card {
            background: rgba(255,255,255,0.2);
            padding: 40px;
            border-radius: 20px;
            max-width: 400px;
        }
        button {
            font-size: 20px;
            padding: 12px 30px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Will you be my Valentine? 💖</h1>
        <p>I made this just for you</p>
        <button onclick="alert('Best answer 😌💘')">YES 💘</button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run()
