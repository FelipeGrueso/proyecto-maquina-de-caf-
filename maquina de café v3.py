agua = 400
leche = 540
café = 120
cups = 9
money = 550
    
while True:
    
    action = input("Write action (buy, fill, take): ")
    if action == "exit":
        break

    if action == "buy":
        tipo = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if action == "back":
            continue
                
        elif tipo == "1":
            if agua <250:
                print("Sorry, not enough water!")
            elif café <16:
                print("Sorry, not enough coffee!")
            elif cups <1:
                print("Sorry, not enough water!")
            else:
                agua -= 250
                café -= 16
                money += 4
                cups -= 1
                print("I have enough resources, making you a coffee!")
             
        elif tipo == "2":
            if agua <350:
                print("Sorry, not enough water!")
            elif café <20:
                print("Sorry, not enough coffee!")
            elif leche <75:
                print("Sorry, not enough milk!")
            elif cups <1:
                print("Sorry, not enough water!")
            else:     
                agua -= 350
                leche -= 75
                café -= 20
                money += 7
                cups -= 1
                print("I have enough resources, making you a coffee!")
            
        elif tipo == "3":
            if agua <200:
                print("Sorry, not enough water!")
            elif café <12:
                print("Sorry, not enough coffee!")
            elif leche <100:
                print("Sorry, not enough milk!")
            elif cups <1:
                print("Sorry, not enough water!")  
            else:
                agua -= 200
                leche -= 100
                café -= 12
                money += 6
                cups -= 1
                print("I have enough resources, making you a coffee!")
            
    if action == "fill":
        agua += int(input("Write how many ml of water you want to add: "))
        leche += int(input("Write how many ml of milk you want to add: "))
        café += int(input("Write how many grams of coffee beans you want to add: "))
        cups += int(input("Write how many disposable coffee cups you want to add: "))

    if action == "take":
        print(f"I gave you ${money}")
        money = 0

    if action == "remaining":
        print(f"""
The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
${money} of money
""")


