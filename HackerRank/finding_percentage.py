# -*- coding: utf-8 -*-
"""
finding_percentage.py

HackerRank challenge ' Finding the percentage'

The provided code stub will read in a dictionary containing key/value 
pairs of name:[marks] for a list of students. Print the average of the
 marks array for the student name provided, showing 2 places after the 
 decimal. 
 
"""
if __name__ == '__main__':
    print("hello")
    n= int(input('Enter n >'))
    
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter input >").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter query >" )