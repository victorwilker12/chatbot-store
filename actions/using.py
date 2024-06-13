# import numpy as np
# import requests
# import json
#
# response = requests.get("https://fakestoreapi.com/products/category/men's clothing")
# if response.status_code == 200:
#     list_products = []
#     s1 = json.dumps(response.json())
#     d2 = json.loads(s1)
#     for product in range(len(d2)):
#         # print(product)
#         result = d2[product].items()
#         data = list(result)
#         list_products.append(np.array(data))
#
# print(list_products)