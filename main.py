import csv, psutil
list = []
for process in psutil.process_iter():
    output = process.name()
    list.append(output)
with open("c:\script\k.csv", 'a') as file:
    append = csv.writer(file)
    append.writerow(list)
with open("c:\scriptk\k.html", 'a') as file:
    file.write(process.name())