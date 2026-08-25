products = {
    101: ["Laptop", "Electronics", 800, 10],
    102: ["Phone", "Electronics", 500, 0],
    103: ["Shoes", "Fashion", 80, 5]
}

print(products[101])

products[101][2] = 750
products[102][3] = 20

for id, p in products.items():
    if p[3] == 0:
        print("Out of stock:", p[0])
