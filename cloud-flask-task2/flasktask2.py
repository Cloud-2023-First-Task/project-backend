"""flask module and methods import"""
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    """basic endpoint"""
    return render_template('home.html')

@app.route('/hello', methods=['POST', 'GET'])
def hello_name():
    """second endpoint, first it will show input to enter name,
    then the name will be saved and to result page"""
    if request.method == 'POST':
        input_data = request.form['input']
        return render_template('printname.html', input_data=input_data)
    return render_template('entername.html')

if __name__ == "__main__":
    app.run(debug=True)
