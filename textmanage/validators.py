from django.core.exceptions import ValidationError
import datetime
from django.core.validators import RegexValidator
def get_gstin_with_check_digit(gstin_without_check_digit):

	factor = 1
	total = 0
	code_point_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	input_chars = gstin_without_check_digit.strip()
	if not input_chars:
		raise ValidationError("GSTIN supplied for checkdigit calculation is blank")
	mod = len(code_point_chars)
	for char in input_chars:
		digit = factor * code_point_chars.find(char)
		if digit < 0:
			raise ValidationError("GSTIN supplied for checkdigit contains invalid character")
		digit = (digit / mod) + (digit % mod)
		total += digit
		factor = 2 if factor == 1 else 1
	return ValueError

def datevalid(value):
    if value > datetime.date.today():
        raise ValidationError("The date can not be in future")
    return value
  
def nonneg(value):
    if value<0:
        raise ValidationError('Input can not be negative')


alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Name cannot contain digits')
phoneno = RegexValidator(r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$','Invalid Phone Number')
pincode = RegexValidator(r'^[1-9][0-9]{5}$','Invalid Pin Code')