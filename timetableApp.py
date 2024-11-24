Below is the translated Python code for the `timetableApp.java` file:

```python
from datetime import time, timedelta
from enum import Enum
import logging

from ortools.sat.python import cp_model

class DemoData(Enum):
    SMALL = 1
    LARGE = 2

class Timeslot:
    def __init__(self, timeslot_id, day_of_week, start_time, end_time):
        self.timeslot_id = timeslot_id
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

class Room:
    def __init__(self, room_id, name):
        self.room_id = room_id
        self.name = name

class Lesson:
    def __init__(self, lesson_id, subject, teacher, student_group):
        self.lesson_id = lesson_id
        self.subject = subject
        self.teacher = teacher
        self.student_group = student_group

class Timetable:
    def __init__(self, name, timeslots, rooms, lessons):
        self.name = name
        self.timeslots = timeslots
        self.rooms = rooms
        self.lessons = lessons

class TimetableApp:
    
    LOGGER = logging.getLogger('TimetableApp')

    @staticmethod
    def generate_demo_data(demo_data):
        timeslots = []
        next_timeslot_id = 0
        timeslots.append(Timeslot(next_timeslot_id, "MONDAY", time(8, 30), time(9, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "MONDAY", time(9, 30), time(10, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "MONDAY", time(10, 30), time(11, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "MONDAY", time(13, 30), time(14, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "MONDAY", time(14, 30), time(15, 30)))
        next_timeslot_id += 1

        timeslots.append(Timeslot(next_timeslot_id, "TUESDAY", time(8, 30), time(9, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "TUESDAY", time(9, 30), time(10, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "TUESDAY", time(10, 30), time(11, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "TUESDAY", time(13, 30), time(14, 30)))
        next_timeslot_id += 1
        timeslots.append(Timeslot(next_timeslot_id, "TUESDAY", time(14, 30), time(15, 30)))
        next_timeslot_id += 1

        if demo_data == DemoData.LARGE:
            timeslots.append(Timeslot(next_timeslot_id, "WEDNESDAY", time(8, 30), time(9, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "WEDNESDAY", time(9, 30), time(10, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "WEDNESDAY", time(10, 30), time(11, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "WEDNESDAY", time(13, 30), time(14, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "WEDNESDAY", time(14, 30), time(15, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "THURSDAY", time(8, 30), time(9, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "THURSDAY", time(9, 30), time(10, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "THURSDAY", time(10, 30), time(11, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "THURSDAY", time(13, 30), time(14, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "THURSDAY", time(14, 30), time(15, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "FRIDAY", time(8, 30), time(9, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "FRIDAY", time(9, 30), time(10, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "FRIDAY", time(10, 30), time(11, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "FRIDAY", time(13, 30), time(14, 30)))
            next_timeslot_id += 1
            timeslots.append(Timeslot(next_timeslot_id, "FRIDAY", time(14, 30), time(15, 30)))
            next_timeslot_id += 1

        rooms = []
        next_room_id = 0
        rooms.append(Room(next_room_id, "Room A"))
        next_room_id += 1
        rooms.append(Room(next_room_id, "Room B"))
        next_room_id += 1
        rooms.append(Room(next_room_id, "Room C"))
        next_room_id += 1

        if demo_data == DemoData.LARGE:
            rooms.append(Room(next_room_id, "Room D"))
            next_room_id += 1
            rooms.append(Room(next_room_id, "Room E"))
            next_room_id += 1
            rooms.append(Room(next_room_id, "Room F"))
            next_room_id += 1

        lessons = []
        next_lesson_id = 0
        lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Physics", "M. Curie", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Chemistry", "M. Curie", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Biology", "C. Darwin", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "History", "I. Jones", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "English", "I. Jones", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "English", "I. Jones", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Spanish", "P. Cruz", "9th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Spanish", "P. Cruz", "9th grade"))
        next_lesson_id += 1

        if demo_data == DemoData.LARGE:
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "ICT", "A. Turing", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physics", "M. Curie", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Geography", "C. Darwin", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Geology", "C. Darwin", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "History", "I. Jones", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "English", "I. Jones", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Drama", "I. Jones", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Art", "S. Dali", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Art", "S. Dali", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "9th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "9th grade"))
            next_lesson_id += 1

        lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Physics", "M. Curie", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Chemistry", "M. Curie", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "French", "M. Curie", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Geography", "C. Darwin", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "History", "I. Jones", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "English", "P. Cruz", "10th grade"))
        next_lesson_id += 1
        lessons.append(Lesson(next_lesson_id, "Spanish", "P. Cruz", "10th grade"))
        next_lesson_id += 1

        if demo_data == DemoData.LARGE:
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "ICT", "A. Turing", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physics", "M. Curie", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Biology", "C. Darwin", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Geology", "C. Darwin", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "History", "I. Jones", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "English", "P. Cruz", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "English", "P. Cruz", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Drama", "I. Jones", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Art", "S. Dali", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Art", "S. Dali", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "10th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "10th grade"))
            next_lesson_id += 1

            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "ICT", "A. Turing", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physics", "M. Curie", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Chemistry", "M. Curie", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "French", "M. Curie", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physics", "M. Curie", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Geography", "C. Darwin", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Biology", "C. Darwin", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Geology", "C. Darwin", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "History", "I. Jones", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "History", "I. Jones", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "English", "P. Cruz", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "English", "P. Cruz", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "English", "P. Cruz", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Spanish", "P. Cruz", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Drama", "P. Cruz", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Art", "S. Dali", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Art", "S. Dali", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "11th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Physical education", "C. Lewis", "11th grade"))
            next_lesson_id += 1

            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "12th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "12th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "12th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "12th grade"))
            next_lesson_id += 1
            lessons.append(Lesson(next_lesson_id, "Math", "A. Turing", "12th grade"))
            next_lesson_id += 1
