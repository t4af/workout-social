#print("Hello World!")

e1 = "Bicep Curls"
e2 = "Tricep Extensions"
e3 = "Bench Press"

numberOfExercises = input("How many exercises are you going to do?\n")
numberOfExercises = int(numberOfExercises)

exercises = []
Points = []
x = False
count = 0

while x is False:
    print(e1 + "," + e2 + "," + e3)
    exerciseNum = input("What exercises? Please input 1 for Bicep Curls, 2 for Tricep Extensions, and 3 for Bench Press\n")
    exerciseNum = int(exerciseNum)

    if exerciseNum > 3 or exerciseNum < 1:
        print("Input Invalid please try again")
        continue
    if exerciseNum == 1:    # if I hit 1 (Bicep Curl)
        exercise = e1
    elif exerciseNum == 2:  # if I hit 2 (Tricep Extensions)
        exercise = e2
    elif exerciseNum == 3:  # if I hit 3 (Bench Press)
        exercise = e3

    exercises.append(exercise)  #adding exercise to array
    count = count + 1

    numOfReps = input("How many reps did you do?\n")
    answer1 = int(numOfReps)
    if int(numOfReps) < 10:
        answer1 = answer1 * 1.5
    elif int(numOfReps) >= 10:
        answer1 = answer1 * 2

    if int(numberOfExercises) >= 4:
        answer1 = answer1 * 2

    Points.append(answer1)  #adding points to array

    if(count == numberOfExercises):     #when count hits numberOfExercises
        x = True



for x in range(0, numberOfExercises):
    print("You did " + exercises[x] + (" and got ") + str(Points[x]) + " points")









