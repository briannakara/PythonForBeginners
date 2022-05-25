idk = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")

for item in idk.items():
    print(item)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
popped = fast_food_items.pop("McDonald's")
print(popped)

fast_food_items.popitem()
print(fast_food_items)