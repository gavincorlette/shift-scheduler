from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

shift_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html", shifts=shift_list)

@app.route("/add-shift", methods=["POST"])
def add_shift():
    fname = (request.form.get("fname"))
    lname = (request.form.get("lname"))
    shift_date = (request.form.get("date"))
    shift_start = (request.form.get("start"))
    shift_end = (request.form.get("end"))
    my_dict = {"First Name":fname, "Last Name":lname, "Date":shift_date, "Start Time":shift_start, "End Time":shift_end}
    shift_list.append(my_dict)
    return redirect(url_for("schedule"))


if __name__ == "__main__":
    app.run(debug=True)

