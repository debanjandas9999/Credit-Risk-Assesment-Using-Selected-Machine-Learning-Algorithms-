from flask.globals import session
from flask.helpers import url_for
import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
import pandas as pd
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/loanform')
def loanform():
	return render_template('Individual.html')


@app.route('/loanform',methods=['POST'])
def predict():
    if request.method == 'POST':
        a = request.form['Status of existing checking account']
        b = request.form['Duration in month']
        c = request.form['Credit history']
        d = request.form['Purpose']
        e = request.form['Credit amount']
        f = request.form['Savings account/bonds']
        g = request.form['Present employment since']
        h = request.form['Installment rate in percentage of disposable income']
        i = request.form['Personal status and sex']
        j = request.form['select']
        k = request.form['Present residence since']
        l = request.form['Property']
        m = request.form['Age in years']
        n = request.form['Other installment plans']
        o = request.form['Housing']
        p = request.form['Number of existing credits at this bank']
        q = request.form['Job']
        r = request.form['Number of people being liable to provide maintenance for']
        s = request.form['Telephone']
        t = request.form['foreign worker']


        int_features = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
        featu = [int(x) for x in int_features]
        cols = model.get_booster().feature_names
        df = pd.DataFrame([featu], columns=cols)
        prediction = model.predict(df)
        print(prediction[0])

        if prediction[0] == 0:
            prediction_text='r'
            print("r")
        else:
            prediction_text='a'
            print("a")

    return render_template('result.html', prediction_text=prediction_text)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080,debug=True)
