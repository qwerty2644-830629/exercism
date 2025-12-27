"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    # student_scores : score of student (學生的分數)
    new_scores = [] # round score (大約分數)
    
    for i in student_scores:
        new_scores.append(round(i))

    return new_scores

def count_failed_students(student_scores):
    # student_scores : score of student (學生的分數)
    num_fail = 0 # number of fail student (不及格學生數)
    
    for i in student_scores:
        if i <= 40:
            num_fail += 1

    return num_fail

def above_threshold(student_scores, threshold):
    # student_scores : score of student (學生的分數)
    good_student = [] # abrove threshold student (超過門檻學生)
    
    for i in student_scores:
        if i >= threshold:
            good_student.append(i)

    return good_student

def letter_grades(highest):
    # highest : the highest score (最高分數)
    lowest = 40 # the low score (最低分數)
    list = []
    i = 0
    while i < 1:
        score = int((highest - lowest) * i)
        list.append(lowest + score +1)
        i += 0.25

    return list

def student_ranking(student_scores, student_names):
    # student_scores : student score (學生分數)
    # student_naems : student name (學生名字)
    new_list = [] # (新列表)

    for index, name in enumerate(student_names):
        string = str(index+1) + '. ' + name + ': ' + str(student_scores[index]) # (格式)
        new_list.append(string)

    return new_list

def perfect_score(student_info):
    # student_info : student name and score (學生的分數和名字)
    perfect = []
    for i in student_info:
        if i[1] == 100:
            perfect = i 
            break

    return perfect
    
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    pass
