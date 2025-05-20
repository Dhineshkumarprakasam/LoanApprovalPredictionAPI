from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')
bank_val = joblib.load('bank_value.pkl')
com_val = joblib.load('com_value.pkl')
lux_val = joblib.load("lux_value.pkl")
res_val = joblib.load("res_value.pkl")
ipa = joblib.load("income_annum.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True) 

    income = ipa.transform([[data['income_annum']]])[0][0]
    bank = bank_val.transform([[data['bank_value']]])[0][0]
    comm = com_val.transform([[data['com_value']]])[0][0]
    lux = lux_val.transform([[data['lux_value']]])[0][0]
    res = res_val.transform([[data['res_value']]])[0][0]

    education_val = 0 if data['education'] == "graduate" else 1
    emp_val = 0 if data['self-employed'] == "no" else 1

    x = [[
        data['dependents'],
        data['loan_term'],
        data['cibil_score'],
        education_val,
        emp_val,
        income,
        res,
        comm,
        lux,
        bank
    ]]

    prediction = model.predict(x)
    return jsonify({'prediction': prediction.tolist()[0]})

if __name__ == '__main__':
    app.run()
