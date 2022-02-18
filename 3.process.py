print('Piyush Verma')
import csv,psutil
list = []

for process in psutil.process_iter():
    Name = process.name()  # Name of the process
    ID = process.pid  # ID of the process
    print("Process name =", Name, ",", "Process ID =", ID)

    output =  str(ID) + " " + Name
    list.append(output)
    # process.csv for csv file
    with open("C:/Users/Administrator.DEMO/Desktop/process1.csv", 'a') as file:
        append = csv.writer(file)
        append.writerow(list)
    # process.html for html file
    with open("C:/Users/Administrator.DEMO/Desktop/process2.html", 'a') as file:
        file.write(output)
