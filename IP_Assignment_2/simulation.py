# Name - Nakul Thureja
# Roll No - 2020528

import a2

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.
def show_menu():
    t=False
    while(True):
        print('\nWelcome to Records')
        print('''

1.  read_data_from_file 
2.  filter_by_first_name
3.  filter_by_last_name
4.  filter_by_full_name
5.  filter_by_age_range
6.  count_by_gender
7.  filter_by_address
8.  find_alumni
9.  find_topper_of_each_institute
10. find_blood_donors
11. get_common_friends
12. is_related
13. delete_by_id
14. add_friend
15. remove_friend
16. add_education

        ''')
        n=int(input('Enter Code (-1 to Exit): '))
        print()
                   
        if n==-1:
            print('Thank you for visiting records')
            break
        
        elif n==1:
            t=True
            records=a2.read_data_from_file()
            for i in records:
                print(i)

        elif not t:
            print('Please read records before performing any other operation')
            
        elif n==2:
            first_name=input('Enter First Name: ')
            id_list=a2.filter_by_first_name(records, first_name)
            print('IDs of person with first name as ', first_name)
            print(id_list)

        elif n==3:
            last_name=input('Enter last Name: ')
            id_list=a2.filter_by_last_name(records, last_name)
            print('IDs of person with last name as ', last_name)
            print(id_list)

        elif n==4:
            full_name=input('Enter Full Name: ')
            id_list=a2.filter_by_full_name(records, full_name)
            print('IDs of person with full name as ', full_name)
            print(id_list)
            
        elif n==5:
            min_age=int(input('Enter minimum age: '))
            max_age=int(input('Enter Maximun age: '))
            id_list=a2.filter_by_age_range(records, min_age, max_age)
            print('IDs of person with age between ', min_age , 'to' , max_age)
            print(id_list)
            
        elif n==6:
            print(a2.count_by_gender(records))
                   
        elif n==7:
            address=dict()

            while(True):
                flag=input('Do you want to enter house_no (y/n):')
                if flag.lower()=='y':
                    house_no=int(input('Enter House Number: '))
                    address['house_no']=house_no
                    break
                elif flag.lower()=='n':
                        break
                else:
                    print('please enter valid input')

            while(True):   
                flag=input('Do you want to enter block (y/n):')
                if flag.lower()=='y':
                    block=input('Enter block: ')
                    address['block']=block
                    break
                elif flag.lower()=='n':
                        break
                else:
                    print('please enter valid input')
                    
            while(True):
                flag=input('Do you want to enter town (y/n):')
                if flag.lower()=='y':
                    town=input('Enter town: ')
                    address['town']=town
                    break
                elif flag.lower()=='n':
                        break
                else:
                    print('please enter valid input')

            while(True):
                flag=input('Do you want to enter city (y/n):')
                if flag.lower()=='y':
                    city=input('Enter city: ')
                    address['city']=city
                    break
                elif flag.lower()=='n':
                        break
                else:
                    print('please enter valid input')

            while(True):
                flag=input('Do you want to enter state (y/n):')
                if flag.lower()=='y':
                    state=input('Enter state: ')
                    address['state']=state
                    break
                elif flag.lower()=='n':
                        break
                else:
                    print('please enter valid input')

            while(True):
                flag=input('Do you want to enter pincode (y/n):')
                if flag.lower()=='y':
                    state=int(input('Enter pincode: '))
                    address['pincode']=state
                    break
                elif flag.lower()=='n':
                        break
                else:
                    print('please enter valid input')
            print(address)
            print(a2.filter_by_address(records,address))
                
        elif n==8:
            institute_name=input('Enter institute name: ')
            print('Alumini of',institute_name,' are: ')
            print(a2.find_alumni(records, institute_name))
            
        elif n==9:
            print('Toppers of each institute are: ')
            print(a2.find_topper_of_each_institute(records))
            
        elif n==10:
            receiver_person_id=int(input('Enter the ID of the patient: '))
            print(a2.find_blood_donors(records, receiver_person_id))
            
            
        elif n==11:
            n=int(input('Enter the no of IDs: '))
            list_of_ids=input('Enter IDS ({} space separated integers): '.format(n)).split()
            for i in range(len(list_of_ids)):
                list_of_ids[i]=int(list_of_ids[i])
            print('Common freinds of {} are: '.format(list_of_ids))
            print(a2.get_common_friends(records, list_of_ids))
            
        elif n==12:
            person_id_1=int(input('Enter the ID of person 1: '))
            person_id_2=int(input('Enter the ID of person 2: '))
            print(a2.is_related(records, person_id_1,person_id_2))
    
        elif n==13:
            person_id=int(input('Enter the ID of the person whose record is to be deleted: '))
            
            print('Record of ',person_id, 'is deleted from records')
            print(a2.delete_by_id(records, person_id))
           
            
        elif n==14:
            person_id=int(input('Enter the ID of the person: '))
            friend_id=int(input('Enter the ID of the friend: '))
            print(person_id, ' is now friends with ', friend_id, 'in records')
            print(a2.add_friend(records, person_id, friend_id))
            
                
        elif n==15:
            person_id=int(input('Enter the ID of the person: '))
            friend_id=int(input('Enter the ID of the be removed from friend list: '))
            print(person_id, ' is not a friend with ', friend_id, 'in records')
            print(a2.remove_friend(records, person_id, friend_id))
            
                    
        elif n==16:
            person_id=int(input('Enter the ID of the person: '))
            institute_name=input('Enter the institute name: ')
            while(True):
                ongoing=(input('Is person_id currently studying at this institute (True/False): (case sensitive) '))
                if (ongoing=='False'):
                    percentage=float(input('Enter percentage:'))
                    print(a2.add_education(records, person_id, institute_name, False, percentage))
                    break
                elif (ongoing=='True'):
                    percentage=-1
                    print(a2.add_education(records, person_id, institute_name, True, percentage))
                    break
                else:
                    print('please enter valid input')
                    
            print('Details added in ',person_id,'Education')

        else:
            print('Please enter valid input \n')
            
    return

if __name__=='__main__':
    show_menu()
            
                
