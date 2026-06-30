# Smart Bus Sync System

## Overview

Smart Bus Sync System is a Flask and PostgreSQL based web application developed to manage college bus attendance and optimize bus utilization.

The system records daily student attendance, monitors bus occupancy, and recommends bus merging or student redistribution based on real-time attendance.

---

## Features

### Student Attendance

* Search student using Student ID
* Mark attendance
* Present
* Absent
* Study Leave
* Semester Leave

### Attendance History

* View today's attendance
* Search using Bus Number
* Status-wise attendance

### Bus Dashboard

* Display today's bus strength
* Current attendance count
* Bus-wise statistics

### Bus Recommendation

* Identify buses sharing a common stop
* Calculate today's strength
* Recommend:

  * Merge buses
  * Split weak buses
  * No merge required

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Jinja2

### Backend

* Python
* Flask

### Database

* PostgreSQL

### Development Environment

* Linux Mint
* Git

---

## Project Structure

smart-bus-system/

├── app.py

├── config/

├── database/

├── docs/

├── static/

├── templates/

├── requirements.txt

└── README.md

---

## Database Tables

* student
* student_status
* bus_stop
* bus_common_stop
* bus_capacity

---

## How to Run

### Clone Repository

git clone <repository-url>

### Create Virtual Environment

python3 -m venv venv

### Activate

source venv/bin/activate

### Install Packages

pip install -r requirements.txt

### Run

python app.py

---

## Future Enhancements

* RFID Integration
* GPS Tracking
* Driver Mobile App
* Live Bus Location
* Route Optimization
* Data Engineering Pipeline
* Predictive Bus Occupancy
* Power BI Dashboard

---

## Author

Sanjana

Smart Bus Sync System

Version 1.0
