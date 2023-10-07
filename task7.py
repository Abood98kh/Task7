# Question 1:
my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get('name'))
my_dict['age'] = 32
my_dict.update({'Workplace': 'GSG'})
print(my_dict)

# Question 2:
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
#***************************************************************
# This is a normal conversion from tuple to dict
# new_dict = dict(my_tuple)
# print(new_dict)
#***************************************************************
# This is to get the output shown in the task
new_dict = {}
for tuple in my_tuple:
    (values , keys) = tuple
    new_dict.update({keys: values})
print(new_dict)

# Question 3:
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
sum_dict = dic1
sum_dict.update(dic2)
sum_dict.update(dic3)
print(sum_dict)
#***************************************************************
# or from Google:
# dic4 = {**dic1, **dic2, **dic3}
# print(dic4)
#***************************************************************

# Question 4:
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
print(f'Maximum value: {max(my_dict.values())}')
print(f'Minimum value: {min((my_dict.values()))}')

# Question 5:
my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
if my_dict.get('ID') is None:
    print(False)

# Question 6:
Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'], 'Market Share %': [27.99, 15.9, 9.36, 6.67]}
new_list = []
for item, per in zip(Languages2023['Programming Language'][:], Languages2023['Market Share %'][:]):
    dict_lst = {}
    new_list = new_list + [dict_lst]
    dict_lst.update({'Programming Language': item, 'Market Share %': per})
    print(dict_lst)
print(new_list)
