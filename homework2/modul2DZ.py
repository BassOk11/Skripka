calls = 0
def count_calls():
    global calls
    calls += 1
    def string_info(string):
        global calls
        calls += 1
        print((len(string), string.upper(), string.lower()))
    string = input('Строчка с вас: ')

    string_info(string)


    def is_contains():
        global calls
        calls += 1
        list_ = []
        string = input("Is contains: ")
        list_.append(input("Is_contains: "))
        for i in range(len(list_)):
            for j in range(len(string)):
                print(i == j)

        print(calls)


    is_contains()

count_calls()
