#Here's a Python Program


def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Banana"

result = linear_search_product(products, target)
print(result)