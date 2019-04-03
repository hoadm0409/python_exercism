from string import ascii_uppercase, digits
from random import sample
import random


class Robot(object):
    def __init__(self):
    	self.generate_name()


    def reset(self):
    	self.generate_name()


    def generate_name(self):
    	random.seed()
    	self.name = ''.join(sample(ascii_uppercase, 2)) + ''.join(sample(digits, 3))
