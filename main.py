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


def remove_existing(pb): 
	# This function is to remove a contact's details from existing phonebook 
	query = str( 
		input("Please enter the name of the contact you wish to remove: ")) 
	# We'll collect name of the contact and search if it exists in our phonebook 	
	temp = 0
	# temp is a checking variable here. We assigned a value 0 to temp. 
	
	for i in range(len(pb)): 
		if query == pb[i][0]: 
			temp += 1
			# Temp will be incremented & it won't be 0 anymore in this function's scope			
			print(pb.pop(i)) 
			# The pop function removes entry at index i	
			print("This query has now been removed") 
			# printing a confirmation message after removal. 
			# This ensures that removal was successful. 
			# After removal we will return the modified phonebook to the calling function 
			# which is main in our program			
			return pb 
	if temp == 0: 
		# Now if at all any case matches temp shoul've incremented but if otherwise, 
		# temp will remain 0 and that means the query does not exist in this phonebook 
		print("Sorry, you have entered an invalid query.\nPlease recheck and try again later.")	
		return pb 
  
            
            
def display_all(pb): 
	if not pb: 
	# if display function is called after deleting all contacts then the len will be 0 
	# And then without this condition it will throw an error 
		print("List is empty: []") 
	else: 
		for i in range(len(pb)): 
			print(pb[i])           




print("Welcome to my phonebook")
print("....................................................................") 
print("Lets make a phonebook")
print("....................................................................") 
pb=create_phonebook()
choice=menu()


if choice == 1:
    pb=add_contact(pb)
elif choice == 2:
    pb=remove_existing(pb)
elif choice==5:
    display_all(pb)   
    

