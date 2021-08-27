 # Assignment - 2
# Name - GUNAR SINDHWANI
# Roll No - 2020199

import json
#*********************************************************************************************************************************************************************
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
#*********************************************************************************************************************************************************************

#code starts from here!
def filter_by_first_name(records, first_name):

	id_list_fn = []
	for i in range(len(records)):
		if records[i]['first_name'].lower() == first_name.lower():
			id_list_fn.append(records[i]['id'])
	if len(id_list_fn)>=1:
		return id_list_fn
	elif len(id_list_fn)==0:
		return id_list_fn

def filter_by_last_name(records, last_name):

	id_list_ln = []
	for i in range(len(records)):
		if records[i]['last_name'].lower() == last_name.lower():
			id_list_ln.append(records[i]['id'])
	if len(id_list_ln)>=1:
		return id_list_ln
	elif len(id_list_ln)==0:
		return id_list_ln

def filter_by_full_name(records, full_name):

	id_list_fullname = []
	x, y = full_name.split()
	x = x.lower()  # first name
	y = y.lower()  # last name
	list1 = []  # first name list
	list2 = []  # second name list
	list3 = []  # intersection of list1,list2
	list4 = []  # final unique list
	for i in range(len(records)):
		if records[i]['first_name'].lower() == x:
			list1.append(records[i]['id'])
		if records[i]['last_name'].lower() == y:
			list2.append(records[i]['id'])
	for i in range(len(list1)):
		if list1[i] in list2:
			list3.append(list1[i])
	for i in range(len(list3)):
		if list3[i] not in list4:
			list4.append(list3[i])

	if len(list4) >= 1:
		return list4
	if len(list4) == 0:
		return list4


def filter_by_age_range(records, min_age, max_age):

	agelist_id = []
	for i in range(len(records)):
		if min_age <= records[i]['age'] <= max_age:
			agelist_id.append(records[i]['id'])
	if len(agelist_id)>=1:
		return agelist_id
	elif len(agelist_id)==0:
		return agelist_id


def count_by_gender(records):
	gender_dict = {'male': 0, 'female': 0}
	for i in range(len(records)):
		if records[i]['gender'].lower() == 'male':
			gender_dict['male'] += 1
		elif records[i]['gender'].lower() == 'female':
			gender_dict['female'] += 1
	return gender_dict




def filter_by_address(records, address):
	address_id = []
	for i in range(len(records)):
		addres_dict = {'first_name': '', 'last_name': ''}
		memory = records[i]['address']
		boole = True
		for j in address.keys():
			if str(memory[j]).lower() == str(address[j]).lower():
				boole = True
			else:
				boole = False
				break
		if boole == True:
			addres_dict['first_name'] = records[i]['first_name']
			addres_dict['last_name'] = records[i]['last_name']
			address_id.append(addres_dict)


	return address_id



def find_alumni(records, institute_name):
	listd = []
	for i in range(len(records)):
		dict = {'first_name': '', 'last_name': '', 'percentage': 0}
		for j in range(len(records[i]['education']) - 1, -1, -1):
			if records[i]['education'][j]['institute'].lower() == institute_name.lower() and records[i]['education'][j]['ongoing'] == False:
				dict['first_name'] = records[i]['first_name']
				dict['last_name'] = records[i]['last_name']
				dict['percentage'] = records[i]['education'][j]['percentage']
				break
		if dict['first_name'] != '' and dict['last_name'] != '' and dict['percentage'] != 0:
				listd.append(dict)

	return listd

def find_topper_of_each_institute(records):

		institutes = []
		for i in range(len(records)):
			for j in range(len((records)[i]['education'])):
				for k in range(len((records)[i]['education'][j])):
					if (records)[i]['education'][j]['institute'] not in institutes:
						institutes.append((records)[i]['education'][j]['institute'])
		dict1 = {}
		dict2 = {}
		for i in range(len(institutes)):
			dict1[institutes[i]] = 0
			dict2[institutes[i]] = 0
		for i in range(len(institutes)):
			for j in range(len(records)):
				memory = records[j]['education']
				for k in range(len(memory)):
					if institutes[i] == memory[k]['institute']:
						if memory[k]['ongoing'] == False:
							if memory[k]['percentage'] > dict1[memory[k]['institute']]:
								dict2[memory[k]['institute']] = records[j]['id']
								dict1[memory[k]['institute']] = memory[k]['percentage']

		return dict2


def find_blood_donors(records, receiver_person_id):
	
		donors = {}
		receiverbg = records[receiver_person_id]['blood_group']
		if receiverbg == 'A':
			for i in range(len(records)):
				if records[i]['blood_group'] == 'A' or records[i]['blood_group'] == 'O':
					if records[i]['id'] != receiver_person_id:
						donors[records[i]['id']] = records[i]['contacts']

		if receiverbg == 'B':
			for i in range(len(records)):
				if records[i]['blood_group'] == 'B' or records[i]['blood_group'] == 'O':
					if records[i]['id'] != receiver_person_id:
						donors[records[i]['id']] = records[i]['contacts']
		if receiverbg == 'AB':
			for i in range(len(records)):
				if records[i]['blood_group'] == 'A' or records[i]['blood_group'] == 'B' or records[i][
					'blood_group'] == 'AB' or records[i]['blood_group'] == 'O':
					if records[i]['id'] != receiver_person_id:
						donors[records[i]['id']] = records[i]['contacts']

		if receiverbg == 'O':
			for i in range(len(records)):
				if records[i]['blood_group'] == 'O':
					if records[i]['id'] != receiver_person_id:
						donors[records[i]['id']] = records[i]['contacts']

		return donors

def get_common_friends(records, list_of_ids):
	unfiltered=[]
	for i in range(len(records)):
		for j in range(len(list_of_ids)):
			if list_of_ids[j]==records[i]['id']:
				unfiltered+=records[i]['friend_ids']
	level1=[]
	for i in range(len(unfiltered)):
		if unfiltered[i] not in level1:
			level1.append(unfiltered[i])
	level2=[]
	for i in range(len(level1)):
		if unfiltered.count(level1[i]) == len(list_of_ids):
			level2.append(level1[i])
	return level2
#*********************************************************************************************************************
def is_related(records, person_id_1, person_id_2):
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
	pass
#***********************************************************************************************************************

def delete_by_id(records, person_id):
	recordsnew = []
	for i in range(len(records)):
		if records[i]['id'] == person_id:
			del records[i]
			break
	for i in range(len(records)):
		if person_id in records[i]['friend_ids']:
			for j in range(len(records[i]['friend_ids'])):
				if records[i]['friend_ids'][j] != person_id:
					recordsnew.append(records[i]['friend_ids'][j])
				else:
					continue
			records[i]['friend_ids'] = recordsnew
	return records



def add_friend(records, person_id, friend_id):
	for i in range(len(records)):
		if records[i]['id'] == person_id:
			if friend_id not in records[i]['friend_ids']:
				records[i]['friend_ids'].append(friend_id)

	for i in range(len(records)):
		if records[i]['id'] == friend_id:
			if person_id not in records[i]['friend_ids']:
				records[i]['friend_ids'].append(person_id)

	return records


def remove_friend(records, person_id, friend_id):
	recordsx = []
	recordsy = []
	for i in range(len(records)):
		if records[i]['id'] == person_id:
			for j in range(len(records[i]['friend_ids'])):
				if records[i]['friend_ids'][j] != friend_id:
					recordsx.append(records[i]['friend_ids'][j])
				else:
					continue

			records[i]['friend_ids'] = recordsx
	for i in range(len(records)):
		if records[i]['id'] == friend_id:
			for j in range(len(records[i]['friend_ids'])):
				if records[i]['friend_ids'][j] != person_id:
					recordsy.append(records[i]['friend_ids'][j])
				else:
					continue

			records[i]['friend_ids'] = recordsy

	return records

def add_education(records, person_id, institute_name, ongoing, percentage):
	newedu = {}


	for i in range(len(records)):
		if records[i]['id'] == person_id:
			newedu['institute'] = institute_name
			newedu['ongoing'] = ongoing
			if ongoing == False:
				newedu['percentage'] = percentage
			records[i]['education'].append(newedu)
	return records

