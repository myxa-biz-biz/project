from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('vstyplenie.html')

@app.route('/osnova/')
def osnova():
	return render_template('osnovnay_chast.html')

@app.route('/modi/')
def modi():
	return render_template('modi_i_resyrspaki.html')





app.run()
