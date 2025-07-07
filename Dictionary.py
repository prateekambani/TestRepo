
#Dictionary is nothing but key value parts

d1 = {}

d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "Prateek":"Roti",
      "Shubham":{"B":"maggie","L":"roti","D":"Rajma"}}

print(d2["Prateek"])

print(d2["Shubham"])
print(d2["Shubham"]["B"])

d2["Ankit"] = "Junk Food"
print(d2)

d2["Aunrangzeb"]="Kebabs"
print(d2)

del d2["Aunrangzeb"]
print(d2)

#copy helps to create new dictionary
d3 = d2.copy()
del d2["Rohan"]
print(d2)
print(d3)


#update
d2.update({"Leena":"Tofee"})
print(d2)

print(d2.keys())
print(d2.items())
