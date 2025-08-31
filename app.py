# app.py
# The web portal for the MEGA-CORE protocol.

from flask import Flask, render_template_string, request
from src.core import calculate_semantic_fractal_dimension, calculate_ontological_resonance

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>MEGA-CORE Protocol Portal</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        label { display: block; margin-top: 10px; }
        textarea { width: 100%; height: 100px; }
        input[type="submit"] { margin-top: 10px; padding: 10px 20px; }
        .result { margin-top: 20px; padding: 15px; border: 1px solid #ccc; background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>MEGA-CORE Protocol Portal</h1>
    <form action="/" method="post">
        <label for="text1">Текст 1:</label>
        <textarea id="text1" name="text1"></textarea>
        <label for="text2">Текст 2:</label>
        <textarea id="text2" name="text2"></textarea>
        <input type="submit" value="Анализировать">
    </form>
    {% if result %}
    <div class="result">
        <h2>Результаты анализа:</h2>
        <p><strong>Семантическая Фрактальная Размерность (Df) Текста 1:</strong> {{ result.df1 }}</p>
        <p><strong>Семантическая Фрактальная Размерность (Df) Текста 2:</strong> {{ result.df2 }}</p>
        <p><strong>Онтологический Резонанс:</strong> {{ result.resonance }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

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

    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
