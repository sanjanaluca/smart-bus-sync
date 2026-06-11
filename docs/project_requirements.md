# Smart Bus Sync System - Project Requirements

## Project Overview

Smart Bus Sync System is a web-based transport management system that helps optimize bus stops, track buses using GPS, and verify student boarding using RFID.

## User Roles

1. Admin
2. Student
3. Bus Incharge

## Student Features

* Login to the system
* Update daily status:

  * Present
  * Absent
  * Semester Leave
  * Study Leave
* View bus information

## Bus Incharge Features

* View students expected at each stop
* View RFID attendance records
* Monitor bus location

## Admin Features

* Manage students
* Manage buses
* Manage routes and stops
* View reports and attendance

## RFID Functionality

* Morning boarding attendance
* Evening boarding attendance
* Attendance recorded using RFID card scans

## GPS Functionality

* GPS hardware device installed in buses
* Live bus location tracking

## Main Entities

### Student

* ID Number
* Student Name
* College Name
* Department
* Year
* RFID Card Number
* Assigned Bus
* Assigned Stop

### Bus

* Bus Number
* Capacity
* Driver Name
* Driver Phone
* Bus Incharge Name
* Bus Incharge Phone
* GPS Device ID
* Status

### Route

* Route Name
* Source
* Destination

### Bus Stop

* Stop Name
* Route

### Student Daily Status

* Student ID
* Date
* Status
* Submission Time

### RFID Attendance

* Student ID
* RFID Card Number
* Bus Number
* Scan Time
* Attendance Type (Morning/Evening)

### GPS Tracking

* Bus Number
* Latitude
* Longitude
* Timestamp
