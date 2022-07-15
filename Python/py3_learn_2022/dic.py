capitals ={'USA': 'DC',
           'India': 'Dehli',
           'China': 'Beijing',
           'Russia':'Moscow'

        }
capitals.update({'Germany':'Berlin'})


#print (capitals['Russia'])
#print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key,value)
