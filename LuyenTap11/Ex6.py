
people = {}
n = int(input("Nhập số lượng người: "))
for i in range(n):
    name = input(f"Nhập tên người thứ {i+1}: ")
    age = int(input(f"Nhập tuổi của {name}: "))
    people[name] = age

print("Danh sách ban đầu:", people)

average_age = sum(people.values()) / len(people)
print("Tuổi trung bình =", average_age)

items = list(people.items())

for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]

sorted_people = dict(items)
print("Danh sách sau khi sắp xếp theo tuổi giảm dần:", sorted_people)

people.clear()
print("Danh sách sau khi xóa:", people)
