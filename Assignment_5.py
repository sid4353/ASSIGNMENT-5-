# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


students = {'Alice': 85,'Bob': 78,'Charlie': 92,'rohan':89,'disha':78}
Stu=input("Enter the student's name:")
if Stu in students:
    m=(students[Stu])
    print(Stu+"'s","marks:",m)
else:
    print('student not found')


# Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

l=list(range(0,11))
print('original list: ',l)

Ex=l[5:11]
print('Extracted first five element:',Ex)
re= Ex[-1:-7:-1]

print('Reversed extracted elements:',re)


