print("***********welcome to ziziya we here to serve a favorite food ***********")
print("\n The menu are\t\t 1.Burger\t\t 2.Pizza\t\t 3.Noodles\t\t 4.Sandwiches\t\t 5.Soups and Salads ")
choose=input("Are you want order a food")
card=[]
quantity=[]
add=0

if choose== 'yes':

    x=input("select the order")

    if x==1:
        print("1.Californian Double chicken burger $ 149\t2.Pepper Mushroom Tacos $ 149")
        a = input("selected a  which  burger do  you want")
        item1 = "Californian Double chicken burger"
        item2 = "Pepper Mushroom Tacos "
        if a==1:
            print("1 item is added to card")
            price=149
            print("if u want add one more")
            if p1 =='yes':
                add=add+1
                quantity.append(add*price)
                total = price
                card.append(item1)
                card.append(total)
                card.extends(quantity)
                print(card)
            else p2=='no':

                total=price
                card.append(item1)
                card.append(total)
                print(card)
        elif a==2:
            print(" 2 item is added to card")
            price = 149
            total=price
            card.append(item2)
            card.append(price)
            print(card)
    elif x==2:
        b = input("selected a pizza  you want")
        print("1.Corn Pizza $149 \t 2.onion Pizza $149")
        item1 = "Corn pizza"
        item2 = "Onion Pizza "
        if b==1:
            print("1 item is added to card")
            price = 149.00
            total = price
            card.append(item1)
            card.append(total)
            print(card)
        else b==2:
            print(" 2 item is added to card")
            price = 150.00
            total = price
            card.append(item2)
            card.append(price)
            print(card)

    elif x==3:

        c = input("selected a Noodles  you want")
        print("1.Teriyaki Chicken Noodle Bowl $149 \t 2.Tofu Veggie  Stirfy $149")
        item1 = "Teriyaki Chicken Noodle Bowl"
        item2 = "Tofu Veggie Strify"
        if c==1:
            print("1 item is added to card")
            price = 150.00
            total = price
            card.append(item1)
            card.append(total)
            print(card)
        elif c==2:
            print(" 2 item is added to card")
            price = 170.00
            total = price
            card.append(item2)
            card.append(price)
            print(card)

    elif x == 4:
        d = input("selected a Noodles  you want")
        print("1.Spinach Corn Whole Wheat Sandwich $119 \t 2.Paneer Slaw Whole Wheat Sandwich  $129")
        item1 = "Spinach Corn Whole Wheat Sandwich"
        item2 = "Paneer Slaw Wheat Sandwich"
        if d==1:
            print("1 item is added to card")
            price = 150.00
            total = price
            card.append(item1)
            card.append(total)
            print(card)
        else d==2:
            print(" 2 item is added to card")
            price = 170.00
            total = price
            card.append(item2)
            card.append(price)
            print(card)
    elif x==5:

        e = input("selected a soups and salad  you want")
        print(
            "1.Peri Peri Chicken Salad  $299\t 2.Morocon Paneer Super Salad $299\t3.Cream-of Spinach Corn Soup $ 134\t Creamy Tamoto Thyme Soup $ 123")
        item1 = "peri peri Chicken Salad"
        item2 = "Morocon Paneer Super Salad"
        item3 = "Cream-of Spinach Corn Soup"
        item4 = "Creamy Tamoto Thyme Soup"

        if e==1:
            print("1 item is added to card")
            price = 299.00
            total = price
            card.append(item1)
            card.append(total)
            print(card)
        elif e==2:
            print(" 2 item is added to card")
            price = 299.00

            total = price
            card.append(item2)
            card.append(price)
            print(card)

        elif e==3:
            print(" 3 item is added to card")
            price = 134.00
            total = price
            card.append(item2)
            card.append(price)
            print(card)
        else 'e==4':
            print(" 4 item is added to card")
            price = 123.00
            total = price
            card.append(item2)
            card.append(price)
            print(card)


        print("Invoice")
        print("card",card)

else choose=='no':
    print("you are not ordered anything ")




