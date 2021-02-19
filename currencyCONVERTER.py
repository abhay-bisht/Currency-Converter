with open("currency.txt") as f:
    a = f.readlines()
currencydict ={}
for line in a:
    parsed = line.split("\t")
    currencydict[parsed[0]]=parsed[1]

amount = int(input("Enter the amount u want to convert : "))
print("Enter the name of currency u want to convert the amount ? \n"
      "available options : \n")
[print(item) for item in currencydict.keys()]
currency = input("please enter one of these values : \n")
print(f"{amount} INR is equal to {amount*float(currencydict[currency])} {currency}")