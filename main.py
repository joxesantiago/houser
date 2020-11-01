from flask import Flask, render_template, redirect, request, session, url_for
import psycopg2

conn = psycopg2.connect("dbname=d1j12hfu81fusv  user=ybvcezhsbtthew password=c25e2e381493ce7f44698d77ca1f30ab3828f97820045c2102e9868d7aed22c8 host=ec2-18-210-90-1.compute-1.amazonaws.com")
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor.execute('SELECT * from accounts WHERE usernames=%s AND passwords=%s',(username,password))
            credentials = cursor.fetchone()
            print(credentials)
            if credentials is not None:
                if credentials[0] == username and credentials[1] == password:
                    return "login successful"
            else:
                return "login unsuccessful, please register"
    return render_template("login.html")
#
# @app.route('/new')
# def new_user():
#     return render_template("register.html")
#
# @app.route('/profile')
# def profile():
#     return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)