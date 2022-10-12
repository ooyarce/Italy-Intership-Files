import time as t
import logging

logging.basicConfig(filename="perfomance.log", 
					format='%(asctime)s %(message)s', 
					filemode='w')
Logger=logging.getLogger() 

#import numpy as np 
#import pyplotlib as plt
#-----------------------------------
def isfloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
#-----------------------------------

file_name = "Omarson.log" #automatizar esta linea
times = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5]
t0 = 0
t1 = t.perf_counter()
perf_times = []
ti = 0

Logger.info('-----------------------------------RESUME---------------------------------')

while True:
	t.sleep(1)
	temp_records = []
	temporal = []
	for t_i in times:
		with open (file_name) as log:

			for line in log.readlines():
				phrase = "t = "+str(t_i)[0:3]
				line2 = line[0:20]
				line3 = line2.split(' ')
				if len(line3) < 5 or isfloat(line3[4]) == False:
					continue

				num = line3[4]
				if phrase in line2 and t_i == float(num):
					t2 = t.perf_counter()
					t0 = t2-t1
					temp_records.append(t_i)
					temporal.append(t0)
					break
	log.close()

	if len(temporal) != 0 and len(perf_times) < len(times):
		Logger.info(f"\n-----------------------Iteration {ti}-------------------------")
		Logger.info(f'------------len of perf_times = {len(perf_times)}-------------------')
		Logger.info(f"---------------------Current ti = {times[len(perf_times)-1]}-----------------------")
		Logger.info(f"\nCurrent time = {t0}")
		perf_times.append(temporal)

	substracter = 0
	if len(perf_times) > len(temp_records):
		for i in range(len(perf_times)-1):
			i -=substracter
			if len(perf_times[i]) == len(perf_times[i+1]):
				perf_times.pop(i+1)
				substracter+=1
	
	ti+=1
	
	if len(temp_records) == 25:
		break

records = []
print(len(perf_times))
print(len(perf_times[-1]))
for i in range(len(perf_times)-1):
	records.append(perf_times[i][i])
records.append(t0)

Logger.info("---------------------FINAL RESULTS---------------------")
Logger.info(f"records = {records}")
Logger.info(f"lens de = {len(records)}, {len(times)}")

with open('dataplot.txt','w') as file:
	for i in range(len(times)):
		file.write(str(times[i])+ ' ' + str(records[i])+' \n')

file.close()