# common operations
basket_a = {"apple", "banana", "kiwi", "plum", "apple", "orange", "banana"}
basket_b = {"grapes", "water melon", "kiwi", "apple", "guava"}

print(type(basket_a))

print("basket_a | basket_b", basket_a | basket_b)  # union
print("basket_a & basket_b", basket_a & basket_b)  # intersection
print("basket_a ^ basket_b", basket_a ^ basket_b)  # sym diffe (uncommon)
print("basket_a - basket_b", basket_a - basket_b)  # difference 
