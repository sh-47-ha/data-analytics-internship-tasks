marks = {}

print("1 : Maths\n" "2 : Physics\n" "3 : Chemistry")
for i in range(1,4):
    stu_name = input("Enter your name: ")
   
    mark = []   #new line for each student

    for k in range(1,4):                        
        mark_sub = int(input("Enter you mark :"))
        mark.append(mark_sub)                      # store mark in list

    marks.update({stu_name: mark})         #Store each student’s marks in a dictionary
print(f"\n{marks}\n")


#Average marks of student

for stu_name in marks:
    avg = round(sum(marks[stu_name])/3, 1)
    print(f"{stu_name}--> Average: {avg}")


# Find topper

max_total = 0
topper = ""
for stu_name in marks:
    total = sum(marks[stu_name])
    if total > max_total:
        max_total = total
        topper = stu_name
print(F"\nTopper: {topper} with {total} marks\n")        


#Subject-wise Average

subjects = ["Maths", "Physics", "Chemistry"]

for j in range(3):
    sub_avg = 0

    for i in marks:
        sub_avg += marks[i][j]

    avg = round(sub_avg / len(marks),1)
    print(subjects[j], "Average =", avg)   


