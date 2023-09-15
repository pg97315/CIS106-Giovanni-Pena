#Compute the final score among 2 exam score

print("Enter the score of your first exam: ")
exam_1 = float(input("1st exam: "))
print("")

print("Enter the score of your second exam: ")
exam_2 = float(input("2nd exam: "))
print("")

total = float((exam_1 * .6) + (exam_2 * .4))
print("Your final score is:" , round(total,2))