# Name - GUNAR SINDHWANI
# Roll No - 2020199
import a2


# Write the code here for creating an interactive program.
print('-'*40)
print("DATABASE MANAGER")
print('-'*40)
print('')
print("Welcome to the Database Manager")
print('')
print("Please Read the Menu Carefully and then Proceed!")
print('')
print('         MENU       ')
print('')
print('S.no| Task to Perform        | Input Code | Input Requirements                                                | Output')
print('1   |Read Data from Data File| 1          |                                                                   |          ')
print("2   |Filter By First Name    | 2          | Enter the First Name                                              | List of  ID with the input First Name")
print("3   |Filter By Last Name     | 3          | Enter the Last Name                                               | List of  ID with the input Last Name")
print("4   |Filter By Full Name     | 4          | Enter the Full Name                                               | List of  ID with the Same Full Name")
print("5   |Filter By Age Range     | 5          | Enter the Minimum and Maximum Age for Filtration                  | List of ID with age between Min-Age and Max-Age")
print("6   |Count by Gender         | 6          | You just have to call the function                                | Returns the Gender Count in the Database")
print("7   |Filter by Address       | 7          | Enter the Address                                                 | Returns the list of ID with common Address Inputs")
print("8   |Alumni                  | 8          | Enter the Institute Name                                          | Returns Alumni of Each Institute")
print("9   |Topper Of Each Institute| 9          | You have to just enter the Input Code                             | Returns Topper of Each Institute and ID")
print("10  |Blood Donor             | 10          | Enter the Receiver Person ID                                     | Returns Contact Number of Possible Blood Donors")
print("11  |Common Friends          | 11         | Enter the List of ID                                              | Returns list of Common Friends")
print('12  |Is Related              | 12         | Enter 2 input ID                                                  |  Returns if two person are related or not')
print("13  |Delete ID               | 13         | Enter the Person ID                                               | Deletes the ID")
print("14  |Add Friend              | 14         | Enter the Person ID and Friend ID                                 | Adds Friend ")
print("15  |Remove Friend           | 15         | Enter the Person ID and Friend ID                                 | Removes Friend")
print("16  |Add Education           | 16         | Enter the Person ID,Institute Name , Ongoing Status and Percentage| Updates or Adds Education of the Person")
print("")

while True:
    n = int(input("Please Fill the Input Code from the Above Menu. Enter -1 to exit from the Database! Thankyou :"))
    if n==-1:
        print("Thanks for Coming ! We wish you Good Luck!")
        break
    if n==1:
        records=a2.read_data_from_file()
        print(records)

    if n==2:
        first_name=input("Enter First Name")
        list1=a2.filter_by_first_name(records,first_name)
        print(list1)

    if n==3:
        last_name=input("Enter Last Name")
        list2=a2.filter_by_last_name(records,last_name)
        print(list2)

    if n==4:
        full_name=input("Enter Full Name")
        list3=a2.filter_by_full_name(records,full_name)
        print(list3)

    if n==5:
        min_age=int(input("Enter Minimum Age"))
        max_age=int(input("Enter Maximum Age"))
        list5=a2.filter_by_age_range(records,min_age,max_age)
        print(list5)

    if n==6:
        dict={a2.count_by_gender(records)}
        print(dict)

    if n == 7:

        address = {}
        house_no = input('Enter House No. : ')
        block = input('Enter Block No. : ')
        town = input('Enter Town Name : ')
        city = input('Enter City Name : ')
        state = input('Enter State Name : ')
        pincode = (input('Enter PinCode : '))
        if house_no != '':
            house_no = int(house_no)
            address['house_no'] = house_no
        if block != '':
            address['block'] = block
        if town != '':
            address['town'] = town
        if city != '':
            address['city'] = city
        if state != '':
            address['state'] = state
        if pincode != '':
            pincode = int(pincode)
            address['pincode'] = pincode
        print('address = ', address)
        list4 = a2.filter_by_address(records, address)
        print(list4)

    if n==8:
        institute_name=input("Enter The Institute Name : ")
        list6=a2.find_alumni(records,institute_name)
        print(list6)

    if n==9:
        dict2={a2.find_topper_of_each_institute(records)}
        print(dict2)

    if n==10:
        receiver_person_id=int(input('Enter the Receiver Person ID : '))
        dict3={a2.find_blood_donors(records,receiver_person_id)}
        print(dict3)

    if n==11:
        list_of_id=list(map(int,input().split()))
        list7=a2.get_common_friends(records,list_of_id)
        print(list7)

    if n == 13:
        person_id = int(input('Enter Person ID : '))
        records = a2.delete_by_id(records, person_id)
        print(records)


    if n==14:
        person_id1=int(input("Enter Person ID : "))
        friend_id1=int(input("Enter Friend ID : "))
        records=a2.add_friend(records,person_id1,friend_id1)
        print(records)

    if n==15:
        person_id2=int(input('Enter Person ID : '))
        friend_id2=int(input("Enter Friend ID : "))
        records=a2.remove_friend(records,person_id2,friend_id2)
        print(records)

    if n == 16:
        person_id = int(input('Enter the Person ID :  '))
        institute_name = input('Enter Name of the Institute : ')
        ongoing = input('Please Enter your ongoing education status (True if you are still studying else False) : ')
        if ongoing.lower() == 'false':
            percentage = float(input('Enter the percentage: '))
            ongoing = False
        elif ongoing.lower() == 'true':
            ongoing = True
        records = a2.add_education(records, person_id, institute_name, ongoing, percentage)
        print(records)
    if n==12:
        person_id4=int(input('Enter Person ID : '))
        person_id5=int(input('Enter Second Person ID : '))
        boola=a2.is_related(records,person_id4,person_id5)
        print(boola)
    if n>16 or n<-1 or n==0:
        print('Invalid Code : Try Again')












