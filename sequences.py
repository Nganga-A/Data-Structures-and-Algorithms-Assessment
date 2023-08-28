def remove_duplicates(sequence):
    list = []
    for num in sequence:
        if list.count(num) == 0:
            list.append(num)
    return list
    
sequence = [1,1,1,2,3,3,4,5,5,7,7,7,7,7]
print(remove_duplicates(sequence))