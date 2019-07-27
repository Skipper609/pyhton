
products = dict()
while True:
    print("1.Add Product 2.Print Products 3.Search 4.Exit")
    ch = int(input("Enter the choice : "))
    if ch == 1:
        product_id = input("Enter the product ID:")
        name = input("Enter the Product Name :")
        if product_id in products:
            print(f"{name} is already in the list")
        else:
            products[product_id] = name
    elif ch == 2:
        if len(products) == 0:
            print("No items to Display")
        else:
            for key,value in products.items():
                print(f"{key} - {value}")
    elif ch == 3:
        pass

    else:
        break
