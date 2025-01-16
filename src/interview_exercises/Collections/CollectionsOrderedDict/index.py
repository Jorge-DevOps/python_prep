from collections import OrderedDict
if __name__ == "__main__":
    orders = OrderedDict()
    for _ in range(int(input())):
        name, price = input().rsplit(' ', 1)
        orders[name] = orders.get(name, 0) + int(price)
    # OrderedDict suma los valores que los que tengan el mismo nombre   
    [print(*item) for item in orders.items()]
    