from flask import Flask, render_template, request
import joblib

model=joblib.load('salary_predict.pk1')
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/application", methods=['POST'])
def application():
    if request.method=='POST':
        val=request.form.get('value')
        if val =="":
            val=0.0
        val=float(val)
        out=int(model.predict([[val]]))
        
        return render_template("output.html", output=str(out))
app.run(host="192.168.43.226",debug=True)
