cart = {}

def add_product(pid, price, qty):
    if pid in cart:
        cart[pid]["qty"] += qty
    else:
        cart[pid] = {"price": price, "qty": qty}

def remove_product(pid):
    cart.pop(pid, None)

def update_quantity(pid, qty):
    if pid in cart:
        cart[pid]["qty"] = qty

def total():
    return sum(item["price"] * item["qty"] for item in cart.values())

add_product("P1", 100, 2)
add_product("P2", 50, 3)

update_quantity("P1", 4)
remove_product("P2")

print("Total:", total())
