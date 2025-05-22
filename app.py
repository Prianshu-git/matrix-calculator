from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def safe_matrix(form, name, rows, cols):
    return np.array([[float(form.get(f"{name}_{i}_{j}", 0)) for j in range(cols)] for i in range(rows)])

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    matrix_a = matrix_b = None
    operation = ""

    if request.method == "POST":
        rows, cols = int(request.form["rows"]), int(request.form["cols"])
        matrix_a = safe_matrix(request.form, "a", rows, cols)
        matrix_b = safe_matrix(request.form, "b", rows, cols)
        operation = request.form["operation"]

        try:
            if operation == "add":
                result = matrix_a + matrix_b
            elif operation == "subtract":
                result = matrix_a - matrix_b
            elif operation == "multiply":
                result = matrix_a @ matrix_b
            elif operation == "transpose_a":
                result = matrix_a.T
            elif operation == "determinant_a":
                result = np.linalg.det(matrix_a)
            elif operation == "inverse_a":
                result = np.linalg.inv(matrix_a)
        except Exception as e:
            result = f"❌ Error: {str(e)}"

    return render_template("index.html", result=result, matrix_a=matrix_a, matrix_b=matrix_b, operation=operation)

if __name__ == "__main__":
    app.run(debug=True)
