from flask import Flask, render_template, request, redirect, session, url_for
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
#    if 'username' in session:
#        return 'Logged in as %s' % escape(session['username'])
#    return 'You are not logged in'
    return render_template('index.html')
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#@app.route('/login', methods=['POST', 'GET'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if valid_login(request.form['username'],
#                      request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = 'Invalid username/password'
#    return render_template('login.html', error=error)

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        session['username'] = request.form['username']
#        return redirect(url_for('index'))
#    return '''
#        <form method="post">
#            <p><input type=text name=username>
#            <p><input type=submit value=Login>
#        </form>
#    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/testing/urlkeypairs')
def use_arguments():
    arguments = request.args
    return render_template('testing_arguments.html', args = arguments)

@app.route("/meapi")
def me_api():
    #Need to make forms and add login functions first! But this is cool!
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
