import time
import os
import subprocess
#------------------------------------------------------------
def check_file(filename):
	while True:
	    try:
	    	with open(filename) as file:
	    		file.close()
	    		return True
	    except IOError:
	    	continue

#------------------------------------------------------------

if (check_file('Omarson.log')):
	subprocess.run(': >Omarson.log', shell = True, stdout = subprocess.PIPE)
print("Starting to write log files")
file_name = 'dataplot.txt'
subprocess.run('sbatch run.sh', shell = True, stdout = subprocess.PIPE)
subprocess.call("perfomance.py", shell=True)
print('perfomance.py started succesfully')
if (check_file(file_name)):
	print('Still waiting for code to end...')
	time.sleep(8)
	
print('Results recorded succesfully!')
print('Process correct')
exit()
