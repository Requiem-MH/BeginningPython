#Prompt User for Points Earned

homework = eval(input("Please enter how many points earned for homework, out of 150: "))
exam = eval(input("Please enter how many points earned for exam, out of 250: "))
recitation = eval(input("Please enter how many points earned for recitation, out of 75: "))

#Calculate Score and Percent
TOTAL = 475
score = (homework + exam + recitation)
percent = ((homework + exam + recitation) / TOTAL) * 100

#Display Final Score and Percentage in class
print("\nTotal points out of 475: ", score)
print("Final Percentage: ", int(percent), "%")
