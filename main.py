from flask import Flask, request, redirect, render_template, url_for
from datetime import datetime

app = Flask(__name__)

shift_list = []

# ID for shifts in order to delete or edit them
next_id = 1

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
    global next_id
    fname = (request.form.get("fname"))
    lname = (request.form.get("lname"))
    shift_date = datetime.strptime(request.form.get("date"), "%Y-%m-%d") # Formatting date to be more readable
    shift_start = datetime.strptime(request.form.get("start"), "%H:%M") # Formatting time to 12-hour format
    shift_end = datetime.strptime(request.form.get("end"), "%H:%M")
    my_dict = {"ID":next_id, "First Name":fname, "Last Name":lname, "Date":shift_date.strftime("%b %d, %Y"), "Start Time":shift_start.strftime("%I:%M %p"), "End Time":shift_end.strftime("%I:%M %p")}
    shift_list.append(my_dict)
    
    # Each time a shift is submitted, the ID increments
    next_id += 1

    return redirect(url_for("schedule"))

# Function to edit shift
@app.route("/edit-shift", methods=["GET", "POST"])
def edit_shift():
    return redirect(url_for("schedule"))

# Function to delete shift
@app.route("/delete-shift", methods=["GET"])
def delete_shift():
    shift_id = int(request.args.get("id"))
    for shift in shift_list:
        if shift["ID"] == shift_id:
            shift_list.remove(shift)
    return redirect(url_for("schedule"))

# Run application
if __name__ == "__main__":
    app.run(debug=True)

