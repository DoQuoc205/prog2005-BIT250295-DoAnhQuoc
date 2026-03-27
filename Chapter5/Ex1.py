import matplotlib.pyplot as plt

score = {"xuất sắc": 6, "Giỏi": 10, "Trung bình": 12, "Yếu": 4, "Kém": 1}

sorted_score = dict(sorted(score.items(), key=lambda item: item[1], reverse=True))

names = list(sorted_score.keys())
areas = list(sorted_score.values())

plt.barh(names, areas, color='skyblue')
plt.xlabel("Số học sinh đạt thành tích")
plt.title("Kết quả học tập của lớp 12b5 (giảm dần)")
plt.gca().invert_yaxis()

plt.show()
