-- =====================================
-- Smart Bus Sync Sample Data
-- =====================================

-- Route

INSERT INTO route (
    route_id,
    route_name,
    starting_point,
    destination
)
VALUES (
    1,
    'Karur Route',
    'Palamala',
    'VCEW'
);

-- Bus

INSERT INTO bus (
    bus_number,
    capacity,
    driver_name,
    driver_phone,
    incharge_name,
    incharge_phone,
    gps_device_id,
    status,
    route_id
)
VALUES (
    'A128',
    50,
    'Kumar',
    '9876543210',
    'Ravi',
    '9876543211',
    'GPS001',
    'Active',
    1
);

-- Bus Stops

INSERT INTO bus_stop (
    stop_id,
    stop_name,
    stop_order,
    route_id
)
VALUES
(1, 'Oil Mill', 1, 1),
(2, 'Valusamipuram', 2, 1),
(3, 'Muniyappan Kovil', 3, 1),
(4, 'KRV Meridien', 4, 1),
(5, 'Polytechnic', 5, 1),
(6, 'Athur', 6, 1),
(7, 'VPM By Pass', 7, 1),
(8, 'VCEW', 8, 1);

-- Students

INSERT INTO student (
    id_number,
    student_name,
    college_name,
    department,
    year,
    rfid_card_number,
    bus_number,
    stop_id
)
VALUES
(
    '22CSE101',
    'Sanjana',
    'VCEW',
    'CSE',
    3,
    'RFID001',
    'A128',
    2
),
(
    '22CSE102',
    'Priya',
    'VCEW',
    'CSE',
    3,
    'RFID002',
    'A128',
    4
),
(
    '22CSE103',
    'Rahul',
    'VCEW',
    'CSE',
    3,
    'RFID003',
    'A128',
    6
);
