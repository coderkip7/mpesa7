# list data structure,it is ordered and changeble
cars =['Mercedes','Nissan','Toyota','Range']
cars[2]="Subaru"
cars.append("Mitsubishi")
cars.insert(2,"Rolls Royce ")
cars.reverse()
cars.remove("Range")
print(cars)
#this is a tuple, its unchangeable
fruits=("Mangoes","Oranges","Pineapples","Bananas")
#fruits.count(3)
for x in fruits:
    print(x)

#sets datastructure,unordered

countries={"Kenya","Sweden","Rwanda","France","Korea"}
print(countries)

#dictionaries

matunda={
    "amount":40,
    "jina":"Ndizi",
    "rangi":"Yellow"
}
matunda["size"]="Large"
matunda.pop("size")
for m in matunda:
    print(m)
print(matunda)
