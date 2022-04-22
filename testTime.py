# 35 points for correctness
# First set of tests are those published as part of program

import time340

total_points = 0
def compare(time_span, hours, minutes, seconds, test_case, points = 1):
    global total_points
    if time_span.get_seconds() == seconds and time_span.get_minutes() ==  minutes and time_span.get_hours() == hours:
        total_points += points
        print("Test Case", test_case, "PASSED. Total Points =", total_points)
        return True
    else:
        print("Test Case", test_case, "FAILED. Total Points = ", total_points)
        return False
#Published test case #1
t1 = time340.TimeSpan(3.1, 7)
compare(t1, 0, 7, 3, 1)
#Published test case #2
t2 = time340.TimeSpan(74, -5, 8)
compare(t2, 7, 56, 14, 2)
#Published test case #3
t3 = t1 + t2
compare(t3, 8, 3, 17, 3)
#Published test case #4, 5
t2 += t1
compare(t2, 8, 3, 17, 4)
compare(t1, 0, 7, 3, 5)
#Published test case #6, 7
t3 = -t2
compare(t2, 8, 3, 17, 6)
compare(t3, -8, -3, -17, 7)
#Published test case 8
t5 = time340.TimeSpan()
t5.set_time(6, 5, 8)
compare(t5, 8, 5, 6, 8)
#Published test case 9
t4 = time340.TimeSpan(6,7,8)
if t4 >= t5:
    total_points += 1
    print("Test Case", 9, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 9, "FAILED. Total Points =", total_points)
#Published test case 10
t6 = time340.TimeSpan(9, 78, -7)
t6 = -t6
compare(t6, 5, 41, 51, 10, 1)
#FOLLOWING TEST CASES NOT PUBLISHED IN DOCUMENT
#test case 11
if t4 != t5:
    total_points += 1
    print("Test Case", 11, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 11, "FAILED. Total Points =", total_points)
#test case 12
t4 = time340.TimeSpan(1, 2, 3)
t5 = time340.TimeSpan(1, 2, 3)
if t4 == t5:
    total_points += 1
    print("Test Case", 12, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 12, "FAILED. Total Points =", total_points)
#test case 13, 14, 15
t1 = time340.TimeSpan(60) # 00:01:00
compare(t1, 0, 1, 0, 13, 2)
t2 = time340.TimeSpan(-60, 60) # 00:59:00
compare(t2, 0, 59, 0, 14, 2)
t3 = time340.TimeSpan(0, 180, -2) # 01:00:00
compare(t3, 1, 0, 0, 15, 2)
#test case 16, 17
t4 = time340.TimeSpan(0)
t4.set_time(0, 1, 0)
compare(t1, 0, 1, 0, 16, 2)
if t1 == t4:
    total_points += 1
    print("Test Case", 17, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 17, "FAILED. Total Points =", total_points)
# test case 18, 19
t1 = time340.TimeSpan(5, 5, 5)
t2 = time340.TimeSpan(4, 4, 4)
t3 = time340.TimeSpan(9, 9, 9)
if t1 + t2 == t3:
    total_points += 2
    print("Test Case", 18, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 18, "FAILED. Total Points =", total_points)
if t1 == t3 - t2:
    total_points += 2
    print("Test Case", 19, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 19, "FAILED. Total Points =", total_points)
#Test Case 20
t1 = time340.TimeSpan(0, 1)
t4 = time340.TimeSpan(0, -1)
if -t1 == t4:
    total_points += 2
    print("Test Case", 20, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 20, "FAILED. Total Points =", total_points)
#Test Case 21 - 
t1 = time340.TimeSpan(1, -1, 1)
t2 = time340.TimeSpan(2, -3, 4)
# Test not equal operator
if t1 != t2:
    total_points += 1
    print("Test Case", 21, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 21, "FAILED. Total Points =", total_points)
if t2 > t1:
    total_points += 1
    print("Test Case", 22, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 22, "FAILED. Total Points =", total_points)
if t2 >= t1:
    total_points += 1
    print("Test Case", 23, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 23, "FAILED. Total Points =", total_points)
if t1 >= t1:
    total_points += 1
    print("Test Case", 24, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 24, "FAILED. Total Points =", total_points)
if t1 < t2:
    total_points += 1
    print("Test Case", 25, "PASSED. Total Points =", total_points)
else:
    print("Test Case", 25, "FAILED. Total Points =", total_points)
#Test Case 26, 27, 28
t1 = time340.TimeSpan(45) # 00:0:45
compare(t1, 0, 0, 45, 26)
t2 = time340.TimeSpan(-59, 59) # 00:58:01
compare(t2, 0, 58, 1, 27)
t3 = time340.TimeSpan(0, 30, -2) # -01:30:00
compare(t3, -1, -30, 0, 28)
# Print out the final test grade
print("FINAL SCORE:", total_points)