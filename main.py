def odd(n):
    even_num = n*3 + 1
    return even_num

def even(n):
    half_num = n // 2
    return half_num


def longest_collatz(num):
    count = 1
    storage = 0
    if num % 2 == 0:
        storage = even(num)
        while storage != 1:
            storage = even(storage)
            count += 1
    elif num % 2 != 0:
        storage = odd(num)
        while storage != 1:
            storage = even(storage)
            count += 1
    return count

def result_list(input_array):
        memory = input_array.copy()
        list = []
        #storage = input_array
        #while len(input_array) > 0:
        for val in input_array:
            list.append(longest_collatz(val))
            input_array.pop(0)
                #storage = input_array
                # while len(storage) > 0:
                #     for v in storage:
                #         list.append(longest_collatz(v))
                #         storage.pop(0)
                #return list

        index = range(len(list))
        max_num = list[0]
        max_num_index = 0
        for num in index:
            if list[num] > max_num:
                max_num = list[num]
                max_num_index = num
            elif list[num] < max_num:
                max_num = max_num
        return memory[max_num_index]

print(result_list([27, 4, 5, 27, 4, 5]))

