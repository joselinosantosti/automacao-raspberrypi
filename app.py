from flask import Flask, render_template, flash, redirect, url_for, request
#from models import Device

app = Flask(__name__)

#device = Device()

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return redirect(url_for('login'))

@app.route("/logar", methods=['POST'])
def logar():
	if request.method == 'POST':
		if request.form['user'] and request.form['senha']:
			if request.form['user'] == 'admin' and request.form['senha'] == 'admin':
				return redirect(url_for('home'))
			else:
				flash('Dados incorretos, tente novamente')
				return redirect(url_for('login'))

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/lighting")
def lighting():
    return render_template('index.html', module='lighting')

@app.route("/dashboard")
def dashboard():
	return render_template('index.html', module='dashboard', temp=30, humi=70)

@app.route("/control", methods=['GET','POST'])
def control():
	device = request.form['device1']
	#device.acionar(1) if device == 'on' else device.acionar(0)
	return 'ok'
	
if __name__ == '__main__':
	app.run(debug=True)
