import json
import unittest
import a2 as my

# NOTE:
# 1. Make sure your file is named as a2.py and in the same folder as tests.py
# 2. Make sure data.json is also in the same folder as tests.py
# 3. Make sure data.json is the same as the one given in the assignment
#    and no modifications have been done to it


def read_data_from_file(file_path='all_data.json'):
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


class TestIsRelated(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		person_id_1 = 200
		person_id_2 = 201
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = True # 200 -> 201
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		person_id_1 = 10
		person_id_2 = 11
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = True 
		# 10 -> 7 -> 19 -> 16 -> 38 -> 43 -> 9 -> 4 -> 53 -> 12 -> 30 -> 56 -> 97 -> 35 -> 17 -> 13 -> 88 -> 26 -> 24 -> 39 -> 8 -> 47 -> 15 -> 28 -> 5 -> 31 -> 36 -> 3 -> 27 -> 1 -> 62 -> 18 -> 21 -> 50 -> 79 -> 23 -> 84 -> 51 -> 46 -> 20 -> 42 -> 2 -> 25 -> 32 -> 14 -> 29 -> 68 -> 73 -> 106 -> 0 -> 33 -> 76 -> 52 -> 54 -> 58 -> 63 -> 89 -> 45 -> 109 -> 64 -> 83 -> 74 -> 75 -> 90 -> 57 -> 61 -> 93 -> 87 -> 66 -> 41 -> 37 -> 102 -> 70 -> 185 -> 92 -> 100 -> 98 -> 48 -> 34 -> 170 -> 111 -> 65 -> 22 -> 82 -> 94 -> 91 -> 121 -> 6 -> 135 -> 67 -> 11
		self.assertEqual(exp_output, user_output)
	

	def test_3(self):
		records = read_data_from_file()
		person_id_1 = 205
		person_id_2 = 102
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = False
		self.assertEqual(exp_output, user_output)


	def test_4(self):
		records = read_data_from_file()
		person_id_1 = 10
		person_id_2 = 200
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = False
		self.assertEqual(exp_output, user_output)

	
	def test_5(self):
		records = read_data_from_file()
		person_id_1 = 99
		person_id_2 = 202
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = False
		self.assertEqual(exp_output, user_output)


if __name__ == '__main__':
	unittest.main()
