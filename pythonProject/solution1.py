def fruits(tuple_of_fruits):
    list_of_fruits = {}
    for fruit in tuple_of_fruits:
        if fruit['shape'] == "sphere" and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
            if fruit['name'] in list_of_fruits:
                list_of_fruits[fruit['name']] += 1
            else:
                list_of_fruits[fruit['name']] = 1
    return list_of_fruits
