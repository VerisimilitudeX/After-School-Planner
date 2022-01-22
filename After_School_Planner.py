print("Welcome to After-School Planner!")
print("Follow the instructions to find out how to divide you time with activities in your free time in the afternoon!")
print()

minutes_left = int(input("How many minutes of free time do you have in the afternoon?"))

schedule = ""

while minutes_left > 0:

    print(str(minutes_left) + " minutes remaining")

    activity = input("Tell me an activity.")

    minutes = int(input("How many minutes will " + activity + " take?"))


    minutes_left = minutes_left - minutes

    schedule += activity

    schedule += ": "

    schedule += str(minutes)

    schedule += " minutes"

    schedule += "\n"

    print()

print("Time's up!")

print()

print("YOUR SCHEDULE")

print("--------------")

print("Here is your schedule \n" + schedule)
