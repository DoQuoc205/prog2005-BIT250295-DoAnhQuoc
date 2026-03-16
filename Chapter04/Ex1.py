def analyze_tuple(numbers: tuple):
    return {"Tổng": sum(numbers),
        "Lớn nhất": max(numbers),
        "Nhỏ nhất": min(numbers)}

print(analyze_tuple((1, 5, 3, 9, -2)))