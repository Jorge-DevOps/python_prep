if __name__ == '__main__':
    number_shoes = input()  
    sizes_shoes = list(map(int, input().split()))  
    number_customers = input()  
    list_sales = [input().split() for _ in range(int(number_customers))]
    
    total = 0
    for x in list_sales:
        shoes_size = int(x[0])
        shoes_price = int(x[1])
        if shoes_size in sizes_shoes:
            total += shoes_price
            sizes_shoes.remove(shoes_size)
    print(total)
