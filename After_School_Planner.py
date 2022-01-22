"""
LESSON: 2.4 - While Loops
EXERCISE: After-School Planner
"""
print("Welcome to After-School Planner!")
print("Follow the instructions to find out how to divide you time with activities in your free time in the afternoon!")
#### ---- SETUP ---- ####
print()
# Ask the user how much free time (minutes) they have
# in the afternoon. Typecast to an int and assign it
# to the variable minutes_left
minutes_left = int(input("How many minutes of free time do you have in the afternoon?"))

# Assign an empty string "" to the variable schedule
# ---> TEST AFTER THIS LINE <--- #
schedule = ""


#### ---- MAIN LOOP ---- ####

# WHILE minutes_left remains GREATER THAN 0
while minutes_left > 0:

    #### ---- LOOP INPUT ---- ####

    # Print how many minutes_left the user has
    print(str(minutes_left) + " minutes remaining")

    # Ask the user for an activity. Assign it to the
    # variable activity.
    activity = input("Tell me an activity.")

    # Ask the user how long (minutes) the activity will
    # take. Typecast to an int and assign to minutes
    minutes = int(input("How many minutes will " + activity + " take?"))


    #### ---- CALCULATIONS ---- ####

    # Decrement minutes_left by minutes
    # ---> TEST AFTER THIS LINE <--- #
    minutes_left = minutes_left - minutes

    # Increment schedule by activity
    # ---> TEST AFTER THIS LINE <--- #
    schedule += activity

    # Increment schedule by the string ": "
    schedule += ": "

    # Increment schedule by minutes typecast to a string
    schedule += str(minutes)

    # Increment schedule by the string " minutes"
    schedule += " minutes"

    # Increment schedule by the string "\n"
    # (This creates a new line break)
    # ---> TEST AFTER THIS LINE <--- #
    schedule += "\n"

    # Print an empty line for spacing
    # ---> TEST AFTER THIS LINE <--- #
    print()


#### ---- FINAL OUTPUT ---- ####

# Print the message "Time's up!"
# ---> TEST AFTER THIS LINE <--- #
print("Time's up!")

# Print a blank line
print()

# Print the title "YOUR SCHEDULE"
print("YOUR SCHEDULE")

# Print a line of dashes "--------------"
print("--------------")

# Print schedule
# ---> TEST AFTER THIS LINE <--- #
print("Here is your schedule \n" + schedule)


# Turn in your Coding Exercise.

