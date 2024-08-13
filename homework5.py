immutable_var = ('данные',True, 1,2,3,4,)
print(immutable_var)
#immutable_var.append(False)
"""immutable_var [2] = 56   #кортеж не изменяемый набор данных
   immutable_var [2] = 56
    ~~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment"""
mutable_list = ['данные',True, 1,2,3,4,]
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list[5] = 'новые данные'
print(mutable_list)
mutable_list.extend('12345')
print(mutable_list)
