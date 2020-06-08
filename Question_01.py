# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1


# ----| Functions |--------------------------------------------------------------------------------------------------- #

def write_student_to_file(all_students):
    """Prints/Outputs student information to ('output.txt': text file)"""
    file = open("output.txt", "w")
    student_num = 1
    
    for student in all_students:
        firstName = student[0]
        lastName = student[1]

        file.write("{ID}) {} {}".format(student_num, firstName, lastName))
        file.write("Average score: {}".format(avgScore))
        file.write("{ID}) {} {}".format(student_num, firstName, lastName))
        file.write("{ID}) {} {}".format(student_num, firstName, lastName))
        file.write("{ID}) {} {}".format(student_num, firstName, lastName))
    

def process_raw_line(line_to_process):
    """Removes colon and commas from (line_to_process: str). Returns list delimited by SPACE(' ')."""
    processed_line = line_to_process                                            # "line_to_process" is immutable
    
    processed_line = processed_line.replace(':', '')                            # Remove the colon (':')
    processed_line = processed_line.replace(",", "")                            # Remove the commas (',')
    
    return processed_line.split()                                               # Return as individual words


def find_high_score(all_scores):
    """Returns highest score within the sublist passed-in"""
    high_score = 0.0
    
    for score in all_scores:
        if score > high_score:
            high_score = score
    
    return high_score


def find_low_score(all_scores):
    """Returns lowest score within the sublist passed-in"""
    low_score = 0.0
    
    for score in all_scores:
        if score < low_score:
            low_score = score
    
    return low_score


def calculate_average_score(all_scores):
    """Returns average score"""
    scores_subtotal = 0
    num_of_scores = len(all_scores)
    
    for score_value in all_scores:
        scores_subtotal += score_value
    
    return scores_subtotal / num_of_scores


def convert_to_letter_grade(score):
    """Returns the letter grade for (score: float)"""
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    elif score >= 50.0:
        return 'E'
    else:
        return 'F'
    
    
# ----| main |-------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    students = []                                                               # List of students
    data = []                                                                   # List for each line of the file
    ID = 0                                                                      # X-axis controller for (students: list)
    
    fileInStream = open("input.txt", 'r')                                       # Open the file in read mode
    
    for raw_line in fileInStream:
        student = process_raw_line(raw_line)                                    # Remove unwanted characters
        
        firstName = student[0]
        lastName = student[1]
        avgScore = calculate_average_score(student[2:7])
        highScore = find_high_score(student[2:7])
        lowScore = find_low_score(student[2:7])
        letterGrade = convert_to_letter_grade(avgScore)

        students[ID][0] = firstName
        students[ID][1] = lastName
        students[ID][2] = avgScore
        students[ID][3] = highScore
        students[ID][4] = letterGrade
        
        ID = ID + 1
    
    for student in students:
        write_student_to_file(student)