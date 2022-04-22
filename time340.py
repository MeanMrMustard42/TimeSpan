# Steven Suarez
# CSS 340
# Program 2
# 4/6/2022

import math

class TimeSpan:

    # Initializes TimeSpan object, initially assuming at least one value is positive
    negative_time = False
    def __init__(self, seconds: float = 0, minutes: float = 0, hours: float = 0):
        self.set_time(seconds, minutes, hours)
    

    # Adds together two TimeSpan objects systematically, normalizing as it goes and returning a new TimeSpan object at the end
    def __add__(self, other):
        new_time = TimeSpan(0, 0, 0)
        new_time.set_hours(self._hours + other.get_hours())
        new_time.set_seconds(self._seconds + other.get_seconds())
        while new_time.get_seconds() < -60 or new_time.get_seconds() > 60:
            new_time.normalize_seconds(new_time.get_seconds())
        new_time.set_minutes(self._minutes + other.get_minutes())
        while new_time.get_minutes() < -60 or new_time.get_minutes() > 60:
            new_time.normalize_minutes(new_time._minutes)
        return new_time
    

    # Subtracts two TimeSpan objects systematically, normalizing as it goes and returning a new TimeSpan object at the end
    def __sub__(self, other):
        new_time = TimeSpan(0, 0, 0)
        new_time.set_seconds(self._seconds - other.get_seconds())
        while new_time.get_seconds() < -60 or new_time.get_seconds() > 60:
            new_time.normalize_seconds(new_time.get_seconds())
        new_time.set_minutes(self._minutes - other.get_minutes())
        while new_time.get_minutes() < -60 or new_time.get_minutes() > 60:
            new_time.normalize_minutes(new_time._minutes)
        new_time.set_hours(self._hours - other.get_hours())
        return new_time


    # Uses the same algorithm as __add__ but adds *this* TimeSpan object to another rather than returning a new one
    def __iadd__(self, other):
        self.set_seconds(self._seconds + other.get_seconds())
        if self.get_seconds() < -60 or self.get_seconds() > 60:
            self.normalize_seconds(self.get_seconds())
        self.set_minutes(self._minutes + other.get_minutes())
        if self.get_minutes() < -60 or self.get_minutes() > 60:
            self.normalize_minutes(self._minutes)
        self.set_hours(self._hours + other.get_hours())
        return self

    # Uses the same algorithm as __sub__ but subtracts *this* TimeSpan object from another rather than returning a new one
    def __isub__(self, other):
        self.set_seconds(self._seconds - other.get_seconds())
        if self.get_seconds() < -60 or self.get_seconds() > 60:
            self.normalize_seconds(self.get_seconds())
        self.set_minutes(self._minutes - other.get_minutes())
        if self.get_minutes() < -60 or self.get_minutes() > 60:
            self.normalize_minutes(self._minutes)
        self.set_hours(self._hours - other.get_hours())
        return self

    # Unary negation operator - each time value is flipped and this TimeSpan object is returned.
    def __neg__(self):
        negative_time = TimeSpan(-self._seconds, -self._minutes, -self._hours)
        return negative_time
    
    # Determines if this TimeSpan object is less than another TimeSpan object by checking each individual time value.
    def __lt__(self, other):
        if self._hours < other.get_hours():
            return True
        elif self._minutes < other.get_minutes():
            return True
        elif self._seconds < other.get_seconds():
            return True
        else:
            return False

    # Determines if this TimeSpan object is greater than another TimeSpan object by checking each individual time value.
    def __gt__(self, other):
        if self._hours > other.get_hours():
            return True
        elif self._minutes > other.get_minutes():
            return True
        elif self._seconds > other.get_seconds():
            return True
        else:
            return False
    
    # Determines if this TimeSpan object is less than or equal to another TimeSpan object by checking each individual time value.
    def __le__(self, other):
        if self._hours <= other.get_hours():
            return True
        elif self._minutes <= other.get_minutes():
            return True
        elif self._seconds <= other.get_seconds():
            return True
        else:
            return False
    
# Determines if this TimeSpan object is greater than or equal to another TimeSpan object by checking each individual time value.
    def __ge__(self, other):
        if self._hours >= other.get_hours():
            return True
        elif self._minutes >= other.get_minutes():
            return True
        elif self._seconds >= other.get_seconds():
            return True
        else:
            return False

    # Determines inequality of this TimeSpan object to another.
    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
    
    # Determines equality of this TimeSpan object to another.
    def __eq__(self, other):
        if self._seconds == other.get_seconds() and self._minutes == other.get_minutes() and self._hours == other.get_hours():
            return True
        else:
            return False

    # Returns a string representation of this TimeSpan object.
    def __str__(self):
        return "Hours: " + str(self._hours) + ", Minutes: " + str(self._minutes) + ", Seconds: " + str(self._seconds)
    
    # Normalizes the minutes value after it is passed in. Values higher than 60 will "spill over" into the hours value.
    def normalize_minutes(self, minutes):
        leftover = divmod(minutes, 60)
        self._hours += int(leftover[0])
        self._minutes = leftover[1]
        partial_value = minutes % 1
        self._minutes -= int((partial_value))
        self._seconds += int((partial_value * 60))
        while self._seconds < -60 or self._seconds > 60:
            self.normalize_seconds(self._seconds)

        partial_value = self._hours % 1
        self._hours -= (partial_value) # doing it for hours too
        self._minutes += (partial_value * 60)
        return self._minutes

    
# Normalizes the seconds value after it is passed in. Values higher than 60 will "spill over" into the minutes value.
    def normalize_seconds(self, seconds):
        leftover = divmod(seconds, 60)
        self._minutes += int(leftover[0]) # seconds can't be floats but won't be overflowed either
        self._seconds = leftover[1]
        self._seconds = int(round(self._seconds))
        return self._seconds


    # Sets the TimeSpan object to the desired values but also checks for legitimacy before saving those values.
    # Negative values are handled appropriately and any non-numeric input is not accepted and will default to 0.
    def set_time(self, seconds, minutes, hours):
        try:
            if(seconds == int or seconds == 0):
                self._seconds = int(seconds)
            else:
                self._seconds = float(seconds)
        except:
            self._seconds = 0
            seconds = 0
        try:
            if(minutes == int or minutes == 0):
                self._minutes = int(minutes)
            else:
                self._minutes = float(minutes)
        except:
            self._minutes = 0
            minutes = 0
        try:
            if(hours == int or hours == 0):
                self._hours = int(hours)
            else:
                self._hours = float(hours)
        except:
            self._hours = 0
            hours = 0

        self.take_in_this_mess(self._seconds, self._minutes, self._hours)


    def is_legitimate(self):
        abs_value = abs(self._seconds) + abs(self._minutes) + abs(self._hours)
        test_value = self._seconds + self._minutes + self._hours
        if abs_value != test_value:
            return False
        if(self._seconds < - 60 or self._seconds > 60):
            return False
        elif (self._minutes < -60 or self._minutes > 60):
            return False
        return True


    def take_in_this_mess(self, seconds, minutes, hours):

       total_time = ((seconds) + (minutes * 60) + (hours * 60 * 60))
       time_in_seconds = total_time/60
       new_seconds = divmod(total_time, 60)
       self._seconds = int(new_seconds[1])

       time_in_minutes = time_in_seconds/60
       new_minutes = divmod(time_in_seconds, 60)
       self._minutes = int(new_minutes[1])
       if time_in_seconds < 0:
           self._minutes = -self._minutes
       if time_in_seconds % 1  == 0 and time_in_seconds > -60 and time_in_seconds < 60:
           self._minutes = time_in_seconds
       
       self._hours = int(time_in_minutes)
       #self._minutes += (time_in_minutes % 1 * 60) # doing it here
       print("FUCC")
       


    # Accounts for any negative numbers in a TimeSpan object by setting them to 0 and subtracting the value
    # from the other appropriate values.
    def accountForNegatives(self):
        if self._seconds < 0 and self.negative_time == False:
            while self._seconds <= -59:
                minutes_rebalance = int(self._minutes/60)
                seconds_rebalance = float(((self._seconds/60) % 1) * 60)
                self._minutes += minutes_rebalance
                self._seconds = seconds_rebalance
        if self._hours < 0 and self.negative_time == False:
            hours_offset = self._hours * 60
            self._hours = 0
            self._minutes += hours_offset # doesn't matter if self._minutes goes below 0 here bc that is immediately corrected for
            
            while self._minutes < -60:
                hours_rebalance = int(self._minutes/60)
                minutes_rebalance = float(((self._minutes/60) % 1) * 60)
                self._hours += hours_rebalance
                self._minutes = minutes_rebalance
                if(self._hours < 0): # change minutes to negative if hours is still 0
                    self._minutes = -self._minutes
        

        if self._minutes < 0 and self._seconds > 0:
            minutes_offset = self._minutes * 60
            self._minutes = 0
            if(self._seconds - minutes_offset < 0):
                self._minutes = 0
            else:
                self._seconds += minutes_offset # adding bc minutes_offset should always be negative

            return self

    # Returns number of seconds in this TimeSpan object.
    def get_seconds(self):
        return int(self._seconds)
    
    # Sets number of seconds in this TimeSpan object.
    def set_seconds(self, new_seconds):
        try:
            if(new_seconds == int or new_seconds == 0):
                self._seconds = int(new_seconds)
            else:
                self._seconds = float(new_seconds)
        except:
            self._seconds = 0
            new_seconds = 0
        if new_seconds < -60 and new_seconds > 60:
            self.normalize_seconds(new_seconds)
        else:
            self._seconds = new_seconds
        self.accountForNegatives()


    # Returns number of minutes in this TimeSpan object.
    def get_minutes(self):
        return int(self._minutes)

    # Sets number of minutes in this TimeSpan object.
    def set_minutes(self, new_minutes):
        try:
            if(new_minutes == int or new_minutes == 0):
                self._minutes = int(new_minutes)
            else:
                self._minutes = float(new_minutes)
        except:
            self._minutes = 0
            new_minutes = 0
        if new_minutes < -60 and new_minutes > 60:
            self.normalize_minutes(new_minutes)
        else:
            self._minutes = int(new_minutes)
        self.accountForNegatives()


    # Returns number of hours in this TimeSpan object.
    def get_hours(self):
        return int(self._hours)
    
    # Sets number of hours in this TimeSpan object.
    def set_hours(self, new_hours):
        try:
            if(new_hours == int or new_hours == 0):
                self._hours = int(new_hours)
            else:
                self._hours = float(new_hours)
        except:
            self._hours = 0
            new_hours = 0
        self.accountForNegatives()


