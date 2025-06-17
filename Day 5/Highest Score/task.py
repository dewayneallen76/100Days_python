student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# sum() will give the total of a list of numbers
total_exam_score = sum(student_scores)
print(total_exam_score)

# example of max() using a for loop
student_scores_max = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for student_score_max in student_scores_max:
    if student_score_max > max_score:
        max_score = student_score_max

print(max_score)

# max() or min() will give the highest and lowest numbers
print(max(student_scores))
print(min(student_scores))
