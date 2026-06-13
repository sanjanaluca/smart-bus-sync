-- Smart Bus Sync System
-- PostgreSQL Database Schema
-- Version 1
CREATE TABLE route (
    route_id INTEGER PRIMARY KEY,
    route_name VARCHAR(100) UNIQUE NOT NULL,
    starting_point VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL
);
