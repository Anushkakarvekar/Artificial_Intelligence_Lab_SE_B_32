print(" Develop the decision making using if else in python.")
student_likes1= str(input("enter the name of subject 1="))
student_likes2= str(input("enter the name of subject 2="))
if (student_likes1=="Maths" and student_likes2=="Physics"):
	print("Mechanical Engineering")
elif (student_likes1 == "Programming" and student_likes2== "Maths"):
	print("Computer Engineering")
elif (student_likes1 == "Biology" and student_likes2 == "Chemistry"):
	print("Biotechnology")
elif (student_likes1 == "Circuits" and student_likes2== "Maths"):
	 print("Electronics Engineering")
elif (student_likes1 == "Programming" and student_likes2== "Statistics"):
	print ("Artificial Intelligence and Data Science")
elif (student_likes1 == "Programming" and student_likes2 == "AI Concepts"):
	print("Artificial Intelligence and Machine Learning Engineering")
else:
	print("invalid subject name")
