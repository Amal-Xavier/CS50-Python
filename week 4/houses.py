students = [{"name":"harry","house":"gryffindor"},
          {"name":"Draco","house":"gryffindor"}]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)