from flask import Flask, request, redirect, render_template, url_for
from datetime import datetime

app = Flask(__name__)

shift_list = []

# Render home page
@app.route("/")
def home():
    return render_template("home.html")

# Render schedule page
@app.route("/schedule")
def schedule():
    return render_template("schedule.html", shifts=shift_list)

# Add all attributes to dictionary, add dictionary to list
@app.route("/add-shift", methods=["POST"])
def add_shift():
    fname = (request.form.get("fname"))
    lname = (request.form.get("lname"))
    shift_date = (request.form.get("date"))
    shift_start = datetime.strptime(request.form.get("start"), "%H:%M") # Formatting time to 12-hour format
    shift_end = datetime.strptime(request.form.get("end"), "%H:%M")
    my_dict = {"First Name":fname, "Last Name":lname, "Date":shift_date, "Start Time":shift_start.strftime("%I:%M %p"), "End Time":shift_end.strftime("%I:%M %p")}
    shift_list.append(my_dict)
    return redirect(url_for("schedule"))

# Run application
if __name__ == "__main__":
    app.run(debug=True)

