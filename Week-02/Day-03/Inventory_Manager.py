def get_number_of_products():

    num_product = int(input("How many product do you want to enter? "))
    
    while num_product <= 0:
        print("Enter a valid Number")
        num_product = int(input("How many product do you want to enter? "))
        
    return num_product

def store_products(num_product):

    inventory = {}
    
    for n in range(num_product):
        name, quantity = input(f"Enter the product name and how many quantity: ").split()
        quantity = int(quantity)
        inventory[name.lower()] = quantity
    return inventory

def display_inventory(store_product):
    width = 6
    line = "=" * 6
    title = "INVENTORY"
    middle = title.center(width)
    
    print(f"{line} {middle} {line}")
    for name, product in store_product.items():
        print(f"{name.capitalize()}: {product}")
    print(line * 4)

def search_product(store_product):
    while True:
        name = input("Enter the product to search: ")

        found = False
        
        if name.lower() in store_product.keys():
            print(f"{name.lower().capitalize()} is in stock")
            print(f"Quantity: {store_product.get(name.lower())}")
            found = True
            break
        if not found:
            print("Product not found")
            search = input("Do you want to search again? (Y/N): ")
            if search.upper() == "N":
                print("Goodbye!")
                break
        if search.upper() == "Y":
            continue      
         
def update_quantity(store_product):
    new_product, new_quantity = input("Which product do you want to update and how many quantity? ").split()
    new_quantity = int(new_quantity)
    
    while new_product.lower() not in store_product.keys():
        print("Product does not exist")
        new_product, new_quantity = input("Which product do you want to update and how many quantity? ").split()
        new_quantity = int(new_quantity)
        
    store_product[new_product.lower()] = new_quantity
    
    another_product = input("Do you want to add another product? (Y/N): ")
    
    while another_product.upper() == "Y":
    
        name, quantity = input(f"Enter the product name and how many quantity: ").split()
        quantity = int(quantity)
        store_product[name.lower()] = quantity
        
        another_product = input("Do you want to add another product? (Y/N): ")
        
    return store_product
    
    
num_product = get_number_of_products()

store_product = store_products(num_product)

display_inventory(store_product)

search_product(store_product)

store_product = update_quantity(store_product)

display_inventory(store_product)
