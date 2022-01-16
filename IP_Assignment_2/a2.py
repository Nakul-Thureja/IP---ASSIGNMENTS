# Assignment - 2
# Name - Nakul Thureja 
# Roll No - 2020528

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
    '''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
    '''
	
    with open(file_path, 'r') as data:
        records = json.load(data)

    return records


def filter_by_first_name(records, first_name):
    '''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    l=[]
    for i in range(len(records)):
        if records[i]['first_name'].lower()==first_name.lower():
            l.append(records[i]['id'])

    return l


def filter_by_last_name(records, last_name):
    '''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    l=[]
    for i in range(len(records)):
        if records[i]['last_name'].lower()==last_name.lower():
            l.append(records[i]['id'])

    return l


def filter_by_full_name(records, full_name):
    '''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    l=[]
    name=full_name.split()
    
    for i in range(len(records)):
        if records[i]['first_name'].lower()==name[0].lower() and records[i]['last_name'].lower()==name[1].lower():
            l.append(records[i]['id'])

    return l

    
def filter_by_age_range(records, min_age, max_age):
    '''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    l=[]
    for i in range(len(records)):
        if min_age<=records[i]['age']<=max_age:
            l.append(records[i]['id'])

    return l


def count_by_gender(records):
    '''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
    '''
    d={'male':0,'female':0}
    for i in range(len(records)):
        d[records[i]['gender']]+=1

    return d


def filter_by_address(records, address):
    '''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
    '''
    list1=[]
    
    for i in range(len(records)):
        d=dict()
        c1=0
        c2=0
        if "house_no" in address.keys():
            c1+=1
            if address['house_no'] == records[i]['address']['house_no']:
                c2+=1
            
        if "block" in address.keys():
            c1+=1
            if address['block'].lower() == records[i]['address']['block'].lower():
                c2+=1

        if "town" in address.keys():
            c1+=1
            if address['town'].lower() == records[i]['address']['town'].lower():
                c2+=1

        if "city" in address.keys():
            c1+=1
            if address['city'].lower() == records[i]['address']['city'].lower():
                c2+=1
                
        if "state" in address.keys():
            c1+=1
            if address['state'].lower() == records[i]['address']['state'].lower():
                c2+=1
            
        if "pincode" in address.keys():
            c1+=1
            if address['pincode'] == records[i]['address']['pincode']:
                c2+=1
        
        
        if c1==c2:
            d['first_name']=records[i]['first_name']
            d['last_name'] =records[i]['last_name']
            list1.append(d)

    return list1
            
            
def find_alumni(records, institute_name):
    '''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
    '''
    l=[]
    for i in range(len(records)):
        d=dict()
        institute=[]
        for j in range(len(records[i]['education'])-1,-1,-1):
            if records[i]['education'][j]['institute'] not in institute and records[i]['education'][j]['ongoing']==False:
                institute.append(records[i]['education'][j]['institute'])
                if records[i]['education'][j]['institute'].lower() == institute_name.lower():
                    d["first_name"]=records[i]["first_name"]
                    d["last_name"] =records[i]["last_name"]
                    d["percentage"]=records[i]['education'][j]["percentage"]
                    l.append(d)  

    return l


def find_topper_of_each_institute(records):
    '''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
    '''
    d=dict()
    d1=dict()
    institutes=[] 
    for i in range(len(records)):
        institute=[]
        for j in range(len(records[i]['education'])-1,-1,-1):
            if records[i]['education'][j]['institute'] not in institute and records[i]['education'][j]['ongoing']==False:
                institute.append(records[i]['education'][j]['institute'])

                if records[i]['education'][j]['institute'] in d.keys():
                    if d[records[i]['education'][j]['institute']] <  records[i]['education'][j]['percentage']:
                        d[records[i]['education'][j]['institute']] = records[i]['education'][j]['percentage']
                        d1[records[i]['education'][j]['institute']] = records[i]['id']
                else:
                    d[records[i]['education'][j]['institute']] = records[i]['education'][j]['percentage']
                    d1[records[i]['education'][j]['institute']] = records[i]['id']
    return d1
                       

def find_blood_donors(records, receiver_person_id):
    '''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''
    d=dict()
    receiver_blood_group=None
    for i in range(len(records)):
        if receiver_person_id==records[i]['id']:
            receiver_blood_group = records[i]['blood_group']


    if receiver_blood_group!=None:
        for i in range(len(records)): 
            blood_group=records[i]['blood_group']
            if records[i]['id']!=receiver_person_id:
                if blood_group=='O':
                    d[records[i]['id']]=records[i]['contacts']
                elif blood_group=='A' and (receiver_blood_group=='A' or receiver_blood_group=='AB'):
                    d[records[i]['id']]=records[i]['contacts']
                elif blood_group=='B' and (receiver_blood_group=='B' or receiver_blood_group=='AB'):
                    d[records[i]['id']]=records[i]['contacts']
                elif blood_group=='AB' and receiver_blood_group=='AB':
                    d[records[i]['id']]=records[i]['contacts']

    return d


def get_common_friends(records, list_of_ids):
    '''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''
    friends=[]
    for i in range(len(records)):
        if records[i]['id'] in list_of_ids:
            friends.append(records[i]['friend_ids'])
    common_friends=[]
    for j in friends[0]:
        c=0
        for i in range(1,len(friends)):
            if j in friends[i]:
                c+=1
        if j not in list_of_ids and c==len(friends)-1:
            common_friends.append(j)

    return common_friends


def make_set(l):
    '''
        *****************Helper function*********************
        Description: Returns a a list of sorted and unique IDs(integers) in the given list l

        Parameters:
        - l(list): a list of integers
        
        Returns:
        - A LIST of INTEGERS containing unique elements in sorted order
    '''  
    list1=[]
    for i in l:
        if i not in list1:
            list1.append(i)
    list1.sort()

    return list1
        

def get_friends(records, list_of_ids,person_id_1):
    '''
    *****************Helper function*********************
    Description: Find all the direct and indirect friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people who are friends of the  to be found
    - person_id_1: id of the main person whose friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the direct and indirect friends of the person_id_1
    '''
    friends=[]
    
    for i in range(len(records)):
        if records[i]['id'] in list_of_ids:
            friends.extend(records[i]['friend_ids'])

    friends=make_set(friends)
    if person_id_1 in friends:
        friends.remove(person_id_1)
    
    return friends


def is_related(records, person_id_1,person_id_2):
    '''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''
   
    list_of_ids=[person_id_1]
    f=[]

    while(True):
        a=[]
        a.extend(f)
        f=f+get_friends(records,list_of_ids,person_id_1)
        f=make_set(f)
        list_of_ids=f
        if a==f:
            break


    if person_id_2 in f:
        return True
    else:
        return False
  

def delete_by_id(records, person_id):
    '''
	Description: Given a person ID, this function deletes them from the records.
	Note that the given person can also be a friend of any other person(s),
	so also delete the given person ID from other persons friend list.
	If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
    '''
    index=None
    friends=[]
    for i in range(len(records)):
        if records[i]['id']==person_id:
            index=i
        if person_id in records[i]['friend_ids']:
            records[i]['friend_ids'].remove(person_id)
    if index != None:
        records.pop(index)
    return records


def add_friend(records, person_id, friend_id):
    '''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
    '''
    t1=False
    t2=False
    for i in range(len(records)):
        if person_id==records[i]['id']:
            t1=True
            
        elif friend_id==records[i]['id']:
            t2=True
            
    
    if t1 and t2 :
        for i in range(len(records)):
            if person_id==records[i]['id']:
                if friend_id not in records[i]['friend_ids']:
                    records[i]['friend_ids'].append(friend_id)
            elif friend_id==records[i]['id']:
                if person_id not in records[i]['friend_ids']:
                    records[i]['friend_ids'].append(person_id)

    return records


def remove_friend(records, person_id, friend_id):
    '''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
    '''
    
    t1=False
    t2=False
    for i in range(len(records)):
        if person_id==records[i]['id']:
            t1=True
        elif friend_id==records[i]['id']:
            t2=True
            
    if t1 and t2 :
        for i in range(len(records)):
            if person_id==records[i]['id']:
                if friend_id in records[i]['friend_ids']:
                    records[i]['friend_ids'].remove(friend_id)
            elif friend_id==records[i]['id']:
                if person_id in records[i]['friend_ids']:
                    records[i]['friend_ids'].remove(person_id)

    return records


def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
    ''' 
    for i in range(len(records)):
        d=dict()
        if person_id==records[i]['id']:
            d['institute']=institute_name
            d['ongoing']=ongoing
            if not ongoing:
                d['percentage']=percentage
            records[i]['education'].append(d)

    return records




