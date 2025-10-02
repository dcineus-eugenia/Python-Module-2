# Exercice 1

# Fruit_list = ["Mango", "Blueberries", "Strawberries", "Orange"]
# print(Fruit_list)

# Fruit_list.append("Pineapple")
# print(Fruit_list)

# Fruit_list.extend(["Banana","Cherries","Apple"])
# print(Fruit_list)

# Fruit_list.remove("Mango")
# print(Fruit_list)

# popped_item = Fruit_list.pop(2)
# print(Fruit_list)

# Fruit_list.sort()
# print(Fruit_list)

# First_three = Fruit_list[:3]
# print("Original list:", Fruit_list)
# print("First three fruits:",First_three)

# # Exercice 2 

# Colors_ = ("Red","Blue","Green","Yellow","Purpule")
# print(Colors_)
# print("Original tuple:", Colors_)

# Count_Red = Colors_.count("Red")
# print("Count of red:", Count_Red)

# Index_Blue = Colors_.index("Blue")
# print("Index of blue:", Index_Blue)

# New_colors = ("Magenta","Black")
# Combined_tuples = Colors_ + New_colors
# print(Combined_tuples)

# Exercice 3

# Persone = { "name" : "Alice" ,"age" : 42 ,"City" : "London" }
# print("Original dictionary:", Persone)

# Persone["Occupation"] = "Lawyer"
# print("\nAfter adding occupation:", Persone)

# Persone.update({"age" : 43})
# print("Uptaded age:", Persone)

# print(Persone.values())
# print(Persone.keys())

# print(Persone.get("City"))
# print("\n Is 'name' a key in dictionary:", "name" in Persone)
# print("\n Is 'London' a value in dictinary:", "London" in Persone["City"])
# print(Persone)

# Exercice 4

Set_of_numb_1 = {0,1,2,3,4,5,6,7,8,9,10}
Set_of_numb_2 ={0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5}
Set_3 = Set_of_numb_1.union(Set_of_numb_2)
Set_4 = Set_of_numb_1 | Set_of_numb_2
print(Set_3)
print(Set_4)



