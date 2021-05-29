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
        val=int(request.form.get('value'))
        out=int(model.predict([[val]]))
        
        return render_template("output.html", output=str(out))
app.run(host="172.17.0.2",debug=True)
