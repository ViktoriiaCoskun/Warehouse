import csv

from decimal import Decimal
items=[]
sold_items=[]

def load_items_from_csv():
    items.clear()
    filepath = "magazyn.csv"
    with open(filepath,"r") as csv_file:
    
        reader = csv.DictReader(csv_file)
        for item in reader:
            #print(dict(item))
            items.append(dict(item))

load_items_from_csv()

def get_items():

    print("Name\t\t Quantity\t Unit\t\t Unit Price (PLN)")
    print("------------------------------------------------------------------")
    for item in items:
        item_values=""
        for value in item.values():
            item_values=item_values+value+" \t\t"
        print(item_values)    

def add_items():
    new_item={}
    new_item["name"]=input ("Product Name :")
    new_item["quantity"]=input ("Product Quantity :")
    new_item["unit"]=input ("Product Unit :")
    new_item["unit_price"]=input ("Product Unit Price :")
    items.append(new_item)

def sell_item(itemname,quantity):
    found=False
    unit=""
    sold_item={}
    for item in items:
        if item["name"]==itemname:
           found=True
           sold_item["name"]=itemname
           sold_item["quantity"]=quantity
           sold_item["unit"]=item["unit"]
           sold_item["unit_price"]=item["unit_price"]
           sold_items.append(sold_item)
           newquantity=Decimal(item["quantity"])-Decimal(quantity)
           item["quantity"]=str(newquantity)
           unit = item["unit"]

    if(found):print("Succesfully sold",quantity,unit,"of",itemname)
    else:print(f"we could not find the product {itemname} in our stock!")
    get_items()

def get_costs():
    current_List=[Decimal(item["quantity"])*Decimal(item["unit_price"]) for item in items]
    current_cost=sum(current_List)
    return current_cost
def get_income():
    current_income=[Decimal(item["quantity"])*Decimal(item["unit_price"]) for item in sold_items]
    return sum(current_income)
def show_revenue():
    print("Revenue Breakdown (PLN)")
    print("Cost:",get_costs(),"PLN") 
    print("Income:",get_income(),"PLN") 
    print("--------------------------")
    revenue=get_income()-get_costs()
    print("Revenue:",round(revenue,2),"PLN")

def export_items_to_csv():
    filename = "magazyn.csv"
    with open(filename,"w") as csv_file:
        fields = ['name', 'unit', 'quantity', 'unit_price'] 
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(items)

    print("Succesfully added file")
    return 1





message=("what would you like to do:")
choice=""
while choice!="exit":
    choice=input(message)
    if choice=="exit":
        print("Exiting....see you!") and exit()
    elif choice=="show":   
        get_items() 
    elif choice=="add":   
        add_items()
        print("Succesfully added to stock!Current status:")
        get_items() 
    elif choice=="sell":
        itemname=input("Sold Item Name:")
        quantity=input("quantity :")
        sell_item(itemname,quantity)  
    elif choice=="cost": print("Current Cost :",get_costs(),"PLN") 
    elif choice=="income":print("Current income:",get_income(),"PLN") 
    elif choice=="revenue": show_revenue()  
    elif choice=="save": export_items_to_csv()
    elif choice=="load":load_items_from_csv()


        
        
            





