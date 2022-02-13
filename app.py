from flask import Flask
app = Flask(__name__)
from flask import request,render_template
import joblib

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        rates = rates if rates else 0
        model = joblib.load("predict DBS")        
        pred = model.predict([[rates]])

        try:
            s = "Our predict DBS price is:"+str(pred[0][0])
        except:
            s = "wrong in pred " 

        return render_template("index.html",result =s)
    else:
        return render_template("index.html",result = "")

if __name__=="__main__":
    app.run()