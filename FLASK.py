from flask import Flask, render_template, request
import numpy as np
from anp import calculate_anp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        sambal_scores = {
            'Sambal Bawang': float(request.form['sambal_bawang']),
            'Sambal Ijo': float(request.form['sambal_ijo']),
            'Sambal Matah': float(request.form['sambal_matah']),
            'Sambal Kecap': float(request.form['sambal_kecap']),
            'Sambal Terasi': float(request.form['sambal_terasi']),
            'Sambal Pete': float(request.form['sambal_pete'])
        }
        result = calculate_anp(sambal_scores)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
