import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from flask import Flask , render_template , request
import gunicorn


#load model
model = pickle.load(open('Loan_cls_model.pkl', "rb"))

#load scaler
scalerfile = 'scaler.save'
scaler = pickle.load(open(scalerfile, 'rb'))

# flask contrsuctor
app = Flask(__name__)

@app.route('/')

#render home page
@app.route('/Home',methods=["GET"])
def Home():

    #render template
    return render_template('index.html')

#render form.html
@app.route('/Form',methods=["GET"])
def Form():

    #render template
    return render_template('form.html')

#get form data from form.html
@app.route('/classifier',methods=['GET','POST'])
def classifier():

    #checking request type
    str_req_type = request.method

    # get form data
    if request.method == str(str_req_type):

        Gender = request.args.get('gender')

        Martial_st = request.args.get('matialstatus')

        Dependents = request.args.get('dependents')

        Education = request.args.get('education')

        Self_Employed = request.args.get('self_emp_status')

        Credit_History = request.args.get('credithistory')

        Property_Area = request.args.get('property_area')

        ApplicantIncome = request.args.get('app_income')

        CoapplicantIncome = request.args.get('co_app_ic')

        LoanAmount = request.args.get('loanamount')

        Loan_Amount_Term = request.args.get('loan_term')

        # change gender.........................................
        if Gender == 'Female':
            Gender = 0

        elif Gender == 'Male':
            Gender = 1

        # change martial status..................................
        if Martial_st == 'Married':
            Martial_st = 1

        elif Martial_st == 'Unmarried':
            Martial_st = 0

        # change Dependents status..................................
        if Dependents == '0':
            Dependents = 0

        elif Dependents == '1':
            Dependents = 1

        elif Dependents == '2':
            Dependents = 2

        elif Dependents == '3+':
            Dependents = 3

        # change Education status..................................
        if Education == 'Graduate':
            Education = 0

        elif Education == 'Not Graduate':
            Education = 1

        # change Self_Employed status..................................
        if Self_Employed == 'Yes':
            Self_Employed = 1

        elif Self_Employed == 'No':
            Self_Employed = 0

        # change credit history status..................................
        if Credit_History == 'Yes':
            Credit_History = 1

        elif Credit_History == 'No':
            Credit_History = 0

        # change Property Area status..................................
        if Property_Area == 'Urban':
            Property_Area = 0

        elif Property_Area == 'Rural':
            Property_Area = 1

        elif Property_Area == 'Semi Urban':
            Property_Area = 2

        # add feature value to set
        input_data = [Gender, Martial_st, Dependents, Education, Self_Employed, float(ApplicantIncome),
                      float(CoapplicantIncome), float(LoanAmount), float(Loan_Amount_Term), Credit_History, Property_Area]

        # pre processing
        input_array = np.asarray(input_data)
        arr_reshape = input_array.reshape(1, -1)

        #scal value
        scaled = scaler.transform(arr_reshape)

        # predict using model
        Loan_pred = model.predict(scaled)

        # assign string to pass the data to webapp
        if Loan_pred[0]==1:
            cl_value = "Accepted"

        elif Loan_pred[0]==0:
            cl_value = "Rejected"

        # render template with final output
        return  render_template('result.html', value=cl_value)


if __name__ == '__main__':
    app.run(debug=True)
