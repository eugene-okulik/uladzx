my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['list_1', 'list_2', 'list_3', 'list_4', 'list_5'],
    'dict': {'dict_1': 'value_1', 'dict_2': 'value_2', 'dict_3': 'value_3', 'dict_4': 'value_4', 'dict_5': 'value_5'},
    'set': {'set_1', 'set_2', 'set_3', 'set_4', 'set_5'}
}

#tuple

print((my_dict['tuple'])[-1])

#list

add_new_element_in_list = my_dict['list'].append('list_6')
remove_second_element_from_list = my_dict['list'].pop(1)

#dict

add_new_element_in_dict = (my_dict['dict'])['i am a tuple'] = (10, 9, 8, 7, 6, 5)
remove_any_element_from_dict = my_dict['dict'].pop('dict_1')

#set

add_new_element_in_set = my_dict['set'].add('set_new')
remove_any_element_from_set = my_dict['set'].remove('set_3')

#my_dict after all actions has the following view:

print(my_dict)
