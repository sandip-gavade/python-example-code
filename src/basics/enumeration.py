
countries =['India','UK','Belgium','USA','UAE']

for item in enumerate(countries,start=1):
    print(item)

for index,country in enumerate(countries,start=1):
    print(f'{index}. {country}')