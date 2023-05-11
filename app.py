from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle
import sqlite3

app = Flask(__name__)

# Load the XGBoost model
xgb_model = pickle.load(open('./models/xgb_test.pkl', 'rb'))

@app.route('/')
def home():
    # Render the home.html template
    return render_template('home.html')

@app.route('/get_random_row', methods=['GET'])
def get_random_row():
    # Connect to the SQLite database
    conn = sqlite3.connect('bank-account-fraud.db')
    cursor = conn.cursor()

    # Select a random row from the X_test table
    cursor.execute('SELECT * FROM X_test ORDER BY RANDOM() LIMIT 1')
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Create keys and values for the JSON response
    keys = ["income", "name_email_similarity", "prev_address_months_count", "current_address_months_count",
            "customer_age", "days_since_request", "intended_balcon_amount", "zip_count_4w", "velocity_6h",
            "velocity_24h", "velocity_4w", "bank_branch_count_8w", "date_of_birth_distinct_emails_4w",
            "credit_risk_score", "email_is_free", "phone_home_valid", "phone_mobile_valid", "bank_months_count",
            "has_other_cards", "proposed_credit_limit", "foreign_request", "session_length_in_minutes",
            "keep_alive_session", "device_distinct_emails_8w", "month", "payment_type_AA", "payment_type_AB",
            "payment_type_AC", "payment_type_AD", "payment_type_AE", "employment_status_CA", "employment_status_CB",
            "employment_status_CC", "employment_status_CD", "employment_status_CE", "employment_status_CF",
            "employment_status_CG", "housing_status_BA", "housing_status_BB", "housing_status_BC", "housing_status_BD",
            "housing_status_BE", "housing_status_BF", "housing_status_BG", "source_INTERNET", "source_TELEAPP",
            "device_os_linux", "device_os_macintosh", "device_os_other", "device_os_windows", "device_os_x11"]

    data = {k: float(v) for k, v in zip(keys, row)}
    print(data)
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data and convert it to a numpy array
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)

    # Make predictions using the XGBoost model
    output = xgb_model.predict(final_input)[0]

    if output == 1:
        predicted_class = "Fraud"
    else:
        predicted_class = "Genuine"

    # Render the home.html template with the prediction result
    return render_template("home.html", prediction_text=f"Predicted Class of Bank Account Application is {predicted_class}")

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get the JSON data from the request
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = np.array(list(data.values())).reshape(1, -1)

    # Make predictions using the XGBoost model
    output = xgb_model.predict(new_data)
    print(output[0])

    # Return the prediction as a JSON response
    return jsonify(f"Predicted Class of Bank Account Application is {int(output[0])}")

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)


