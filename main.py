#Create an address book that can get various inputs, store them, and retrieve them whenever needed.
def menu(): 
	# We created this simple menu function for 
	# code reusability & also for an interactive console 
	# Menu func will only execute when called 
	print("********************************************************************") 
	print("\t\t\tSMARTPHONE DIRECTORY", flush=False) 
	print("********************************************************************") 
	print("\tYou can now perform the following operations on this phonebook\n") 
	print("1. Add a new contact") 
	print("2. Remove an existing contact") 
	print("3. Delete all contacts") 
	print("4. Search for a contact") 
	print("5. Display all contacts") 
	print("6. Exit phonebook") 

	# Out of the provided 6 choices, user needs to enter any 1 choice among the 6 
	# We return the entered choice to the calling function wiz main in our case 
	choice = int(input("Please enter your choice: ")) 
	return choice 


def create_phonebook():
    rows=int(input("Enter the number of contacts"))
    column=5
    phonebook=[]
    for i in range(rows):
        print("....................................................................") 
        print("Enter contact number",i+1)
        print("....................................................................") 
        temp=[]
        for j in range(1,column+1):
            if j == 1: 
               name=input("Enter name : ")
               temp.append(name)
            if j == 2: 
               phone_number=int(input("Enter phone number: "))
               temp.append(phone_number)
            if j == 3: 
               email=input("Enter e-mail address: ")
               temp.append(email)
            if j == 4:
               date_of_birth=int(input("Enter date of birth(dd/mm/yy): "))
               temp.append(date_of_birth)
            if j ==5:
               category=input("Enter category(Family/Friends/Work/Others): ")
               temp.append(category)
        phonebook.append(temp) 
    return phonebook


def add_contact(pb):
    # Adding a contact is the easiest because all you need to do is: 
	# append another list of details into the already existing list 
	temp = [] 
    for j in range(1,6):
        if j == 1: 
            name=input("Enter name : ")
            temp.append(name)
        if j == 2: 
            phone_number=int(input("Enter phone number: "))
            temp.append(phone_number)
        if j == 3: 
            email=input("Enter e-mail address: ")
            temp.append(email)
        if j == 4:
            date_of_birth=int(input("Enter date of birth(dd/mm/yy): "))
            temp.append(date_of_birth)
        if j ==5:
            category=input("Enter category(Family/Friends/Work/Others): ")
            temp.append(category)
    pb.append(temp)
    return pb


    
            
            
            




print("Welcome to my phonebook")
print("....................................................................") 
print("Lets make a phonebook")
print("....................................................................") 
pb=create_phonebook()
choice=menu()

if choice == 1:
    pb=add_contact(pb)
#elif choice == 2:
    pb
    

