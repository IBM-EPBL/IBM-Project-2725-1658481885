from flask import *
import requests
import pickle
API_KEY = "iygSkPzuv9W25ggWz0B3cyFDw1xNX450kOuvV_mvm1FH"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
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
    payload_scoring = {"input_data": [{"fields":  ["Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase","Aspartate_Aminotransferase","Total_Protiens","Albumin","Albumin_and_Globulin_Ratio"], "values":total}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6f67d237-4eb4-45e1-a093-ef3baeaca908/predictions?version=2022-11-19', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    p=response_scoring.json()['predictions'][0]['values'][0][0]
    if(p==1):
        c1="green"
        p="You are perfectly Alright"
    else:
        c1="red"
        p="You have a liver desease problem, You must and shouldconsult a doctor. Take care"
    return render_template("result.html",label=str(p),color=c1)


if __name__=='__main__':
    app.run()

