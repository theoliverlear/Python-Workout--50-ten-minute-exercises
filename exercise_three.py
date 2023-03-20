# Oliver Sigwarth
# Exercise 3: Run Timing
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/19/2023
# Modified: 3/19/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a function (run_timing) that asks how long it took for you to run 10km and will continue to ask until the user
# presses Enter. Then, the function shows the average time and exits.
def run_timing():
    end_loop = False
    run_times = []
    total_time = 0
    total_runs = 0
    while not end_loop:
        print("Please press the Enter key when you have added all of your runs...")
        temp_run_times = input("Please enter the amount of time (in minutes) it took for you to run 10 kilometers: ")
        if temp_run_times == "":
            end_loop = True
        else:
            run_times.append(temp_run_times)
    for time in run_times:
        total_time += float(time)
        total_runs += 1
    average_time = total_time / int(total_runs)
    average_time_rounded = round(average_time, 2)
    print("Your average 10km run was " + str(average_time_rounded) + " minutes.")
run_timing()