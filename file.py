import time
import os
import subprocess
#------------------------------------------------------------
def check_file(filename):
	while True:
	    try:
	    	with open(filename) as file:
	    		return True,file
	    except IOError:
	    	continue

#------------------------------------------------------------
file_name = 'dataplot2.txt'
#subprocess.run('sbatch run.sh ; python3 perfomance.py', shell = True, stdout=subprocess.PIPE)
if (check_file(file_name))[0]:
	print('Still waiting for code to end...')
	time.sleep(1)
	file = check_file(file_name)[1]
	file.close()
