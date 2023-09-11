#input_array = [1, 5, 27, 4]
def half(n):
    half_num = n // 2
    return half_num


def longest_collatz(input_array):
    count = 0
    storage = 0
    for num in input_array:
        while storage != 1:
            if num % 2 == 0:
                storage = half(num)
                count += 1
                storage = half(storage)
                count += 1
            elif num % 2 != 0:
                result = num*3 + 1
                storage = half(result)
                count += 1
        return count

print(longest_collatz([8]))

