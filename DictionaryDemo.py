# friends=({ 'tom' : '111-222-333',
#          'jerry' : '666-33-111'})
# print(friends) # {'tom': '111-222-333', 'jerry': '666-33-111'}

#Retrieving elements from
# print(friends['tom']) #111-222-333
#
# #Adding elements into dictionary
# friends['bob']='888-999-666'
# print(friends)
#
# #Modify elements into the dictionary
# friends['bob']='888-999-665'
# print(friends)
#
# #Delete element from the dictionary
# del friends['bob']
# print(friends)

#Looping items in the dictionary
# values ={'a' : '100',
#          'b' : '200',
#          'c' : '300',
#          'd' : '400'
#         }
# for k in values:
#     print(k, ":", values[k])
# print(values)
# print(len(values))

#Note ==   != tests equality
# We cant use relational operators like <,>,>=, <= to compare dictionaries

#Order of elements are not important
# d1= { "mike" :41, "bob" : 35}
# d2= {"bob": 35, "mike" : 41}
# print(d1==d2)
# print(d1!=d2)

#Dictionary methods

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
#popitem() Returns randomly select item from dictionary and also remove
print(friends.popitem()) #('jerry', '666-33-111')
print(friends) # {'tom': '111-222-333', 'bob': '888-999-666'}

#clear() Delete everything from dictionary
print(friends.clear()) #None
friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

#keys() Return keys in dictionary as tuples
print(friends.keys()) # dict_keys(['tom', 'bob', 'jerry'])

#values Return values in dictionary as tuples
print(friends.values()) # dict_values(['111-222-333', '888-999-666', '666-33-111'])

#get(key) Return value of key, if key is not found it returns None, instead on throwing KeyError exception
print(friends.get('jerry')) # 666-33-111
print(friends.get('bob')) #888-999-666

#pop(key) Remove the item from the dictionary, if key is not found KeyError will be thrown

print(friends) #{'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
print(friends.pop('tom')) #111-222-333
print(friends) #{'bob': '888-999-666', 'jerry': '666-33-111'}
