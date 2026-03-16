def average_score(students: dict):
    return sum(students.values()) / len(students)
scores = {"An": 8, "Bình": 7, "Chi": 9}
print("Điểm trung bình:", average_score(scores))