children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
# {
# 'key': {'key': value, 'key': value},
# 'key': {'key': value, 'key': value},
# }
# print(children)
# you can add value directly
children['Emily'] = {'profession': 'artist', 'age': 5}
# you can add  value from dictionary
children['Adam'] = {'profession': (children['Adam']), 'age': 9}
children['Nancy'] = {'profession': (children['Nancy']), 'age': 14}
# print(children)
# print(type(children['Emily']['age']))
