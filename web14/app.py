from flask import Flask, request, render_template, session, url_for, redirect, escape

app = Flask(__name__)
app.secret_key = "'&\xd6\xc2\xed\x97\xa2EtsN/\xb2\x17\xf93\xd5\xf3\x16\xe9\x0f\xff\xa5\xedm'"

@app.route('/')
def index():
	if 'username' in session:
		return 'JJANANANAN!!! <h1><a href="/logout">L.O.G.O.U.T</a></h1>'

	return 'You are not logged in <p><a href="/login">Login</a></p>'

@app.route('/student/<username>/<int:user_id>')
def student(username, user_id):
	return 'Hello %s, %d'%(username, user_id)

@app.route('/login', methods=['POST', 'GET'])
def login():
	try:
		if request.method == "POST":
			name = request.form['name']
			passwd = request.form['password']
			if name:
				session['username'] = name
			return render_template('jjan.html', username=session['username'])
	
		else:
			return render_template('login.html')
	except KeyError, err:
		print 'error ->', err
		return 'Get OUT!!'

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/jjan')
def jjan():
	return render_template('')

app.run(debug=True)
