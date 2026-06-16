-- Smart Bus Sync System
-- PostgreSQL Database Schema
-- Version 1

CREATE TABLE route (
    route_id INTEGER PRIMARY KEY,
    route_name VARCHAR(100) UNIQUE NOT NULL,
    starting_point VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL
);

CREATE TABLE bus (
    bus_number VARCHAR(20) PRIMARY KEY,
    capacity INTEGER NOT NULL,
    driver_name VARCHAR(100) NOT NULL,
    driver_phone VARCHAR(15) NOT NULL,
    incharge_name VARCHAR(100) NOT NULL,
    incharge_phone VARCHAR(15) NOT NULL,
    gps_device_id VARCHAR(50) UNIQUE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (
        status IN ('Active', 'Inactive', 'Maintenance')
    ),
    route_id INTEGER NOT NULL,

    FOREIGN KEY (route_id) REFERENCES route(route_id)
);

CREATE TABLE bus_stop (
    stop_id INTEGER PRIMARY KEY,
    stop_name VARCHAR(100) NOT NULL,
    stop_order INTEGER NOT NULL,
    route_id INTEGER NOT NULL,

    FOREIGN KEY (route_id) REFERENCES route(route_id),

    UNIQUE(route_id, stop_order)
);

CREATE TABLE student (
    id_number VARCHAR(20) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    college_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    rfid_card_number VARCHAR(50) UNIQUE NOT NULL,
    bus_number VARCHAR(20) NOT NULL,
    stop_id INTEGER NOT NULL,

    FOREIGN KEY (bus_number) REFERENCES bus(bus_number),
    FOREIGN KEY (stop_id) REFERENCES bus_stop(stop_id)
);

CREATE TABLE student_status (
    status_id INTEGER PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (
        status IN (
            'Present',
            'Absent',
            'Study Leave',
            'Semester Leave'
        )
    ),
    status_date DATE NOT NULL,

    FOREIGN KEY (student_id) REFERENCES student(id_number)
);

CREATE TABLE rfid_attendance (
    attendance_id INTEGER PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    bus_number VARCHAR(20) NOT NULL,
    stop_id INTEGER NOT NULL,
    attendance_type VARCHAR(20) NOT NULL CHECK (
        attendance_type IN ('Morning', 'Evening')
    ),
    scan_time TIMESTAMP NOT NULL,

    FOREIGN KEY (student_id) REFERENCES student(id_number),
    FOREIGN KEY (bus_number) REFERENCES bus(bus_number),
    FOREIGN KEY (stop_id) REFERENCES bus_stop(stop_id)
);

CREATE TABLE gps_tracking (
    tracking_id INTEGER PRIMARY KEY,
    bus_number VARCHAR(20) NOT NULL,
    latitude DECIMAL(10,6) NOT NULL,
    longitude DECIMAL(10,6) NOT NULL,
    recorded_at TIMESTAMP NOT NULL,

    FOREIGN KEY (bus_number) REFERENCES bus(bus_number)
);

CREATE TABLE bus_strength (
    strength_id INTEGER PRIMARY KEY,
    bus_number VARCHAR(20) NOT NULL,
    strength_count INTEGER NOT NULL,
    calculation_date DATE NOT NULL,

    FOREIGN KEY (bus_number) REFERENCES bus(bus_number)
);

CREATE TABLE bus_merge_recommendation (
    recommendation_id INTEGER PRIMARY KEY,
    primary_bus VARCHAR(20) NOT NULL,
    merged_bus VARCHAR(20) NOT NULL,
    total_students INTEGER NOT NULL,
    recommendation_date DATE NOT NULL,

    FOREIGN KEY (primary_bus) REFERENCES bus(bus_number),
    FOREIGN KEY (merged_bus) REFERENCES bus(bus_number)
);
