import matplotlib.pylab as plt
import subprocess
model_name = raw_input('Write Model name: ')
print(f'Model name = {model_name}')
times = [0.0]
records = [0]

with open('dataplot.txt','r') as file:
	for line in file.readlines():
		line2 = line.split(' ')
		times.append(float(line2[0]))
		records.append(float(line2[1]))

plt.plot(times,records)
#plt.yticks([1,10,60,600,1800,3600,5400,7200],["1s", "10 s", "1min", "10min", "30min", "1hr", "1.5hrs", "2hrs"])
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5],['0.5','1','1.5','2','2.5','3','3.5','4','4.5','5'])
plt.yticks([10,60,150,300],["10 s", "1min", "2.5min","5min"])
plt.grid()
plt.title(f'Perfomance {model_name}')
plt.ylabel('Calculus time [s]')
plt.xlabel('Time step [s]')
plt.savefig(f'{model_name}.png')
plt.show()

subprocess.run('zip results.zip rec5.part-*.mpco Omarson.log Base_Model.png', shell = True, stdout=subprocess.PIPE)
print("Correct process!!")
subprocess.run('exit', shell = True, stdout=subprocess.PIPE)