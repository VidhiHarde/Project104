import csv
with open("HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

#calculating median.
n = len(new_data)
new_data.sort()

if n%2 == 0:
#getting first number.    
    median1 = float(new_data[n//2])
#getting second number.    
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
    print(n)
print("Median is -> "+str(median))        
