print("\033[1;32;40m\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Here is the menu \n")

print("\n\t\t\t\t\t\t\tDrinks\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tnon-veg")

print("\n\t\t\t\t\t\t\t1.coffee             20.00"+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t7.Chicken Briyani(half)               60.00")
print("\n\t\t\t\t\t\t\t2.Tea                20.00"+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t8.chicken Briyani(full)               100.00")
print("\n\t\t\t\t\t\t\t3.lemon Tea          30.00"+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t9.chicken 65(1kg)                     300.00")
print("\n\t\t\t\t\t\t\tVeg")
print("\n\t\t\t\t\t\t\t4.Veg Paneer         50.00")
print("\n\t\t\t\t\t\t\t5.Roti               15.00")
print("\n\t\t\t\t\t\t\t6.veg Biriyani       100.00")
print("\033[0m")
table=int(input("Select the table"))
choices=input("enter your choice")
if choices=='1':
    print("you Are Ordered Coffee")
    plates=int(input("how many cups you want"))
    prize = 20.00
    order = "Coffee"
    total=prize * plates

elif choices=='2':
    print("you ordered Tea")
    plates=int(input("how many cups you want"))
    prize=20.00
    order="Tea"
    total = prize * plates


elif choices=='3':
    print("your ordered Lemon Tea")
    plates=int(input("how many cups you want"))
    prize=20.00
    order = "Lemon Tea"
    total = prize * plates


elif choices=='4':
    print("your ordered Veg Paneer")
    plates=int(input("how many plates you want"))
    prize=50.00
    order = "Veg Paneer"
    total = prize * plates


elif choices=='5':
    print("your ordered Roti")
    plates=(input("how many plates you want"))
    prize=15.00
    order = "Veg Paneer"
    total= prize * plates


elif choices=='6':
    print("your ordered Veg Biriyani")
    plates=int(input("how many plates you want"))
    prize=100.00
    order = "Veg Biriyani"
    total= prize * plates
elif choices=='7':
    print("your ordered Chicken Biriyani(Half)")
    plates=int(input("how many plates you want"))
    prize=60.00
    order = "Chicken Biriyani(Half)"
    total=prize * plates


elif choices=='8':
    print("your ordered Chicken Biriyani(full)")
    plates=int(input("how many plates you want"))
    prize=100.00
    order = "Chicken Biriyani(full)"
    total = prize * plates


elif choices=='9':
    print("you ordered Chicken65")
    plates=input("how many plates you want")
    prize=300.00
    order = "Chicken65"
    total = prize * plates



b=input('Are you need anything else')
if b=='yes':
    choices=input("select your order")
    if choices=='1':
        print("you ordered Coffee")
        plates=int(input("how many cups you want"))
        order1="Coffee"
        prize=20.00
        total1 = prize * plates


    elif choices=='2':
        print("you ordered Tea")
        plates=int(input("how many cups you want"))
        order1 = "Tea"
        prize = 20.00
        total1 = prize * plates


    elif choices == '3':
        print("you ordered Lemon Tea")
        plates = int(input("how many cups you want"))
        order1 = "Lemon Tea"
        prize = 20.00
        total1 = prize * plates


    elif choices == '4':
        print("you ordered Veg Paneer")
        plates = int(input("how many plates you want"))
        order1 = "Veg Paneer"
        prize = 50.00
        total1 = prize * plates



    elif choices == '5':
        print("you ordered Roti")
        plates = int(input("how many plates you want"))
        order1 = "Rooti"
        prize = 15.00
        total1 = prize * plates


    elif choices == '6':
        print("you ordered Veg Biriyani")
        plates = int(input("how many plates you want"))
        order1 = "Veg Biriyani"
        prize = 100.00
        total1 = prize * plates


    elif choices == '7':
        print("you ordered Chicken Biriyani(Half)")
        plates = int(input("how many plates you want"))
        order1 = "Chicken Biriyani(Half)"
        prize = 60.00
        total1 = prize * plates



    elif choices == '8':
        print("you ordered full Biriyani(full)")
        plates = int(input("how many plates you want"))
        order1 = "Chicken Biriyani(full)"
        prize = 100.00
        total1 = prize * plates



    elif choices == '9':
        print("you ordered Chicken65")
        plates1= int(input("how many plates you want"))
        order1 = "Chicken65"
        prize = 300.00
        total1=prize*plates


    print("\033[1;32;40m\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Bill\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTable-",table)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\torder1-",order)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tplates/cups", plates)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\torder2",order1)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tplates",plates)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal amount-",total+total1)
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank you, Visit again")
if b=="no":
    print("\033[1;32;40m\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Bill\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttable",table)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\torder-",order)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tplates/cups",plates)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal amount-",total)
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank you, Visit again")










