import os 
import sys 
try:
	os.mkdir('new1')
	print('directory created')
	
	raise RuntimeError('runtime error occured')
	
except FileExistsError:
	print(‘Directory is already created’)
