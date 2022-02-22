import prices
print("Use the following product codes")
print("mlk-->MILK , brd-->BREAD , brn-->BOURNVITA , tit-->TITUS , cop-->COCOPOPS , egg-->EGG , btr-->BUTTER , sgr-->SUGAR")
item = input("Enter item you wish to buy")
qty=input("Enter the quantity")

if item=="mlk":
    price=prices.MILK
    total = int(qty)*price
    print("Total is :" , total)
if item=="brd":
    price=prices.BREAD
    total = int(qty)*price
    print("Total is :" , total)
 
 
 
 
 
if item=="brn":
    price=prices.BOURNVITA
    total = int(qty)*price
    print("Total is :" , total)
if item=="tit":
    price=prices.TITUS
    total = int(qty)*price
    print("Total is :" , total)
if item=="cop":
    price=prices.COCOPOPS
    total= int(qty)*price
    print("Total is :" , total)
if item=="egg":
    price=prices.EGG
    total= int(qty)*price
    print("Total is :" , total)
if item=="btr":
    price=prices.BUTTER
    total = int(qty)*price
    print("Total is :" , total)
if item=="sgr":
    price=prices.SUGAR
    total = int(qty)*price
    print("Total is :" , total)