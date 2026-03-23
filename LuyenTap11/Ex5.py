my_dict = {"name": "Quốc", "age": 21, "city":"Hà Nội"}
key = input("Nhập key cần kiểm tra: ")
if key in my_dict:
    print(f"key '{key}' không tồn tại trong dictionary, giá trị là: {my_dict[key]}")
else:
    print(f"key '{key}' không tồn tại trong dictionary")
