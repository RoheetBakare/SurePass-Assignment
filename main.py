from flask import Flask, render_template, request
from Calculator import cal

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/calculator', methods=['POST'])
def calculator():

	input1 = request.form['input1']
	answer = get_pan_data(float(input1))

 	return render_template (' answer.html ', answer = answer)

app.run(debug= True,host='0.0.0.0', port=8080)