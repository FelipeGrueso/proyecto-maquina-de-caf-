agua = int(input("Write how many ml of water the coffee machine has: "))
leche = int(input("Write how many ml of milk the coffee machine has:"))
café = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))


minimo = min(agua // 200, leche//50, café // 15)

if minimo >= cups:
    if minimo - cups == 0:
        print("Yes, I can make that amount of coffee")
        
    else:
        print(f"Yes, I can make that amount of coffee (and even {minimo - cups} more than that)")

elif (agua / 200 >= cups and leche / 50  >= cups and café / 15) >= cups:
    print(f"No, I can make only {minimo} cups of coffee")
    

else:
    print(f"No, I can make only {minimo} cups of coffee")



    

    
