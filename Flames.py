import csv
from collections import Counter

with open("data2.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
#print(file_data)
#sorting data to get the weight of the people.
new_data=[]
for i in range(len(file_data)) :
  n_num = file_data[i][2]
  new_data.append(float(n_num))

# #getting the mean
n = len(new_data)
total = 0
for x in new_data:
    total+ = x

mean = total/n
#
print("Mean/Avrage is:"+str(mean))

#using floor division to get the nearest number whole number
#floor division is shown by //
if n % 2 ==0:
    #getting the first number
    meadian1 = float(new_data[n//2])
    #getting the second number
    meadian2 = float(new_data[n//2-1])
    #getting the mean of those numbers
    median = (meadian1+meadian2)/2
else:
    median = new_data[n//2]
    print(n)
    print("Median is:"+str(median))

#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {
         75-85:0,
         85-95:0,
         95-105:0,
         105-115:0,
         115-125:0,
         125-135:0,
         135-145:0,
         145-155:0,
         155-165:0,
         165-175:0
}
for weight,occurrence in data.items():
    if 75 <float(weight) <85:
        mode_data_for_range["75-85"]+=occurrence
    elif 85 <float(weight) < 95:
        mode_data_for_range["85-95"]+=occurrence
    elif 95<float(weight) < 105:
        mode_data_for_range["95-105"]+=occurrence
    elif 105 <float(weight) < 115:
        mode_data_for_range["105-115"]+=occurrence
    elif 115 <float(weight) < 125:
        mode_data_for_range["115-125"]+=occurrence
    elif 125 <float(weight) < 135:
        mode_data_for_range["125-135"]+=occurrence
    elif 135 <float(weight) < 145:
        mode_data_for_range["135-145"]+=occurrence
    elif 145 <float(weight) < 155:
        mode_data_for_range["145-155"]+=occurrence
    elif 155 <float(weight) < 165:
        mode_data_for_range["155-165"]+=occurrence
    elif 165 <float(weight) < 175:
        mode_data_for_range["165-175"]+=occurrence

mode_range,mode_occurrence=0,0
for range,occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range,mode_occurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence
mode= float((mode_range[0]-mode_range[1])/2)
print(f"Mode is->{mode:2f}")        