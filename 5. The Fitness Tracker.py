#Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

activities_done = []
time_exercising = 0

def input_exercise():
    global activities_done
    global time_exercising

    print("What exercise did you complete?\n1. Dancing\n2. Swimming\n3. Biking\nEnter anything else when done")
    while True:
        response = input()
        try:
            response = int(response)
        except:
            break
        #print(type(response))
        if type(response) == int:
            if 1 <= response <= len(activities):
                activities_done.append(activities[response - 1])
                time_exercising += duration[response - 1]
            else:
                break
        else:
            break

input_exercise()


#Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5

def calorie_calculator():
    print("Total Calories Burned: " + str(time_exercising*3.5))

calorie_calculator()

#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

def summary():
    print(f"List of activities done:\n{activities_done}")
    calorie_calculator()

summary()