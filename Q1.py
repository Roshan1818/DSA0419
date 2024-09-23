import numpy as np
student_scores = np.array([[85, 90, 78, 92],
                           [88, 76, 85, 80],
                           [92, 88, 94, 89],
                           [75, 85, 80, 78]])
average_scores = np.mean(student_scores, axis=0)
highest_avg_index = np.argmax(average_scores)
subjects = ["Math", "Science", "English", "History"]
print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", subjects[highest_avg_index])
