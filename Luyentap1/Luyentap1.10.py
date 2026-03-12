class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def to_file_format(self):
        return f"{self.code};{self.name};{self.price}"
def add_product_to_file(product, filename="products.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(product.to_file_format() + "\n")
def read_products(filename="products.txt"):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            code, name, price = line.strip().split(";")
            products.append(Product(code, name, float(price)))
    return products
def display_products(products):
    for p in products:
        print(f"{p.code} - {p.name} - {p.price}")
def sort_products_desc(products):
    return sorted(products, key=lambda x: x.price, reverse=True)
p1 = Product("sp1", "Cocacolala", 15.5)
p2 = Product("sp2", "Bưởi 5 Roi", 18.0)
p3 = Product("sp3", "Bia 333", 14.5)
products = read_products()
print("Danh sách sản phẩm:")
display_products(products)
print("\nSắp xếp theo giá giảm dần:")
sorted_products = sort_products_desc(products)
display_products(sorted_products)