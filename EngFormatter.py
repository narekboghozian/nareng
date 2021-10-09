
import math as m

def printEng( num, unit = ' ' ):
	units_pre = [[' ', 'k', 'M', 'G', 'T', 'P', 'E']\
	,[' ', 'm', 'μ', 'n', 'p', 'f', 'a']]
	


	x = abs(num)
	exp = 0
	neg = 0

	if (num < 0):
		neg = 1

	if num == 0:
		mag = 0
	else:

		mag = m.log(x, 10)
	
	small = 0
	if (x > 1):
		exp = m.floor(mag)
	elif (x < 1):
		exp = m.floor(mag)
		small = 1
	

	power = (m.floor(exp/3))*3
	

	unit_pre = ' '
	if (abs(exp) < 21):
		unit_pre = units_pre[small][abs(m.floor((exp)/3))]
	else:
		unit_pre = 'E' + str(power) + ' '

	if unit.lower() =='ohm' or unit.lower()=='ohms':
		unit = 'Ω'
	elif unit.lower() == 'farad' or unit.lower() == "farads":
		unit = 'F'

	new_num = num / 10**(power)

	print(str(round(new_num,6)) + ' ' + unit_pre + unit)
