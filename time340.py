# Steven Suarez
# CSS 340
# Program 2
# 4/6/2022

import math

class TimeSpan:
    def __init__(self, seconds, minutes, hours):
        if seconds > -60 and seconds < 60:
            self._seconds = seconds
        else:
            self._seconds = 0
        if minutes > -60 and minutes < 60:
            self._minutes = minutes
        else:
            self._minutes = 0
        self._hours = hours
    
    def get_seconds(self):
        return self._seconds
    
    def set_seconds(self, new_seconds):
        if new_seconds > -60 and new_seconds < 60:
            self._seconds = new_seconds
        else:
            self._seconds = 0

    def get_minutes(self):
        return self._minutes

    def set_minutes(self, new_minutes):
        if new_minutes > -60 and new_minutes < 60:
            self._seconds = new_minutes
        else:
            self._minutes = 0

    def get_hours(self):
        return self._hours
    
    def set_hours(self, new_hours):
        self._hours = new_hours
    
