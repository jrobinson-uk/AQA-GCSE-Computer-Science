#Get pupil score.
score = int(input("What was the pupils exam score?"))

#Find out the exam grade
if(score >= 36):
    grade = "G"
elif(score >=54):
    grade = "F"
elif(scare >=72):
    grade = "E"
elif(score >=90):
    grade = "D"
elif(score >=108):
    grade = "C"
elif(score >=126):
    grade = "B"
elif(score =144):
    grade = "A"
elif(score >=162):
    grade = "A*"
else:
    grade = "U"


Output the pupil's grade
print("The student's grade is {0}".format(grade))
