def normalize_name(name: str) -> str:
    return " ".join(word.capitalize() for word in name.strip().split())

name = input("Nhập tên: ")
print("Tên chuẩn hóa:", normalize_name(name))