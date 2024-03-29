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
            if storage % 2 == 0:
                storage = even(storage)
                count += 1
            elif storage % 2 != 0:
                storage = odd(storage)
                count += 1

    elif num % 2 != 0:
        storage = odd(num)
        while storage != 1:
            if storage % 2 == 0:
                storage = even(storage)
                count += 1
            elif storage % 2 != 0:
                storage = odd(storage)
                count += 1
    return count

def result_list(input_array):
        memory = input_array.copy()
        list = []

        for val in input_array:
            list.append(longest_collatz(val))

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

print(result_list([75, 226, 113, 340]))

