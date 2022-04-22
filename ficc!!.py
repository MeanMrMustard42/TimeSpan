
def takeInThisMess(seconds, minutes, hours):
    totalTime = ((seconds) + (minutes * 60) + (hours * 60 * 60))
    time_in_seconds = totalTime/60
    new_seconds = divmod(totalTime, 60)
    seconds = int(new_seconds[1])

    time_in_minutes = time_in_seconds/60
    new_minutes = divmod(time_in_seconds, 60)
    minutes = int(new_minutes[1])

    time_in_hours = time_in_minutes/60
    new_hours = divmod(time_in_minutes, 60)
    hours = int(new_hours[1])
    print("fucc?")



takeInThisMess(12, 24, 5)
