import smtplib, ssl
from email.message import EmailMessage
from tkinter import filedialog

def saada_kiri():
    kellele = input('Kellele saata: ')
    teema = input('Teema: ')
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    kellelt = 'eha20082@gmail.com'
    salasõna = input('Salasõna: ')

    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = kellelt
    msg['To'] = kellele

    text_sisu = "Tere! Kui sa ei näe seda kirja õigesti, palun lülita sisse HTML kuvamine."

    html_sisu = """\
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            h1 { color: #ff0000; }
            p { font-size: 12px; }
            a { color: #008000; }
        </style>
    </head>
    <body>
        <h1>Sending an HTML email from Python</h1>
        <p>Tere õpetaja,</p>
        <p>This is a <b> beautiful email</b> with a clickable link :</p>
        <a href="https://tahvel.edu.ee/#/">link in Tahvel!</a>
    </body>
    </html>
    """

    msg.set_content(text_sisu)
    msg.add_alternative(html_sisu, subtype='html')
    fail = filedialog.askopenfilename(title='Vali fail', filetypes=[('All files', '*.*')])
    if fail:
        with open(fail, 'rb') as f:
            faili_sisu = f.read()
            faili_nimi = fail.split('/')[-1]
            msg.add_attachment(faili_sisu, maintype='application', subtype='octet-stream', filename=faili_nimi)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, salasõna)
            server.send_message(msg)
        print('Kiri saadetud')
    except Exception as e:
        print(f'Ver Error: {e}')

saada_kiri()
