"""
Program: validation_with_try.py
Author: Michael Moore
Last Date Modified: 9/20/20

This program takes 3 tests input and return and average of them throws ValueError with negative inputs.
"""
NUMBER_TESTS = 3
def average(score1,score2,score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError


    return float((score1 + score2 + score3) / NUMBER_TESTS)

if __name__ == '__main__':
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    age = int(input("Enter Age: "))
    first_score = int(input("Enter your first score: "))
    second_score = int(input("Enter your second score: "))
    third_score = int(input("Enter your third score: "))
    try:
        average_scores = average(first_score,second_score,third_score)
    except ValueError:
        print("Enter only positive scores!")
    else:
        print(f"{last_name}, {first_name} age: {age}", "average grade: {:.2f}".format(average_scores))


#input 1 Moore,Michael,22,99,99,94 output 1 Moore, Michael age: 22 average grade: 97.33
#input 2 Moore,Michael,22,87,56,34 output 2 Moore, Michael age: 22 average grade: 59.00
#input 3 Moore,Michael,22,96,88,82 output 3 Moore, Michael age: 22 average grade: 88.67
