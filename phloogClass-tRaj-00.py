# YOU CAN DEVELOP YOUR CODE ELSEWHERE
# AND USE THIS FILE TO TEST YOUR FUNCTION
'''
Program: Dr. Phloog’s Class
Filename:phloogClass-tRaj-00.py
Author:  Tushar Raj
Purpose: Program to calculate grades for Dr. Phloog
         Drops lowest 1 out of every 3 grades and
         computes the letter grade (X < 80%, Z >90%, for Y everyone else)
Revisions: none yet
'''

def findGrade(grades):
    '''
    This function accepts the list of grades and drops the loweset grade out of 3 and computes the average and finally calculates the letter grade based on that
    input: accepts list data type
    output: returns tuple data type
    '''
    exclude_num = len(grades)//3 #to compute the number of grades to exclude, divided by 3 because droping 1 out of 3 grades.
    grades.sort() #Solting the grade list
    new_grade_list = grades[exclude_num::1] #creating a new list by droping the low grades
    add=0 #Initialize the variable with 0
    for i in new_grade_list: #looping through list element to get sum of all the element and stor in add variable
        add+=i
    average=add/len(new_grade_list) #computing the average of new list
    if(average<80): #checking the average is less than 80
        letter = 'X'
    elif(average>90): # checking the average if it is more than 90
        letter = 'Z'
    else:
        letter = 'Y'
    return (average,letter) # THIS RETURNS YOUR RESULTS

'''
DO NOT MODIFY ANY OF THE CODE BELOW
WHEN YOU RUN THE PROGRAM YOUR RESULTS SHOULD BE ...
 80.00 --> Y 
 75.00 --> X 
 91.86 --> Z 
 79.86 --> X 
 85.17 --> Y 

'''
print('Program to calculate grades for Dr. Phloog\n')
# CODE TO TEST THE FUNCTION
grades = []
grades.append([50,100,60]) # [80.00,'Y']
grades.append([50,100,50,50,100,50,50,100,50]) # [75.00,'X']
grades.append([65,100,22,89,0,100,92,78,87,97]) # [91.86,'Z']
grades.append([90,70,60,100,65,95,27,55,79,60]) # [79.86,'X']
grades.append([65,100,22,89,45,92,78,87]) # [85.17,'Y']
for item in grades:
    grade = findGrade(item)
    print(f"{grade[0]:6.2f} --> {grade[1]} ")   
