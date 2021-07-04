alphabets=[chr(i) for i in range(96,103)]
My_dict={"person_1":{'name':'Abdul rafay','age':22,'interests':['football','cricket'],'amount deposited':[24000,26000] },
                     "person_2":{'name':'Nancy James','age':23,'interests':['baseball','cricket'],'amount deposited':[24000,27000] },
                                 "person_3":{'name':'selena gomez','age':26,'interests':['baseball','table tennis'],'amount deposited':[24000,26000]}}
map_function=list(map(lambda x:'Mr. ' + x if alphabets(96,102) else 'Ms.'+x,My_dict))
filter=list(filter(lambda x: x=[] if x!=alphabets,My_dict))
print(map_function)
