from flask import *
import pickle
app = Flask( __name__ ,template_folder='templates')
model = pickle. load (open( './liver_analysis.pkl' , 'rb'))
@app. route ( '/' )
def intro() :
    return render_template("index.html")
@app. route ( '/app' )
def intro1() :
    return render_template("web.html")
@app.route('/predict',methods=["POST"])
def predict():
    a=request.form["a"]
    b=request.form["b"]
    c=request.form["c"]
    d=request.form["d"]
    e=request.form["e"]
    f=request.form["f"]
    g=request.form["g"]
    h=request.form["h"]
    i=request.form["i"]
    j=request.form["j"]
    if(b.lower()=="female"):
        b=1
    else:
        b=0
    total=[[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h),float(i),float(j)]]
    p=model.predict(total)
    p=p[0]
    if(p==1):
        c1="green"
        p="You are perfectly Alright"
    else:
        c1="red"
        p="You have a liver desease problem, You must and shouldconsult a doctor. Take care"
    return render_template("result.html",label=str(p),color=c1)


if __name__=='__main__':
    app.run()

