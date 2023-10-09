from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/pred', methods=['POST'])
def predict():
    if request.method == "POST":
        # Extracting input values from the form
        Gender = request.form.get("Gender", "Default_Gender")
        Age = float(request.form.get('Age', 0))
        Type_of_Travel = request.form.get('Type_of_Travel', "Default_Type_of_Travel")
        Class = request.form.get('Class', "Default_Class")
        Flight_Distance = float(request.form.get('Flight_Distance', 0))
        
        Inflight_Entertainment = request.form.get('Inflight_Entertainment', "Default_Entertainment")
        Seat_Comfort = request.form.get('Seat_Comfort', "Default_Comfort")
        Onboard_Service = request.form.get('Onboard_Service', "Default_Service")
        Cleanliness = request.form.get('Cleanliness', "Default_Cleanliness")

        # Advanced prediction logic (customize this as needed)
        satisfaction_score = (
    # (Age / 100) +                       # Age as a percentage factor
    # (Flight_Distance / 1000) +          # Flight distance as a percentage factor
    (1 if Inflight_Entertainment == "Yes" else 0) +   # Bonus for inflight entertainment
    (3 if Seat_Comfort == "Excellent" else
     2 if Seat_Comfort == "Good" else
     1 if Seat_Comfort == "Average" else 0) +        # Bonus for seat comfort
    (3 if Onboard_Service == "Excellent" else
     2 if Onboard_Service == "Good" else
     1 if Onboard_Service == "Average" else 0) +    # Bonus for onboard service
    (3 if Cleanliness == "Excellent" else
     2 if Cleanliness == "Good" else
     1 if Cleanliness == "Average" else 0)          # Bonus for cleanliness
)


        # Determine satisfaction based on the satisfaction score
        if satisfaction_score >= 6.0:
            pred = "Passengers have satisfied the Airline Service"
        else:
            pred = "Passengers have neutral or dissatisfied the Airline Service"

        return render_template('result.html', prediction_text=pred)

if __name__ == "__main__":
    app.run(debug=True)
