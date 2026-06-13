SMART BUS SYNC - ER DIAGRAM

Route
│
├── Bus Stop
│
└── Bus
      │
      ├── Student
      │      │
      │      ├── Student Status
      │      │
      │      └── RFID Attendance
      │
      └── GPS Tracking

Relationships:

1 Route -> Many Bus Stops
1 Route -> Many Buses
1 Bus -> Many Students
1 Student -> Many Status Records
1 Student -> Many RFID Records
1 Bus -> Many GPS Records
