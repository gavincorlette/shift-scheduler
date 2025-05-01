from flask import Flask, request, redirect, render_template, url_for
from datetime import datetime
import json

# JSON file to store shift data between refreshing and loading
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = 'shifts.json'

# Try method since JSON file is empty to start
try:
    shift_list = read_file(file_path)
except FileNotFoundError:
    shift_list = []

# Method to write to JSON file
def write_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

app = Flask(__name__)

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
    write_file('shifts.json', shift_list)
    
    # Each time a shift is submitted, the ID increments
    next_id += 1

    return redirect(url_for("schedule"))

# Function to edit shift
@app.route("/edit-shift", methods=["GET", "POST"])
def edit_shift():
    # Set shift ID as the value from the query string in the URL
    shift_id = int(request.args.get("id"))
    # Check if method is GET request
    if request.method == 'GET':
        shift_to_edit = None
        # Loop and find shift based on shift ID
        for shift in shift_list:
            if shift["ID"] == shift_id:
                shift_to_edit = shift
        return render_template("edit-shift.html", shift=shift_to_edit)

    # Check if method is a POST request
    if request.method == 'POST':
        # Grab form data
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        # Convert date and time
        date = datetime.strptime(request.form.get("date"), "%Y-%m-%d")
        start = datetime.strptime(request.form.get("start"), "%H:%M")
        end = datetime.strptime(request.form.get("end"), "%H:%M")

        # Loop through and update data
        for shift in shift_list:
            if shift['ID'] == shift_id:
                shift['First Name'] = fname
                shift['Last Name'] = lname
                # Format date and time
                shift['Date'] = date.strftime("%b %d, %Y")
                shift['Start Time'] = start.strftime("%I:%M %p")
                shift['End Time'] = end.strftime("%I:%M %p")
        
        write_file('shifts.json', shift_list)

        return redirect(url_for("schedule"))

# Function to delete shift
@app.route("/delete-shift", methods=["GET"])
def delete_shift():
    shift_id = int(request.args.get("id"))
    for shift in shift_list:
        if shift["ID"] == shift_id:
            shift_list.remove(shift)
    
    write_file('shifts.json', shift_list)

    return redirect(url_for("schedule"))

# Run application
if __name__ == "__main__":
    app.run(debug=True)

