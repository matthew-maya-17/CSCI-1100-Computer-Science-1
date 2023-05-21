import json
import BerryField
import Bear
import Tourist

file = input("Enter the json file name for the simulation => ")
print(file)
#file = "bears_and_berries_1.json"
f = open(file)
data = json.loads(f.read())
bf = (data["berry_field"])
ab = (data["active_bears"])
rb =(data["reserve_bears"])
at = (data["active_tourists"])
rt = (data["reserve_tourists"])


#creates tourist list
tourists = []
for x in range(len(at)):
    tourists.append(Tourist.Tourist(at[x][0],at[x][1]))
#creates bear list
bears =[]
for x in range(len(ab)):
    bears.append(Bear.Bear(ab[x][0],ab[x][1],ab[x][2]))

#prints everything    
berryfield = BerryField.BerryField(bf,tourists,bears)
print("\nField has {} berries.".format(berryfield.totalb()))
print(berryfield)
print("Active Bears:")
for x in range(len(bears)):
    print(bears[x])
print("\nActive Tourists:")
for x in range(len(tourists)):
    print(tourists[x])



