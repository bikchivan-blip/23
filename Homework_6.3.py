warehouse = {
    "цукор": {"price": 30, "qty": 100},
    "борошно": {"price": 25, "qty": 150},
    "сіль": {"price": 15, "qty": 200},
}

order = {}

def add_to_order(item, qty):
  if item in warehouse and warehouse[item]["qty"] >= qty:
    order[item] = order.get(item, 0) + qty
    warehouse[item]["qty"] -= qty


add_to_order("цукор", 10)
add_to_order("сіль", 20)

total_cost = sum(order[i] * warehouse[i]["price"] for i in order)
print("Загальна вартість замовлення:", total_cost)

if order:
  max_qty = max(order.values())
  max_items = [i for i, q in order.items() if q == max_qty]
  print("Товар(и) з найбільшою кількістю у замовленні:", max_items)

  min_price = min(warehouse[i]["price"] for i in order)
  min_price_items = [i for i in order if warehouse[i]["price"] == min_price]
  print("Товар(и) з найменшою ціною у замовленні:", min_price_items)