arrival_time = []
burst_time = []
waiting_time = [0]
finish_time = []
index=0
index1=0
size=0
print "Enter number of processes:"
size = input()
while index<size :
	print "Enter arrival times:"
	a = input()
	arrival_time.append (a)
	index+=1
while index1<size :
	print "Enter burst times:"
	b = input()
	burst_time.append (b)
	index1+=1

for x in range(size):
	a = burst_time[x] + arrival_time[x] + waiting_time[x]
	finish_time.append(a)
	if x<size-1:
		z = finish_time[x] - arrival_time[x+1]
		waiting_time.append(z)
	
print "Waiting time is: "
print waiting_time
print "Finish time is: "
print finish_time
