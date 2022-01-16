import unittest
from unittest.mock import patch
import a1 as my

# NOTE: make sure your file name is a1.py and is in the same folder as that of tests.py


ITEMS = {
    0: {'name': 'Tshirt'        , 'price': 500      , 'category': 'Apparels'},
    1: {'name': 'Trousers'      , 'price': 600      , 'category': 'Apparels'},
    2: {'name': 'Scarf'         , 'price': 250      , 'category': 'Apparels'},
    3: {'name': 'Smartphone'    , 'price': 20_000   , 'category': 'Electronics'},
    4: {'name': 'iPad'          , 'price': 30_000   , 'category': 'Electronics'},
    5: {'name': 'Laptop'        , 'price': 50_000   , 'category': 'Electronics'},
    6: {'name': 'Eggs'          , 'price': 5        , 'category': 'Eatables'},
    7: {'name': 'Chocolate'     , 'price': 10       , 'category': 'Eatables'},
    8: {'name': 'Juice'         , 'price': 100      , 'category': 'Eatables'},
    9: {'name': 'Milk'          , 'price': 45       , 'category': 'Eatables'}
}


# total test cases -> 10
class TestGetRegularInput(unittest.TestCase):

	@patch('a1.input', create=True)
	def test_1(self, user_input):
		user_input.side_effect = ['0 1 1 3 4 8 1 8']
		user_output = my.get_regular_input()
		exp_output = [1, 3, 0, 1, 1, 0, 0, 0, 2, 0]
		self.assertEqual(exp_output, user_output)


	# 2. with one negative itemcode
	@patch('a1.input', create=True)
	def test_2(self, user_input):
		user_input.side_effect = ['1 2 -3 5']
		user_output = my.get_regular_input()
		exp_output = [0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)

	
	# 3. with only one itemcode
	@patch('a1.input', create=True)
	def test_3(self, user_input):
		user_input.side_effect = ['7']
		user_output = my.get_regular_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 4. with only one -ve itemcode
	@patch('a1.input', create=True)
	def test_4(self, user_input):
		user_input.side_effect = ['-15']
		user_output = my.get_regular_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)

	
	# 5. with all same itemcodes
	@patch('a1.input', create=True)
	def test_5(self, user_input):
		user_input.side_effect = ['3 3 3 3 3 3 3 3 3 3 3']
		user_output = my.get_regular_input()
		exp_output = [0, 0, 0, 11, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 6. with all negative itemcode
	@patch('a1.input', create=True)
	def test_6(self, user_input):
		user_input.side_effect = ['-1 -2 -3 -4']
		user_output = my.get_regular_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 7. with itemcodes greater than 9
	@patch('a1.input', create=True)
	def test_7(self, user_input):
		user_input.side_effect = ['100 100 10 100 1000']
		user_output = my.get_regular_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 8. with empty list
	@patch('a1.input', create=True)
	def test_8(self, user_input):
		user_input.side_effect = ['']
		user_output = my.get_regular_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 9. with 100 itemcodes
	@patch('a1.input', create=True)
	def test_9(self, user_input):
		user_input.side_effect = ['6 0 9 0 2 4 3 0 9 2 1 10 9 5 2 4 0 6 9 6 1 5 3 7 2 2 6 7 5 0 2 2 9 6 2 8 10 6 1 6 1 3 1 6 10 4 4 8 10 1 5 8 9 7 9 3 8 4 0 10 2 10 6 3 1 8 10 7 1 9 6 9 3 4 5 1 3 9 8 8 0 1 6 0 0 10 6 5 2 0 5 5 10 7 2 0 3 2 4 3']
		user_output = my.get_regular_input()
		exp_output = [11, 10, 12, 9, 7, 8, 12, 5, 7, 10]
		self.assertEqual(exp_output, user_output)

	
	# 10. with 200 quantities with negative ones
	@patch('a1.input', create=True)
	def test_10(self, user_input):
		user_input.side_effect = ['2 20 -9 9 -9 -5 -1 20 20 -3 -9 8 -5 -7 10 8 1 16 -5 -1 20 17 -9 2 9 14 3 -8 1 14 -4 5 -5 -5 2 15 14 20 4 20 14 0 18 -9 -5 16 18 -5 8 12 3 -6 6 10 18 12 2 -7 2 20 16 -7 -3 -7 3 13 10 -1 13 -1 7 10 17 18 -7 1 16 19 6 9 5 9 -3 7 -1 -10 11 -5 20 11 2 12 -3 -7 6 10 14 5 -7 8 18 2 8 -4 -1 1 -8 18 -4 9 17 7 6 -10 -8 2 15 -9 -10 10 16 3 0 16 19 -5 13 -9 1 0 10 5 15 -5 -10 -4 -6 -1 20 16 -4 -3 18 -3 2 9 7 8 9 3 17 7 14 -10 -6 -10 -7 -10 16 -9 11 14 14 -5 -7 12 2 -8 -10 11 3 13 11 -5 9 3 18 -9 7 -5 -9 12 2 8 4 4 0 -5 -9 2 10 4 5 20 12 12 1 11 -8 -6']
		user_output = my.get_regular_input()
		exp_output = [4, 6, 12, 7, 4, 5, 4, 6, 7, 8]
		self.assertEqual(exp_output, user_output)


# total test cases -> 6
class TestGetBulkInput(unittest.TestCase):

	# 1. with few negative quantities
	@patch('a1.input', create=True)
	def test_1(self, user_input):
		user_input.side_effect = [
			'1 50',
			'3 10',
			'1 20',
			'4 -5',
			'25 2',
			'25 -5',
			''
		]

		user_output = my.get_bulk_input()
		exp_output = [0, 70, 0, 10, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)
	
	# 2. with empty shopping cart
	@patch('a1.input', create=True)
	def test_2(self, user_input):
		user_input.side_effect = [
			''
		]

		user_output = my.get_bulk_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)

	
	# 3. with 0 quantity of item code 0
	@patch('a1.input', create=True)
	def test_3(self, user_input):
		user_input.side_effect = [
			'99 -5',
			'5 -2',
			'-3 2',
			'0 0',
			''
		]

		user_output = my.get_bulk_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 4. with same itemcode appearing multiple times, quantity should only increase
	@patch('a1.input', create=True)
	def test_4(self, user_input):
		user_input.side_effect = [
			'5 50',
			'5 30',
			'5 -70',
			'5 0',
			'5 7',
			''
		]

		user_output = my.get_bulk_input()
		exp_output = [0, 0, 0, 0, 0, 87, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


	# 5. with 100 input strings with few negative quantities
	@patch('a1.input', create=True)
	def test_5(self, user_input):
		user_input.side_effect = ['9 -92', '6 23', '9 -97', '3 18', '7 -29', '2 -92', '8 25', '5 -81', '3 90', '5 -89', '6 -65', '9 -10', '6 7', '4 72', '4 16', '2 75', '4 69', '5 -66', '7 96', '3 12', '9 -4', '0 49', '0 -40', '2 -51', '4 37', '5 97', '3 -20', '8 15', '6 20', '1 67', '9 -17', '8 -60', '3 5', '3 -91', '0 27', '4 55', '1 36', '1 -62', '6 45', '5 53', '2 -72', '1 13', '2 -52', '5 10', '6 14', '3 74', '4 -64', '9 33', '2 -70', '4 16', '4 -58', '2 99', '2 22', '5 -17', '6 -43', '0 39', '0 -16', '5 -38', '1 -33', '7 3', '9 -60', '6 26', '3 88', '8 -31', '8 23', '9 27', '1 -58', '7 72', '7 2', '2 7', '8 49', '5 37', '6 25', '2 43', '7 -75', '6 -91', '0 12', '8 -84', '0 -11', '1 -62', '1 55', '7 24', '2 17', '6 98', '8 14', '5 85', '4 78', '7 8', '5 66', '8 33', '2 89', '3 -18', '9 -92', '3 64', '9 47', '7 -94', '1 -25', '6 -37', '4 -78', '0 52', '']
		user_output = my.get_bulk_input()
		exp_output = [179, 171, 352, 351, 343, 348, 258, 205, 159, 107]
		self.assertEqual(exp_output, user_output)


	# 6. with 100 input strings with all wrong input codes
	@patch('a1.input', create=True)
	def test_6(self, user_input):
		user_input.side_effect = ['-27 4', '-46 61', '-27 1', '-74 59', '-38 35', '-17 20', '-96 66', '-38 41', '-91 31', '-5 46', '-95 53', '-83 77', '-55 48', '-47 36', '-14 33', '-42 22', '-13 38', '-16 46', '-83 58', '-2 30', '-44 78', '-52 5', '-26 0', '-70 17', '-76 38', '-32 46', '-2 30', '-60 85', '-30 57', '-45 60', '-92 83', '-26 41', '-36 20', '-72 52', '-70 4', '-96 63', '-62 77', '-16 9', '-32 10', '-81 49', '-28 47', '-24 19', '-86 99', '-2 12', '-44 21', '-76 44', '-45 53', '-43 31', '-13 35', '-82 79', '-34 22', '-85 34', '-42 38', '-79 84', '-17 22', '-1 22', '-39 98', '-56 41', '-45 28', '-100 69', '-9 5', '-58 40', '-69 10', '-67 57', '-49 74', '-80 49', '-37 86', '-70 94', '-33 34', '-34 61', '-23 63', '-92 21', '-38 86', '-41 51', '-83 53', '-31 74', '-56 68', '-51 62', '-11 21', '-29 56', '-88 53', '-96 0', '-44 68', '-92 6', '-56 11', '-81 13', '-23 58', '-38 17', '-42 55', '-1 64', '-43 43', '-8 33', '-11 58', '-46 42', '-17 66', '-34 19', '-6 30', '-59 79', '-96 87', '-75 82', '']
		user_output = my.get_bulk_input()
		exp_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(exp_output, user_output)


# total test cases -> 4
class TestCalculateCategoryWiseCost(unittest.TestCase):
	
	# 1. with normal quantities with few 0
	def test_1(self):
		quantities = [1, 3, 0, 1, 1, 0, 0, 0, 2, 0]
		user_output = my.calculate_category_wise_cost(quantities)
		exp_output = (2300, 50000, 200)
		self.assertEqual(exp_output, user_output)


	# 2. with normal quantities
	def test_2(self):
		quantities = [344, 458, 595, 904, 655, 571, 313, 626, 329, 411]
		user_output = my.calculate_category_wise_cost(quantities)
		exp_output = (595550, 66280000, 59220)
		self.assertEqual(exp_output, user_output)


	# 3. with empty cart
	def test_3(self):
		quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		user_output = my.calculate_category_wise_cost(quantities)
		exp_output = (0, 0, 0)
		self.assertEqual(exp_output, user_output)


	# 4. with normal quantities
	def test_4(self):
		quantities = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
		user_output = my.calculate_category_wise_cost(quantities)
		exp_output = (1350, 100000, 160)
		self.assertEqual(exp_output, user_output)


# total test cases -> 6
class TestCalculateDiscountedPrices(unittest.TestCase):
	# 1. normal case
	def test_1(self):
		costs = (2300, 50000, 200)
		user_output = my.calculate_discounted_prices(*costs)
		exp_output = (2070, 45000, 200)
		self.assertEqual(exp_output, user_output)


	# 2. with discount in 2 categories
	def test_2(self):
		costs = (42000, 200000, 0)
		user_output = my.calculate_discounted_prices(*costs)
		exp_output = (37800, 180000, 0)
		self.assertEqual(exp_output, user_output)


	# 3. with discount in all 3 categories
	def test_3(self):
		costs = (595550, 66280000, 59220)
		user_output = my.calculate_discounted_prices(*costs)
		exp_output = (535995, 59652000, 53298)
		self.assertEqual(exp_output, user_output)


	# 4. with all 0 cost
	def test_4(self):
		costs = (0, 0, 0)
		user_output = my.calculate_discounted_prices(*costs)
		exp_output = (0, 0, 0)
		self.assertEqual(exp_output, user_output)


	# 5. with discount in only 1 category
	def test_5(self):
		costs = (1350, 100000, 160)
		exp_output = (1350, 90000, 160)
		user_output = my.calculate_discounted_prices(*costs)
		self.assertEqual(exp_output, user_output)


	# 6. with no discount
	def test_6(self):
		costs = (1350, 900, 160)
		exp_output = (1350, 900, 160)
		user_output = my.calculate_discounted_prices(*costs)
		self.assertEqual(exp_output, user_output)


# total test cases -> 5
class TestGetTax(unittest.TestCase):

	# normal case
	def test_1(self):
		costs = (2070, 45000, 200)
		user_output = my.calculate_tax(*costs)
		exp_output = (54237, 6967)
		self.assertEqual(exp_output, user_output)


	# with one 0 cost
	def test_2(self):
		costs = (37800, 180000, 0)
		user_output = my.calculate_tax(*costs)
		exp_output = (248580, 30780)
		self.assertEqual(exp_output, user_output)


	# with random costs
	def test_3(self):
		costs = (535995, 59652000, 53298)
		user_output = my.calculate_tax(*costs)
		exp_output = (69245356, 9004063)
		self.assertEqual(exp_output, user_output)


	# all 0 costs
	def test_4(self):
		costs = (0, 0, 0)
		user_output = my.calculate_tax(*costs)
		exp_output = (0, 0)
		self.assertEqual(exp_output, user_output)


	# two 0 costs
	def test_5(self):
		costs = (0, 0, 160)
		user_output = my.calculate_tax(*costs)
		exp_output = (168, 8)
		self.assertEqual(exp_output, user_output)


# total test cases -> 9
class TestApplyCouponCode(unittest.TestCase):
	
	# wrong coupon applied
	@patch('a1.input', create=True)
	def test_1(self, user_input):
		total_cost = 54237
		user_input.side_effect = [
			'ABCD99',
			''
		]

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (54237, 0)
		self.assertEqual(exp_output, user_output)


	# correct input applied
	@patch('a1.input', create=True)
	def test_2(self, user_input):
		total_cost = 248580
		user_input.side_effect = [
			'CHILL50'
		]

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (238580, 10000)
		self.assertEqual(exp_output, user_output)


	# random coupon codes applied - all wrong
	@patch('a1.input', create=True)
	def test_3(self, user_input):
		total_cost = 69245356
		user_input.side_effect = ['3Q0HECM', 'G8YX163IFHGFB9', 'E1YS8CFZ6', 'GYSL3ICYG', 'D6L8NXOD38Q', '4WUII4WE', '6WS10TIYYIG1', 'AJO95V9NA3I', 'ZOF7017IURI8Z', 'E4CBQHR', '7EEW1BY1KH18', 'U8SHX42UQ6XP', 'OFV4T9QKXMUVY', 'UJEBKMFPF', '80N1BJZZ7', '1EQMJ9UCO', 'BMADFFP5', 'JBTQXLXR', 'U9CSOU9KFO1', 'UOGKWKRSJ', '2KVOUVKZR8JV', '63Q5OREWGZ0Y', 'GSY162K', '732ZM5S', '6J9FFE1ODYYV', '06SK4IGNY7X', 'K4M21GRAJ', 'N62ACNFE2K1H', 'ZFKOCMTI', '0GCNPVZH', '62MMF41V4', 'ZFB8G9KY3', '6XS4O5O5B0A', 'IVJTGOJA67', 'TIGM90TUFPA', 'ZRG0YSPH804L', 'QGLIB3IO0B', 'I3DXSRG', 'QWSXOFOP554EZ9', 'HHTSZADM', 'XZDGQJPWU', '93MXHEFGUYJ', 'FJM38C6V', 'LOCFEPY64S1', 'IQ987COZFCR5ZT', '8NXFW2Y8F8', '5CTVDO019A', 'RZPPI05TRRV', '2VPX6YERE', 'YCYTP3A1G0XJ', 'EB7JG9ZEBIUND', '2FPOR6RJ3L5HCY', 'RKADCFTFH85K', 'DI5DYODKD', 'SQQGXDLXTCR', 'F6XW40HO', '1JJOLKQF8NZ1', 'Z601PV92D', '590CTTQY', 'S8QX88Y9', 'EY63CCZP3L62M', 'BXGDE9FI03I', 'UF5MH46T', 'LAD4WTUFA0', '79V1REVLXU', 'QB5XDA4QD4C', 'A0E9XYS8YUSEN', 'YDUVDW0YU7MEHU', 'PZIYF10FQQX4AJ', '05GOSVTG21', 'HCISQDK5Z9XEK', 'QVZXDSKHRXS', 'A9RS0VMBOLYW', 'TONN8RU', '3U4P4EINY', 'VHKQPO6N', '4O70LN689ZD4F', '87NR7FHEI9TZMI', 'M0L6CRIG6U8P4', 'XOVYAD11AZ', 'ZQ5S96K6FHP2X', '66YX9MO10V57FR', 'F13G7XDE', '2H9YG7OVIY', 'XG53WIQW', 'Y6TI7V8Z51HEI', 'ZGQ3DJ6', 'BIRATBBO4M2G6D', '9D7CCS4REBQ', 'NW9Q387EV81JEU', 'YH24TD1UG5CL', 'R45MSWU1', '51Y7VBYA4N5P', 'PQ2Z8SCYQP28Y', '78F23PDK3NM', 'SL4HDYY0', 'DLGR72U3DR5RK', '2E0AZ1P9RMJK2', 'OZFYPJ95ZE', 'G1Z9SL9HSE', 
		'']

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (69245356, 0)
		self.assertEqual(exp_output, user_output)


	# random coupon codes applied - only last is correct
	@patch('a1.input', create=True)
	def test_4(self, user_input):
		total_cost = 69245356
		user_input.side_effect = ['PE9RIIEWMICB3', 'MNO6O5IQDGFL', '4TKSS79TU', 'XDLHTCIYZY', 'J3AYV6HMH4SA', '74TUDO1A', 'G9MFBFCI559H0', 'RPMBMX6AUKC', 'F65IX0DN13RF', '2L3WDGSGAERVD', 'CU1YIDXGSXQ4TH', 'YE3WEZRYP845', 'YKT19JZP17UIPP', '8K88WY7S8ER98I', '3WOYM63AIPL6FC', 'TOYZM49G3EE5L', 'L2RJJA4W3', 'PB9EPGRS', 'LJTH5TDTF7LFS2', 'EEC5IZF9RPHZ', '9H34M6R0FMA56', 'U0GGZ5EQK', 'VZFJOCNJMPZYCA', 'GWOAMWHWN', 'PG7AWXR9R', 'FYSHW75Q', 'IFJIE6H', '4U1CK7QO59BA4', 'TZBWM7N', 'P0B7Z08W', 'RKF81LIBC', 'M22JIONWGINS', 'MTPOWSWC3', 'ML82H0L8R3', '86HE7G10G7TBRJ', 'X6394US86Z', 'XOQQJNODRQMJ2', 'M8CHYH40UMQ', '9EGGQIAM10AWZG', '92WQH0NH1WK', 'ERL5DTTU7EC', '21G5QHFJ', 'YD0XSNLVCP', 'DP34X8XOO', 'CXD9XNV1DIF', 'NHODK7DV8AWRSJ', 'YUCVN3TDZJ', 'LBQIONTXN', 'ICEZ2F8UMZ1SW', 'GB5RQ9SRDIJNF', '741U00I3P17', 'RMBHRDS7', 'W775H4IUTZAIYY', '26K4N1S', 'SVKRFZ2FGJ', 'SW5NME11G3', '7MX6DQFXPI', 'LNT6QNET', '1WHZA607W', 'M5F2216ALBY2TJ', 'PZH4NJBY5ZZXA', 'GGXR16KU', 'DB5CYOIR3O', '508Z6M9JD', 'NYSSVHQE', 'A7NQXRN3JW', 'W8MLW1D',
		'CHILL50']

		user_output = my.apply_coupon_code(total_cost)
		print(user_output)
		exp_output = (69235356, 10000)
		self.assertEqual(exp_output, user_output)


	# random coupon codes applied - only last is correct
	@patch('a1.input', create=True)
	def test_5(self, user_input):
		total_cost = 69235356
		user_input.side_effect = ['9S1LZ4XYIE', 'JD57R70MO0E', 'Z6VPV2MBIRDU', 'BY5CP5I1DLW', 'M6H8MQXMO466BY', 'R4HT0M4BZH8', '2HJXDK4', '8DEIYFD', 'S09G6YGCM', 'FIICVM87GYXOYF', 'TWM23G3G5W', 'SBBC2ZDN', '9682FOA4OD54OY', 'SMET726X', 'F1RZRYST4Z1RC', '42B227F8T', 'ACLDO2XS', '9D7GSUY', 'TMYBR7KM2FN', 'P01GO76JXG', 'QTVSDCUBQ', '8FG1BC1OR', 'KITEL2S659Y9WN', '2LGGCBSUI1T4', 'W4RD5L9XD0E6V', 'EH0XJ9H64F5', 'EMLUCMD1U9ZS5', 'GRA10QZ', 'GRN0S1ZVJQ1YM', 'QHBYBJ5W', '0PML4BYSTFU9O', '1HAN0PH7AYQ', 'UGCLUXQ6GLKUFU', 'W7PIMXK', '4ZP5BJ3', 'IA3ZCAW7SJJCPD', 'HXVJYQBHPBC4', 'O03I245LMJ', 'JP03F2ALRG', 'YR1EIVOL', 'SBP3VM5YUS', 'E9HVW9A4YYTU', 'PF27VDSTBKMKGI', 'C6H74NQ', '47B7IR79', 'FQDS6P1V9', 'Z0NVCYBJV', '7A0H7ZX41D9', 'KMGNUAPREC', 'Q83SZGVI', '99C9WVGWSS7IO3', 'ZDUA39FVUAUXOD', 'SFC1C8G62OAL', '057Q5PZM', '62JBAXF', 'RZWTUV5', 'YT7ZTSXHK63R', '8XQT1NX5GRIMNX', 'AL779R0NKF', '1RKDQEU', '1NJVWYBI', 'MOJ3X7MKG7MHO', 'TU5KTT0HYFWL', 'HNZNO02KF4CQ', 'HER8VKG9T0', 
		'HELLE25']

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (69230356, 5000)
		self.assertEqual(exp_output, user_output)


	# no coupon applied
	@patch('a1.input', create=True)
	def test_6(self, user_input):
		total_cost = 248580
		user_input.side_effect = [
			''
		]

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (248580, 0)
		self.assertEqual(exp_output, user_output)


	# with total_cost = 0
	@patch('a1.input', create=True)
	def test_7(self, user_input):
		total_cost = 0
		user_input.side_effect = ['9S1LZ4XYIE', 'JD57R70MO0E', 'Z6VPV2MBIRDU', 'BY5CP5I1DLW', 'M6H8MQXMO466BY', 'R4HT0M4BZH8', '2HJXDK4', '8DEIYFD', 'S09G6YGCM', 'FIICVM87GYXOYF', 'TWM23G3G5W', 'SBBC2ZDN', '9682FOA4OD54OY', 'SMET726X', 'F1RZRYST4Z1RC', '42B227F8T', 'ACLDO2XS', '9D7GSUY', 'TMYBR7KM2FN', 'P01GO76JXG', 'QTVSDCUBQ', '8FG1BC1OR', 'KITEL2S659Y9WN', '2LGGCBSUI1T4', 'W4RD5L9XD0E6V', 'EH0XJ9H64F5', 'EMLUCMD1U9ZS5', 'GRA10QZ', 'GRN0S1ZVJQ1YM', 
		'HELLE25', 
		'']

		user_output = my.apply_coupon_code(total_cost)
		print(user_output)
		exp_output = (0, 0)
		self.assertEqual(exp_output, user_output)


	@patch('a1.input', create=True)
	def test_8(self, user_input):
		total_cost = 1000
		user_input.side_effect = [
			'helle25',
			'HeLLe25',
			'HELLE50',
			'CHILL25',
			'chill50',
			''
		]

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (1000, 0)
		self.assertEqual(exp_output, user_output)

	
	@patch('a1.input', create=True)
	def test_9(self, user_input):
		total_cost = 1000
		user_input.side_effect = [
			'',
			'wrong1',
			'asdghf789'
			'CHILL50'
		]

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (1000, 0)
		self.assertEqual(exp_output, user_output)


if __name__ == '__main__':
	unittest.main()
