from flask import Flask, render_template_string
import os

app = Flask(__name__)
app.debug = False

# ---------- HOME PAGE ----------
home_page = '''
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>𝐑𝐊 𝐑𝐀𝐉𝐀 𝐗𝐖𝐃 𝐏𝐀𝐍𝐄𝐋</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
          rel="stylesheet">

    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

    <style>
        body {
            background-color: #000;
            color: white;
            font-family: 'Courier New', monospace;
            text-align: center;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }

        h1 {
            font-size: 30px;
            color: #f0f;
            text-shadow: 0 0 10px #f0f;
            margin-bottom: 10px;
        }

        .container {
            max-width: 700px;
            margin: 0 auto;
        }

        .button-box {
            margin: 15px auto;
            padding: 20px;
            border: 2px solid #00ffff;
            border-radius: 10px;
            background: #000;
            max-width: 90%;
            box-shadow: 0 0 15px #00ffff;
        }

        .button-box a {
            display: inline-block;
            background-color: #00ffff;
            color: #000;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 15px;
            text-decoration: none;
            width: 100%;
        }

        .button-box a:hover {
            box-shadow: 0 0 12px #00ffff;
            background-color: #0ff;
        }

        footer {
            margin-top: 40px;
            color: #aaa;
            font-size: 12px;
        }

        footer a {
            color: #0ff;
            text-decoration: none;
            margin: 0 5px;
        }

        .admin {
            margin-top: 25px;
        }

        .admin a {
            display: block;
            background: #ff00ff;
            color: #000;
            padding: 12px;
            border-radius: 7px;
            font-weight: bold;
            text-decoration: none;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>𝐑𝐊 𝐑𝐀𝐉𝐀 𝐗𝐖𝐃</h1>
    <h2>(𝐀𝐋𝐋 𝐎𝐏𝐓𝐈𝐎𝐍)</h2>

    <div class="button-box">
        <a href="/section/1">◄ 1 – CONVO SERVER ►</a>
    </div>

    <div class="button-box">
        <a href="/go/backup_convo">◄ 2 – BACKUP CONVO ►</a>
    </div>

    <div class="button-box">
        <a href="/section/2">◄ 3 – POST SERVER ►</a>
    </div>

    <div class="button-box">
        <a href="/go/backup_post">◄ 4 – BACKUP POST SERVER ►</a>
    </div>

    <div class="button-box">
        <a href="/section/3">◄ 5 – TOKEN CHECK VALIDITY ►</a>
    </div>

    <div class="button-box">
        <a href="/section/4">◄ 6 – FETCH ALL UID WITH TOKEN ►</a>
    </div>

    <div class="button-box">
        <a href="/section/5">◄ 7 – FETCH PAGE TOKENS ►</a>
    </div>

    <div class="button-box">
        <a href="/go/group_name_locker">◄ 8 – GROUP NAME LOCKER ►</a>
    </div>

    <div class="button-box">
        <a href="/go/yt_downloader">◄ 9 – YOUTUBE DOWNLOADER ►</a>
    </div>

    <div class="button-box">
        <a href="/go/insta_downloader">◄ 10 – INSTAGRAM DOWNLOADER ►</a>
    </div>

    <div class="button-box">
        <a href="/go/fb_downloader">◄ 11 – FACEBOOK DOWNLOADER ►</a>
    </div>

    <div class="button-box">
        <a href="/go/cookie_json">◄ 12 – COOKIE TO JSON ►</a>
    </div>

    <div class="admin">
        <a href="/admin">⚙ ADMIN PANEL</a>
    </div>

</div>

<footer>
    <p>© 2026 MADE BY :- 𝐑𝐊 𝐑𝐀𝐉𝐀 𝐗𝐖𝐃 𝐏𝐀𝐍𝐄𝐋</p>
    <p>𝘼𝙇𝙒𝘼𝙔𝙎 𝙊𝙉 𝙁𝙄𝙍𝙀 🔥</p>

    <p>
        <a href="https://www.facebook.com/">Chat on Messenger</a>
    </p>
</footer>

</body>
</html>
'''


# ---------- ADMIN PAGE ----------
admin_page = '''
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RK RAJA ADMIN</title>

    <style>
        body {
            background: #000;
            color: white;
            font-family: monospace;
            text-align: center;
            padding: 30px;
        }

        h1 {
            color: #ff00ff;
            text-shadow: 0 0 15px #ff00ff;
        }

        .box {
            max-width: 600px;
            margin: 30px auto;
            padding: 25px;
            border: 2px solid #00ffff;
            border-radius: 10px;
            box-shadow: 0 0 15px #00ffff;
        }

        a {
            display: block;
            margin-top: 20px;
            padding: 12px;
            background: #00ffff;
            color: #000;
            text-decoration: none;
            font-weight: bold;
            border-radius: 6px;
        }
    </style>
</head>

<body>

<h1>𝐑𝐊 𝐑𝐀𝐉𝐀 𝐀𝐃𝐌𝐈𝐍</h1>

<div class="box">
    <h2>ADMIN PANEL</h2>
    <p>Panel successfully running.</p>

    <a href="/">◄ BACK HOME ►</a>
</div>

</body>
</html>
'''


# ---------- HOME ----------
@app.route('/')
def home():
    return render_template_string(home_page)


# ---------- ADMIN ----------
@app.route('/admin')
def admin():
    return render_template_string(admin_page)


# ---------- SECTION ----------
@app.route('/section/<int:section_id>')
def section(section_id):
    return render_template_string(f'''
    <!doctype html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RK RAJA XWD</title>
        <style>
            body {{
                background:#000;
                color:#00ffff;
                text-align:center;
                font-family:monospace;
                padding:30px;
            }}

            .box {{
                max-width:600px;
                margin:30px auto;
                padding:25px;
                border:2px solid #00ffff;
                border-radius:10px;
                box-shadow:0 0 15px #00ffff;
            }}

            a {{
                display:block;
                margin-top:20px;
                padding:12px;
                background:#00ffff;
                color:#000;
                text-decoration:none;
                font-weight:bold;
                border-radius:6px;
            }}
        </style>
    </head>

    <body>

        <div class="box">
            <h1>SECTION {section_id}</h1>
            <p>Feature page is ready.</p>
            <a href="/">◄ BACK HOME ►</a>
        </div>

    </body>
    </html>
    ''')


# ---------- OTHER FEATURES ----------
@app.route('/go/<name>')
def go(name):
    return render_template_string(f'''
    <!doctype html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RK RAJA XWD</title>
        <style>
            body {{
                background:#000;
                color:#fff;
                text-align:center;
                font-family:monospace;
                padding:30px;
            }}

            .box {{
                max-width:600px;
                margin:30px auto;
                padding:25px;
                border:2px solid #ff00ff;
                border-radius:10px;
                box-shadow:0 0 15px #ff00ff;
            }}

            a {{
                display:block;
                margin-top:20px;
                padding:12px;
                background:#ff00ff;
                color:#000;
                text-decoration:none;
                font-weight:bold;
                border-radius:6px;
            }}
        </style>
    </head>

    <body>

        <div class="box">
            <h1>{name.replace("_", " ").upper()}</h1>
            <p>Feature page is ready.</p>
            <a href="/">◄ BACK HOME ►</a>
        </div>

    </body>
    </html>
    ''')


# ---------- START ----------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 22061))
    app.run(host='0.0.0.0', port=port)
