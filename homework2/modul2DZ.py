calls = 0


def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_


print(string_info('Capybara'))
print(string_info('Armageddon'))



def is_contains(string_, list_,):
    count_calls()

    string_ = string_.lower()
    list_ = [item.lower() for item in list_]
    return string_ in list_


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
