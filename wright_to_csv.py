import csv

with open('pytocsv.csv', 'w', newline='') as tf:
    writer = csv.writer(tf)
    writer.writerow(["SN", "Name", "Area"])
    writer.writerow([1, "Ranjan Bharadvaj", "Banglore"])
    writer.writerow([2, "Harish", "shima"])
    writer.writerow([3, "Satish", "delhi"])
