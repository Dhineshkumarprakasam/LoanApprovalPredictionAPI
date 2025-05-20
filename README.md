# Loan Approval Prediction API

This is a simple Flask API that predicts loan approval using a pre-trained machine learning model. The model processes various financial and personal features provided in the request and returns a prediction.

## 🌐 Hosted API

You can access the live API here:
👉 **[https://loanapprovalprediction-production.up.railway.app](https://loanapprovalprediction-production.up.railway.app)**

## 🔧 Features

* Accepts user input via a POST request in JSON format.
* Applies transformations using pre-fitted encoders.
* Returns loan approval prediction as a JSON response.

## 📦 Requirements

* Python 3.x
* Flask
* joblib
* scikit-learn

Install dependencies with:

```bash
pip install flask scikit-learn joblib
```

## 📁 Files

* `app.py` – Main API logic
* `model.pkl` – Trained prediction model
* `*_value.pkl` – Label encoders for transforming input features:

  * `bank_value.pkl`
  * `com_value.pkl`
  * `lux_value.pkl`
  * `res_value.pkl`
  * `income_annum.pkl`

## 🚀 How to Use

### Endpoint

**`POST /predict`**

📍 Full URL:
`https://loanapprovalprediction-production.up.railway.app/predict`

### Request Body (JSON)

```json
{
  "dependents": 2,
  "loan_term": 360,
  "cibil_score": 750,
  "education": "graduate",
  "self-employed": "no",
  "income_annum": 500000,
  "res_value": 300000,
  "com_value": 150000,
  "lux_value": 100000,
  "bank_value": 200000
}
```

### Response

```json
{
  "prediction": 1
}
```

> 🔢 A prediction of `1` may represent *Loan Approved*, and `0` may mean *Loan Not Approved* (based on your model setup).
