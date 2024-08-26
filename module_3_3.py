def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [False, 25, [1, 2, 3]]
values_dict = {'a': 1, 'b': 2, 'c': 3}
values_list_2 = [54.32, 'Строка']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
