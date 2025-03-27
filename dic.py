# I want to sort students dict based on student names
#Sorting dictionary based on keys

simple ={'cv':34,'er': '45', 'q': 0,'a':3,'z':45,'g':'op'}
s=dict(sorted(simple.items() ))

#Sorting dictionary based on values
simple1 ={'cv':34,'er': 45, 'q': 3,'a':3,'b':45,'g':6}
s1=dict(sorted(simple1.items(), key= lambda x:( x[1], x[0] )))

#Sorting a nested list, 2D-listt
nested =[[9,-91,3,0,12,42,-94,64,2,11],[13,0,5,-13,45,62],[-15,-4,16,-2,95,0,-15],[19,-19,0]]
sorted_list=[sorted(small) for small in nested]      # Sorting inner lists
sorted_list.sort()    # Sorting outer list 

students = [
    {"name": "Glice", "age": 20, "grade": "A"},
    {"name": "Mob", "age": 22, "grade": "B"},
    {"name": "Aharlie", "age": 21, "grade": "A"},
    {"name": "Omar", "age": 10, "grade": "F"},
    {"name": "Xyb", "age": 29, "grade": "B"},
    {"name": "Rizwan", "age": 45, "grade": "D"}
]

sorted_students=sorted(students,key= lambda x : x['age'])


students1 = {
    "ZDlice": {
        "age": 22,
        "grades": {"math": 90, "science": 85, "english": 88},
        "address": {"city": "New York", "zip": "10001"},
    },
    "Xob": {
        "age": 21,
        "grades": {"math": 75, "science": 80, "english": 79},
        "address": {"city": "Los Angeles", "zip": "90001"},
    },
    "Tharlie": {
        "age": 23,
        "grades": {"math": 95, "science": 92, "english": 90},
        "address": {"city": "Chicago", "zip": "60601"},
    }
}
sorted_dict = dict(sorted(students1.items(),key= lambda x: x[1]['grades']['math']))

students2 = {
    "Alice": [90, 85, 88],
    "Bob": [75, 80, 79],
    "Charlie": [95, 92, 90],
    "David": [88, 76, 85]
}

last = dict(sorted(students2.items(), key= lambda x: x[0], reverse= True))
print(last)