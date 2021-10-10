
# python 3.5 or above

import numpy as np
import cmath as cm
import math  as m

round_digits = 14


def zl2gamma(ZL, Z0=50):
	num = (ZL - Z0)/(ZL + Z0)
	num2 = round(num.real, round_digits) + round(num.imag, round_digits) * 1j
	return num2


def zl2vswr(ZL, Z0=50):
	top = 1 + abs(gamma(ZL,Z0))
	if top != 2:
		bot = 2 - top
		ret = round(top/bot, round_digits)
	else:
		ret = m.inf
	return ret

def gamma2vswr(g):
	top = 1 + abs(g)
	if top != 2:
		bot = 2 - top
		ret = round(top/bot, round_digits)
	else:
		ret = m.inf
	return ret

def gamma2zl(g, Z0 = 50):
	top = 1 + g
	if top != 2:
		bot = 2 - top
		ret = round(Z0 * top/bot, round_digits) 
	else:
		ret = m.inf
	return ret


def cart2pol(val):
	x = val.real
	y = val.imag
	rho = round(np.sqrt(x**2 + y**2), round_digits)
	phi = round((180/m.pi) * np.arctan2(y, x), round_digits)
	return(rho, phi)


def pol2cart(rho, phi):
	x = round(rho * np.cos(phi*m.pi/180), round_digits)
	y = round(rho * np.sin(phi*m.pi/180), round_digits) * 1j
	return(x + y)















