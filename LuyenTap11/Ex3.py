numbers = list(map(int, input("Nhập danh sách số: ").split()))

even_numbers = [num for num in numbers if num % 2 == 0]

sum_even = sum(even_numbers)

print("Các số chẵn là:", even_numbers)
print("Tổng các số chẵn =", sum_even)
