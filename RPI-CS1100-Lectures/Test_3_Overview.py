# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 01:36:31 2019

@author: matth
"""
''' Test 3 Overview '''
#Question 1
print("Question 1: ")
s1 = {0,1,2,3,4,5,6,7,8,9,17,23,24,34,100,101}
s2 = {0,2,4,6,8,10,12,14,16}
s3 = {1,3,5,7,9,11,13,15,17}
print(s1.difference(s2).difference(s3))
#Question 2
print("Question 2: ")
w1 = "the quick brown fox jumps over the lazy dog"
w2 = "hey diddle diddle the cat and the fiddle the cow jumps over the moon"
w3 = "jack and jill went over the hill to fetch a pail of water"
print(len(set(w1.split(" ")).intersection(set(w2.split(" "))).intersection(set(w3.split(" ")))))
print()

#Question 3
''' Output:
{7,12}
{7,9,12,'abc','b','car',10}
True
False
True
{14,'ab'} --------> I fucked up as I forgot to reference the new s2 set which discarded the 12. This would mean
that (s1 &  s2) = {7}, so ((s1 &  s2) ^ s3) = {'ab',7,12,14} as nothing matches in either set
'''
print("Question 3: ")
s1 = set( [7,9, 12, 7, 9] )
s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
s3 = set( [12, 14, 12, 'ab'] )
print(s1 & s2)
print(s1 | s2)
print('b' in s2)
print('ab' in s2)
print('ab' in s3)
s2.discard(12)
print((s1 & s2) ^ s3)
print()

#Question 4a
#rest_reviews = {"DeFazio's":["Great pizza", "Best in upstate"], \
#"I Love NY Pizza":["Great delivery service"], \
#"Greasy Cheese": [ "Awful stuff", "Everything was terrible" ] }
#
#counter = 0
#for key in rest_reviews.keys():
#    for LIST in rest_reviews[key]:
#        for review in LIST:
#            words = review.split(" ")
#            for i in range(len(words)):
#                if words[i].lower() == "awful":
#                    counter += 1
#                    print(counter)
#        if counter > 0:
#            print("{} found awful {} times".format(rest_reviews[key], counter))

#Question 5a
''' Output:
kate 3
jane 1
'''
print("Question 5a: ")
x = {1:['joe',set(['skiing','reading'])],\
2:['jane',set(['hockey'])]}
x[1][1].add('singing')
x[1][0] = 'kate'
for item in sorted(x.keys()):
    print(x[item][0], len(x[item][1]))
print()  
    
#Question 5b
''' Output:
** alice
** bob
** jane
!! #jane #after leaving the first for loop m is equal to 10 and both jane and kirsten are equiivalent to m 
but jane will be ran through first as the list of keys is sorted
!! kristen
'''
print("Question 5b: ")
y = {'jane':10, 'alice':2, 'bob':8,\
'kristin':10}
m = 0

for person in sorted(y.keys()):
    if y[person] > m:
        print("**", person)
        m = y[person]
for person in sorted(y.keys()):
    if y[person] == m:
        print("!!", person)
print()
       
#Question 5c
''' Output:
'5'  '0'  '1'  '6'

'8'  'car'  'b'  'k'
'''
print("Question 5c: ")
L1 = [0,1,2]
L2 = ['a','b']
d = { 5:L1, 8:L2 }
L1[2] = 6
d[8].append('k')
L2[0] = 'car'
for k in sorted(d.keys()):
    print(str(k) + ' ', end='')
    for v in d[k]:
        print(str(v) + ' ', end='')
    print()
print()
    
#Question 5d
''' Output:
[5,1,2]
-----------> 0 #pop does not affect the set, no aliasing so 0 and 4 remain in the set
2 ---------> 2
5 ---------> 4 #changing the list does not affect the set
6 ---------> 6
'''
print("Question 5d: ")
L1 = [0,1,2,4,1, 0]
s1 = set(L1)
L1.pop()
L1.pop()
L1.pop()
L1[0] = 5
s1.add(6)
s1.discard(1)
print(L1)
print(s1)
for v in sorted(s1):
    print(v)
print()
    
#Question 6
print("Question 6: ")
class Person(object):
    def __init__( self, n, bd, m, f):
        self.name = n
        self.birthday = bd
        self.mother = m
        self.father = f

    def family(self,person):
        if self.name == person.name and self.birthday == person.birthday and \
        self.mother == person.mother and self.father == person.father:
            return -1
        elif self.birthday == person.birthday and self.mother == person.mother and self.father == person.father:
            return 2
        elif self.mother == person.mother and self.father == person.father:
            return 1
        else:
            return 0
print()
 
#Question 7
'''Output:
{'Joe':set(['555-1111','555-2222','555-4444']), 'Jane':set(['555-3333']), 'Kate':set(['555-6666'])}'''
print("Question 7: ")
print()
def merge_dict(D1,D2):
    D = {} #Is there a reason as to why this can't be set() and then add the values into the empty set?
    for key in D1.keys():
        if key in D2.keys():
            D[key] = D1[key].union(D2[key])
        else:
            D[key] = D1[key]
    for key in D2.keys():
        if key not in D1.keys():
            D[key] = D2[key]
    return D
D1 = {'Joe':set(['555-1111','555-2222']), 'Jane':set(['555-3333'])}
D2 = {'Joe':set(['555-2222','555-4444']), 'Kate':set(['555-6666'])}
print(merge_dict(D1,D2))
print()

#Question 8   
    
#Question 10
print("Question 10: ")
def k_smallest(L,k):
    new = list(L)
    new.sort()
    return new[0:k]
L = [ 15, 89, 3, 56, 83, 123, 51, 14, 15, 67, 15 ]
print(k_smallest(L,4))
print()

#Question 11a
''' Output:
2
mom
['gran', 'dad']
'''
print("Question 11a: ")
dt = { 1: [ 'mom', 'dad'], 'hi': [1, 3, 5 ]}
print(len(dt))
print(dt[1][0])
dt['hi'].append(3)
dt[1][0] = 'gran'
print(dt[1])
print()
    
#Question 11b   
''' Output:
4
2
5 -------> LC.append(12) does not change the value for 'co'. No Aliasing as 'co' is a copy due to slicing
5
4
''' 
print("Question 11b: ")
LP = [2, 3, 5, 7]
LC = [4, 6, 8, 9]
nums = dict()
nums['pr'] = LP
nums['co'] = LC[:]
LP[1] = 5
print(len(nums['co']))
v = LC.pop()
v = LC.pop()
v = LC.pop()
LC.append(12)
print(len(LC))
print(nums['co'])
print(len(nums['co']))
v = nums['pr'].pop()
v = nums['pr'].pop()
print(nums['pr'][1])
print(len(LP))
print()