from flask import Flask, request, render_template
import pickle
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open("RandomForestClassifier.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        sex = request.form["Sex"]
        relationship = request.form["relationship"]
        work_class = request.form["work_class"]
        education = request.form["education"]
        marital_status = request.form["marital-status"]
        occupation = request.form["occupation"]
        age = request.form["age"]
        capital_gain = request.form["capital-gain"]
        capital_loss = request.form["capital-loss"]

        print([[
            age,
            work_class,
            education,
            marital_status,
            occupation,
            relationship,
            sex,
            capital_gain,
            capital_loss
        ]])
        prediction = model.predict([[
            int(age),
            int(work_class),
            int(education),
            int(marital_status),
            int(occupation),
            int(relationship),
            int(sex),
            int(capital_gain),
            int(capital_loss)
        ]])
        output = ['above 50K' if prediction else 'less than 50K']
        return render_template('home.html', prediction_text="Your salary is {}".format(output[0]))
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
