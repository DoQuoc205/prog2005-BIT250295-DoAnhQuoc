numbers = [2, 4, 6, 8, 10]

new_num = int(input("nhập số cần thêm: "))
numbers.append(new_num)

print("danh sách sau khi thêm:", numbers)

k = int(input("nhập giá trị k: "))
count_k = numbers.count(k)
print(f"số {k} xuất hiện {count_k} lần trong danh sách")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

prime_sum = sum(num for num in numbers if is_prime(num))
print("tổng các số nguyên tố trong danh sách =", prime_sum)

numbers.sort()
print("danh sách sau khi sắp xếp:", numbers)
numbers.clear()
print("danh sách sau khi xóa:" , numbers)

