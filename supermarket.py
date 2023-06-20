vegetables = {"cabbage": 5, "lettuce": 7,"Tomato": 4}
meat = {"beef": 10, "lamb": 9, "pork": 11}
utensils = {"fork": 2, "knife": 5, "spoon": 3}

goods = ["vegetables: ", "meat: ", "utensils: "]

def display_goods():
    global vegetables
    global meat
    global utensils
    round = 0   
    print(goods[round])
    for key, value in vegetables.items():
        print("+", key, ":", value, "$")
    round += 1 
    print(goods[round])
    for key, value in meat.items():
        print("+", key, ":", value, "$")
    round += 1
    print(goods[round])
    for key, value in utensils.items():
        print("+", key, ":", value, "$")
    round += 1   
    
def buying():
    global vegetables
    global meat
    global utensils
    order = input("Enter what you want to buy: ")
    order = order.lower()
    quantity = input("How many of them: ")
    if order in vegetables:
        vegetable_price = (vegetables[order])
        total_bill = int(quantity) * int(vegetable_price)
        print(f"The total bill for {quantity} {order} is: {total_bill}$")
    elif order in meat:
        meat_price = (meat[order])
        total_bill = int(quantity) * int(meat_price)
        print(f"The total bill for {quantity} {order} is: {total_bill}$")     
    else:
        utensils_price = (utensils[order])
        total_bill = int(quantity) * int(utensils_price)
        print(f"The total bill for {quantity} {order} is: {total_bill}$")  
        

while True:
    display_goods()
    buying()