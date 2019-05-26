""" Python Functions """

def intersection(list1, list2):
    common_items = []
    for val in list1:
        if val in list2:
            common_items.append(val)
    return common_items

print( intersection([1, 2, 3], [2, 3, 4]) )
print( intersection(["harman", "singh", "manchanda"], ["harry", "manchanda"]) )
