from flask import Flask, render_template, request



app = Flask(__name__)
details =[]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        print(request.form)
        details.append(
            (
                request.form.get("firstname"),
                request.form.get("phone"),
                request.form.get("email")
            )
        )
    return render_template("form.html")


@app.route("/result")
def result():
    return render_template("result.html",email=email)

if __name__=="__main__":
    app.run(debug=True)




