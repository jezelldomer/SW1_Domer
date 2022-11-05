

list1 = [15, 7, 9, 12, 45, 90, 23, 27, 52, 70]
print("List of numbers:", list1)

def get_menu_options():
    while True:
        menu_options=('1','2','3','4','5','6','7','9')
        menu= ("\n ‿︵‿︵  ୨˚̣̣̣͙୧ - - ୨˚̣̣̣͙୧   ‿︵‿︵ \n \n** M E N U **\n \n 1. Add a number to the list, \n 2. Remove a number from the list, \n 3. Sort the numbers in ascending order, \n 4. Sort the numbers in descending order \n 5. Display the lowest number, \n 6. Display the highest number \n 9. Quit \n ‿︵‿︵  ୨˚̣̣̣͙୧ - - ୨˚̣̣̣͙୧  ‿︵‿︵ \n ")

        print(menu)
        print("Choose from the menu above:")
        target=input()
        if target in menu_options:
            return target
        else:
            print()
            print("Not in the options! Please Try Again\n")
   
while True:
    target=get_menu_options()
    
    if target=="1":
        Addnum=input("Type in a number to add: ")
        list1.append(Addnum) 
        print (list1)
    
    elif target=="2":
        print ("What number would you like to remove?:")
        Removenum=int(input())
        list1.remove(Removenum)
        print (list1,"\n")
    
    elif target=="3":
        list1.sort()
        print (list1,"\n")
        
    elif target=="4":
        list1.sort(reverse=True)
        print(list1,"\n")
            
    elif target=="5":
        smallest=min(list1)
        print("The lowest number is:", smallest,"\n")
       
    elif target=="6":
        largest=max(list1)
        print("The highest number is:", largest,"\n")
    
    elif target=="9":
        print("Good bye and Thank You!") 
        exit()
        