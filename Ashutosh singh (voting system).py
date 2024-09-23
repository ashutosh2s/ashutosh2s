BJP = 0
INC = 0
SWP = 0
BSP = 0
while True:
    name = input("PROVIDE YOUR NAME: ")
    age = int(input("PROVIDE YOUR AGE: "))
    
    if age >= 18:
        print("\nELIGIBLE...\n")
        print("******** VOTING LIST ********")
        print("1. BJP\n2. INDIAN NATIONAL CONGRESS\n3. SAMAJWADI PARTY\n4. BAHUJAN SAMAJ PARTY")
        print("***************************")
        
        choice = input("PROVIDE SERIAL NUMBER OF YOUR DESIRED PARTY: ")
        
        if choice == '1':
            BJP += 1
        elif choice == '2':
            INC += 1
        elif choice == '3':
            SWP += 1
        elif choice == '4':
            BSP += 1
        else:
            print("INVALID CHOICE GIVEN. VOTING WILL NOT BE COUNTED.")
    else:
        print("\nNOT ELIGIBLE...\n")
    
    more = input("FOR GIVING VOTE TYPE Y/y ELSE N/n: ")
    if more== 'y' or more=="Y":
        continue
    elif more=='n' or more=="N":
        break


if BJP>INC:
    if BJP>SWP:
        if BJP>BSP:
            print("THE ELECTION EINNER IS BJP")
        else:
            print("THE ELECTION WINNER IS BSP")
    elif SWP>BSP:
        print("THE ELECTION WINNER IS BSP")
        
