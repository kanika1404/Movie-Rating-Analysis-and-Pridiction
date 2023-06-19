import joblib
import pandas as pd
from flask import Flask, render_template, request
loaded_model = joblib.load("movie_rating_model.pkl")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    runtime = float(request.form['input1'])
    votes = float(request.form['input2'])
    label = float(request.form['input3'])

    new_data = pd.DataFrame({'runtime': [runtime], 'votes': [votes], 'label': [label]})

    # Perform the same preprocessing steps on the new data
    X_new = new_data[['runtime', 'votes', 'label']]
    X_new_encoded = pd.get_dummies(X_new)

    # Make predictions on the new data using the loaded model
    prediction = loaded_model.predict(X_new_encoded)
    # Pass the output to the result page
    return render_template('result.html', output=prediction)

if __name__ == '__main__':
    app.run(debug=True)


