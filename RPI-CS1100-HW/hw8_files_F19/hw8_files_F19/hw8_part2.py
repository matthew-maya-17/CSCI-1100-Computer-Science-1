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
#prints starting configuration
print("\nStarting Configuration")   
#creates berryfield with berryfield and bear and tourist lists 
berryfield = BerryField.BerryField(bf,tourists,bears)
print("Field has {} berries.".format(berryfield.totalb()))
print(berryfield)
print("Active Bears:")
for x in range(len(bears)):
    print(bears[x])
print("\nActive Tourists:")
for x in range(len(tourists)):
    print(tourists[x])
#variable for what turn we are on
turn = 1
while True:
    #prints out the turn
    if turn == 1:
        print("\nTurn: {}".format(turn))
    else:
        print("\n\nTurn: {}".format(turn))
    #grows and spreads berries
    berryfield.growb()
    berryfield.spreadb()
     #sees if any tourists and bears occupy the same spot
    for b in range(len(bears)):
         for t in range(len((tourists))):
             if  bears[b].r == tourists[t].r  and bears[b].c == tourists[t].c:
                 #kills tourist and give bear a kill
                 tourists[t].die = True
                 bears[b].kill = True
   
    
     
    #counter for seeing how many tourists get removed for list to avoid errors
    counter = 0
    #loops through to see whaat tourists went from chilling to a snack real quick
    for t in range(len(tourists)):
        if tourists[t-counter].die == True or tourists[t-counter].scared == True:
            print("{} - Left the Field".format(tourists[t-counter]))
            tourists.remove(tourists[t-counter])
            counter += 1
    #loops through all the bears every turn
    for b in range(len(bears)):
        #if the bear got a kill it takes a quick nap
        if bears[b].kill == True:
            bears[b].sleep = True
            bears[b].turns = 4
            bears[b].kill = False
        #if bear is napping then it incremments how many turns its been
        if bears[b].sleep == True:
            bears[b].turns -= 1
        #once bear runs out of turns it wakes up
        if bears[b].turns == 0:
            bears[b].sleep = False
        #if the bear is awake and has not bailed yet it continues
        if bears[b].sleep == False and bears[b].left == False:
            while True:
                #bear eats all the bears leave the field with 0 berries at that spot
                bears[b].eat += berryfield.field[bears[b].r][bears[b].c]
                berryfield.field[bears[b].r][bears[b].c] = 0
                #moves bear
                bears[b].move()
                #check to see if a tourist get eaten, if it does then bear stops moving
                for t in range(len((tourists))):
                    if  bears[b].r == tourists[t].r  and bears[b].c == tourists[t].c:
                        tourists[t].die = True
                        bears[b].kill = True              
                if bears[b].kill == True:
                    break
                #if bear goes off field he stops moving  
                if bears[b].r > len(berryfield.field)-1:
                    bears[b].left = True
                    break
                elif bears[b].c > len(berryfield.field)-1:
                    bears[b].left = True
                    break
                elif bears[b].r < 0:
                    bears[b].left = True   
                    break
                elif bears[b].c < 0:
                    bears[b].left = True
                    break
                   #bear eats all the bears leave the field with 0 berries at that spot
                bears[b].eat += berryfield.field[bears[b].r][bears[b].c]
                berryfield.field[bears[b].r][bears[b].c] = 0
                # if bear eats more than 30 bearries turn stops and the extra beries go back
                if bears[b].eat >= 30:
                    berryfield.field[bears[b].r][bears[b].c] =  bears[b].eat - 30
                    break
        #resets for next turn
        bears[b].eat = 0
    
    
     #sees if a bear eats a tourist
    for b in range(len(bears)):
         for t in range(len((tourists))):
             if  bears[b].r == tourists[t].r  and bears[b].c == tourists[t].c:
                 tourists[t].die = True
                 bears[b].kill = True
      #if the tourist is alive it looks around to see if a bears around                  
    for t in range(len(tourists)):
        if tourists[t].die == False:
            if tourists[t].sees(bears) >= 3:
                tourists[t].scared = True
            if tourists[t].sees(bears) > 0:
                tourists[t].turns = 0
            if tourists[t].sees(bears) == 0:
                tourists[t].turns += 1
     #if a tourist has not seen a bear for 3 turns they bail           
    for t in range(len(tourists)):
        if tourists[t].turns == 3:
            tourists[t].bored = True
     #if bear gets a kiill it goes to bed            
    for b in range(len(bears)):
        if bears[b].kill == True:
            bears[b].sleep = True
            bears[b].turns = 3
            bears[b].kill = False
    # if the tourist sees moe than 3 bears it gets scared and bails
    for t in range(len(tourists)):
        if tourists[t].sees(bears) >= 3:
            tourists[t].scared = True
     #counter for seeing how many tourists get removed for list to avoid errors
    counter = 0
    for t in range(len(tourists)):
        if tourists[t-counter].die == True or tourists[t-counter].scared == True or tourists[t-counter].bored == True:
            print("{} - Left the Field".format(tourists[t-counter]))
            tourists.remove(tourists[t-counter])
            counter += 1
    
    #counter for seeing how many bears get removed for list to avoid errors
    counter = 0 
    for b in range(len(bears)):
        if bears[b-counter].left == True:
            print("{} - Left the Field".format(bears[b-counter]))
            bears.remove(bears[b-counter])
            counter +=1
    
     
    
    #prints update
    print("Field has {} berries.".format(berryfield.totalb()))
    print(berryfield)
    print("Active Bears:")
    for bear in range(len(bears)): 
        if bears[bear].sleep == True and bears[bear].turns -1 >0:
            print("{} - Asleep for {} more turns".format(bears[bear],(bears[bear].turns-1)))
        else:
            print(bears[bear])
    print("\nActive Tourists:")
    for tourist in range(len(tourists)):
        print(tourists[tourist])       
    turn += 1
    if turn == 6:
        break
print()