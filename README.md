# Shift Scheduler

A simple web application for managing employee shifts, built with Python (Flask) and styled with CSS.

## Overview

Shift Scheduler allows users to add, edit, and delete employee shifts. The shift data is stored in a `shifts.json` file, which is updated automatically whenever a shift is added, edited, or deleted. The web application is easy to use and provides a clean interface to manage shifts.

## Features

- **Add Shifts**: Employees can be scheduled by entering their name, shift date, start time, and end time.
- **Edit Shifts**: Existing shifts can be modified if changes are needed.
- **Delete Shifts**: Shifts can be removed from the schedule.
- **View Schedule**: The current schedule is displayed in an easy-to-read format.
- **Simple and Intuitive**: The interface is designed to be straightforward and user-friendly.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Data Storage**: JSON (`shifts.json`)

## Usage

- **Home Page**: The landing page gives an introduction to the shift scheduler and provides a link to the scheduling page.
- **Schedule Page**: Add, edit, or delete shifts on the schedule. The shifts are displayed in a list with employee names, shift dates, and times.
- **Editing and Deleting Shifts**: Click "Edit" or "Delete" next to each shift to modify or remove it.

## File Structure

- `main.py`: The Flask application that handles routing and logic for adding, editing, and deleting shifts.
- `templates/`: Contains the HTML files used for rendering pages (`home.html`, `schedule.html`, `edit-shift.html`).
- `static/`: Contains the CSS file (`styles.css`) that styles the web pages.
- `shifts.json`: The JSON file used to store the shifts data.
- `requirements.txt`: Lists the dependencies needed to run the app (e.g., Flask).

## Live Application
You can the Shift Scheduler web application by following this link: [https://shift-scheduler-1h9g.onrender.com/](https://shift-scheduler-1h9g.onrender.com/)  
(Heads up, it may take up to a minute to load)
