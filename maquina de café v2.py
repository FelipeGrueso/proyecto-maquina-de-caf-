agua = 400
leche = 540
café = 120
cups = 9
money = 550



print(f"""The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
{money} of money
""")

action = input("Write action (buy, fill, take): ")


if action == "buy":
    tipo = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if tipo == "1":
        agua -= 250
        café -= 16
        money += 4
        cups -= 1
        print(f"""The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
{money} of money
""")


    elif tipo == "2":
        agua -= 350
        leche -= 75
        café -= 20
        money += 7
        cups -= 1
        print(f"""The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
{money} of money
""")

    elif tipo == "3":
        agua -= 200
        leche -= 100
        café -= 12
        money += 6
        cups -= 1


        print(f"""The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
{money} of money
""")   
        
        
if action == "fill":
    agua += int(input("Write how many ml of water you want to add: "))
    leche += int(input("Write how many ml of milk you want to add: "))
    café += int(input("Write how many grams of coffee beans you want to add: "))
    cups += int(input("Write how many disposable coffee cups you want to add: "))
    print(f"""The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
{money} of money
""")   

    


if action == "take":
    print(f"I gave you ${money}")
    money = 0
    print(f"""The coffee machine has:
{agua} of water
{leche} of milk
{café} of coffee beans
{cups} of disposable cups
{money} of money
""")



