colors = ["Red", "Blue", "Green", "Yellow", "Black"]
try:
    colors.remove("Green")
except ValueError:
    print("Không có màu Green trong danh sách.")
print("Danh sách sau khi xóa:", colors)