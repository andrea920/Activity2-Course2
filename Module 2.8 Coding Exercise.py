#Instruction 1
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}

remove = groceries.pop("oranges")
print(groceries)

#Instruction 2
speakers = {"Sir Rafael": 54, "Ms.Joan": 33, "Ms.Dana": 67}

x = speakers.keys()
print(x)

#Intsruction 3
tryout_result = {"Carl": "passed", "Quentin": "failed", 
"Johhn Y.": "passed", "Peter": "failed", "Max T": "passed", 
"Joesph": "passed", "Jone": "failed", "Jorge": "failed", 
"George": "passed", "Ben": "passsed", "Jerome": "passed", "Rick": "failed", 
"Max G": "failed", "John P.": "failed", "Vince": "passed"}

print(tryout_result.get("Jorge"))