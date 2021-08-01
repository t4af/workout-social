print("Hello World!")

exercise = ("Bicep Curls", 3)
exercises = [("Bicep Curls", 3), ("Tricep Curls", 4)]

numberOfExercises = input("How many exercises are you gonna do?\n")
numberOfExercises = int(numberOfExercises)
for x in range(0,numberOfExercises):
    exercise = input("What exercise?\n")

    numOfReps = input("How many reps did you do?\n")
    answer = int(numOfReps)
    answer = answer * 2
    print("You did " + str(exercise) + (" and got ") + str(answer) + " points")