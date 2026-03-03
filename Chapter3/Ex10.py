nums = list(map(int, input("Nhập danh sách số: ").split()))
evens = [num for num in nums if num % 2 == 0]
print("Các số chẵn:", evens)
print("Tổng các số chẵn:", sum(evens))