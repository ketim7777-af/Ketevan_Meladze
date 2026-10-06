
names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

e_catalog = list(zip(names, prices, ratings))
print(e_catalog)

sorted_catalog = sorted(e_catalog, key=lambda prices: prices[1], reverse=True)
print(sorted_catalog)

new_catalog = sorted(e_catalog, key=lambda rating: rating[2])
print(new_catalog)