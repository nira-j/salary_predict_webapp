from flask import Flask, render_template, request
import joblib
import socket

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
    
s = socket.gethostname()
ip = socket.gethostbyname(s)
app.run(host = ip, debug=True)
