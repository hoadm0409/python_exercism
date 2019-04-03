import re
from string import digits

class Phone(object):
	AREA_CODE_PATTERN = r'\(?[2-9]{1}[0-9]{2}\)?'
	EXCHANGE_CODE_PATTERN = r'[2-9]{1}[0-9]{2}'
	SUBCRIBER_NUMBER_PATTERN = r'[0-9]{4}'

	def __init__(self, phone_number):
		# preprocess: remove punctuation and the country code (1) if present
		phone_number = ''.join([c for c in phone_number if c in digits])
		if phone_number[0] == '1':
			phone_number = phone_number[1:]

		# validate phone number
		if len(phone_number) != 10:
			raise ValueError('phone number is invalid')

		self.number = phone_number
		self.area_code = self.number[0: 3]
		self.exchange_code = self.number[3: 6]
		self.subcriber_number = self.number[6:]

		if not re.match(Phone.AREA_CODE_PATTERN, self.area_code) \
			or not re.match(Phone.EXCHANGE_CODE_PATTERN, self.exchange_code) \
			or not re.match(Phone.SUBCRIBER_NUMBER_PATTERN, self.subcriber_number):
			raise ValueError('phone number is invalid')

	def pretty(self):
		return '({}) {}-{}'.format(self.area_code, self.exchange_code, self.subcriber_number)

if __name__ == '__main__':
	number = Phone("+1 (223) 456-7890")
	print(number.pretty())