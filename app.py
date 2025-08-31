# app.py
# The web portal for the MEGA-CORE protocol.

from flask import Flask, render_template, request
from src.core import calculate_semantic_fractal_dimension, calculate_ontological_resonance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text1 = request.form["text1"]
        text2 = request.form["text2"]

        df1 = calculate_semantic_fractal_dimension(text1)
        df2 = calculate_semantic_fractal_dimension(text2)
        resonance = calculate_ontological_resonance(text1, text2)

        result = {
            "df1": df1,
            "df2": df2,
            "resonance": resonance,
        }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
