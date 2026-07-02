import csv

name = input("whats you name?")
home = input("whats your housename?")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name" : name , "home" : home})