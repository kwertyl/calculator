from flask import Flask, render_template, request
app = Flask(__name__)


def bobr(a, sigma, b):
    a = float(a)
    b = float(b)
    if sigma == "+":
        return str(a+b)
    if sigma == "-":
        return str(a-b)
    if sigma == "*":
        return str(a*b)
    if sigma == "/":
        return str(a/b)


@app.route("/", methods=['POST', 'GET'])
def calculator():
    if request.method == 'POST':
        a = request.form['text']
        sigma = request.form['sigma']
        b = request.form['title']
        return render_template("calcu.html", alfa =bobr(a, sigma, b))
    else:
        return render_template("calcu.html")


if __name__ == "__main__":
    app.run(debug=True)


