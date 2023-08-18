products = []
def read_data():
    f = open("sesstion8/test.txt", "r")
    for l in f:
       product = l.split(",")
       dic = {"id":product[0], "name":product[1],
               "price":product[2], "cout":product[3]}
       products.append(dic)
       print(products)
def show_menu():
    print("1- add")
    print("2- delete")
    print("3- search")
    print("4- buy")
    print("5- edit")
    print("6- exit")
    print("7- show_products")

def add():
    id = input("Enter id: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    count = input("Enter count: ")
    dic = {"id":id, "name":name, "price":price, "count":count}
    products.append(dic)
    print(products)
def delete():
    ID = input("Enter the id of each product that you want to delete: ")
    for product in products:
        if ID == product["id"]:
            products.remove(product)
            print("Deleted")
        else:
            print("Enter the correct id: ")
def search():
    key = input("Enter your key: ")
    for product in products:
        if key == product["id"] or key == product["name"]:
            print(product)
            break
        else:
            print("Not found")
def buy():
    while True:
         A = int(input(" 1=Exit ,2=buy , 3=receipt , 3=add , 4=show menu"))
         if A == 1:
             break
         elif A == 2:
            ID = input("Enter the id of each product that you want to buy: ")
            for product in products:
                if ID == product["id"]:
                    number = int(input("Enter the number: "))
                    stock = int(product["count"])
                    if number <= stock:
                        new_stock = stock - number
                        print("Done")
                        print("id \t name \t price")
                        print(product["id"],'\t' , product["name"],
                               '\t', product["price"] )
                    else:
                        print("we don't have enough stock")
                        break
         elif A == 3:
             receipt = []
             dic = {'id':product['id'],'name':product['name'],'price':product['price']}
             receipt.append(dic)
             for p in receipt:
                print(p['id'],'\t',p['name'],'\t',p['price'])
        
         elif A == 4:
            show_menu()
            user = int(input("Enter your key: "))
            if user == 1:
                add()
            elif user == 2:
                delete()
            elif user == 3:
                search()
            elif user == 4:
                buy()
            elif user == 5:
                edit()
            elif user == 6:
                exit()
            elif user == 7:
                show_products()
            else:
                print("Error")
            break
        
def edit():
    ID = input("Enter the id of product that you want to edit:")
    for product in products:
        if ID == product['id']:
            print(product)
            print("Which one needs edit? 1=name , 2=price , 3=count")
            B = input("Enter the number:")
            if B == '1':
                edit_name = input("Enter new name:")
                product['name'] = edit_name
                print("Done:",product)
            elif B == '2':
                edit_price = input("Enter new price:")
                product['price'] = edit_price
                print("Done:",product)
            elif B == '3':
                edit_count = input("Enter new count:")
                product['count'] = edit_count
                print("Done:",product)
            else:
                print("Error")
                print(products)
def exit():
    pass
def show_products():
    print("id\t name \t price \t cout")
    for product in products:
        print(product["id"], "\t", product["name"], "\t", 
              product["pric"], "\t", product["count"])

read_data()
show_menu()
user_choice = int(input("Enter your choice: "))
if user_choice == 1:
    add()

elif user_choice == 2:
    delete()

elif user_choice == 3:
    search()

elif user_choice == 4:
    buy()

elif user_choice == 5:
    edit()

elif user_choice == 6:
    exit()

elif user_choice == 7:
    show_products()
else:
    print("Error")