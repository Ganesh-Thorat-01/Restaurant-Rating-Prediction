from inspect import Parameter
from pickle import GET
from flask import Flask, app, render_template, request, redirect, url_for, jsonify,json
from flask.wrappers import Response
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import requests

app=Flask(__name__)

# This Function can be called from any from any front end tool/website
def FunctionPredictResult(InputData):
    Num_Inputs=InputData.shape[0]
    
    # Making sure the input data has same columns as it was used for training the model
    # Also, if standardization/normalization was done, then same must be done for new input
    
    # Appending the new data with the Training data
    DataForML=pd.read_pickle('src/DataForML.pkl')
    DataForML['online_order'].replace({'Yes':1, 'No':0}, inplace=True)
    DataForML['book_table'].replace({'Yes':1, 'No':0}, inplace=True)

    InputData=InputData.append(DataForML, ignore_index=True)
    InputData= InputData.reset_index()
    InputData=InputData.drop(columns=['index'])
   
    InputData['online_order'].replace({'Yes':1, 'No':0}, inplace=True)
    InputData['book_table'].replace({'Yes':1, 'No':0}, inplace=True)
    # Generating dummy variables for rest of the nominal variables

    Data=pd.get_dummies(InputData)
    # Maintaining the same order of columns as it was during the model training
    Predictors=['online_order', 'book_table', 'votes', 'costfor2', 'MealType_Buffet',
       'MealType_Cafes', 'MealType_Delivery', 'MealType_Desserts',
       'MealType_Dine-out', 'MealType_Drinks & nightlife',
       'MealType_Pubs and bars']
    # Generating the input values to the model
    X=Data[Predictors].values[0:Num_Inputs]
    
    PredictorScaler=MinMaxScaler()

    # Storing the fit object for later reference
    PredictorScalerFit=PredictorScaler.fit(X)
    
    # Generating the standardized values of X since it was done while model training also
    X=PredictorScalerFit.transform(X)
    
    # Loading the Function from pickle file
    import pickle
    with open('src/FinalKNNModel.pkl', 'rb') as fileReadStream:
        PredictionModel=pickle.load(fileReadStream)
        # Don't forget to close the filestream!
        fileReadStream.close()
            
    # Genrating Predictions
    Prediction=PredictionModel.predict(X)
    PredictionResult=pd.DataFrame(Prediction, columns=['Prediction'])
    return(PredictionResult)

# Creating the function which can take inputs and return predictions
def FunctionGeneratePrediction(online_order, book_table, MealType,votes, costfor2):
    
    # Creating a data frame for the model input
    SampleInputData=pd.DataFrame(
     data=[[online_order, book_table, MealType,votes, costfor2]],
     columns=['online_order', 'book_table', 'MealType','votes', 'costfor2'])

    # Calling the function defined above using the input parameters
    Predictions=FunctionPredictResult(InputData= SampleInputData)

    # Returning the prediction
    return Predictions.to_json()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/api')
def api_home():
    with open ("templates/api_home.json","r") as data:
        inp= data.read()
    #return inp
    return Response (inp, mimetype='application/json')
    

@app.route('/api/predict', methods=["GET"])
def api_predict():
    try:
        # Getting the paramters from API call
        online_order = str(request.args.get('online_order'))
        book_table=str(request.args.get('book_table'))
        MealType=str(request.args.get('MealType'))
        votes=float(request.args.get('votes'))  
        costfor2=float(request.args.get('costfor2'))
        # Calling the funtion to get predictions
        prediction_from_api=FunctionGeneratePrediction(
                                                        online_order=online_order,
                                                        book_table=book_table,
                                                        MealType=MealType,
                                                        votes=votes,
                                                        costfor2=costfor2

                                                )

        return (prediction_from_api)
    
    except Exception as e:
        return('Something is not right!:'+str(e))

@app.route('/result', methods = ["GET", "POST"])
def predict_result():
    rating=""
    if request.method == "POST":
        online_order =request.form.get('online_order')
        book_table=request.form.get('book_table')
        MealType=request.form.get('MealType')
        votes=float(request.form.get('votes'))
        costfor2=float(request.form.get('costfor2'))

        parameters={'online_order':online_order,'book_table':book_table,'MealType':MealType,'votes':votes,'costfor2':costfor2}
        response = requests.get("https://restaurantratingpredictionapp.herokuapp.com/api/predict", params=parameters,allow_redirects=True,)
        rating=response.text
        rating=rating.replace("{","")
        rating=rating.replace("}","")
        rating=rating.split(':')
        star=round(float(rating[2]))
        rating="Your Restaurant Rating is: "+ str(round(float(rating[2])))+"/5"
    return render_template('result.html', output=rating,star=star)



if __name__ == '__main__':
    app.run()