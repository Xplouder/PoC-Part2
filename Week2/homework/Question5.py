counter = 0
iteration_counter_list = []


def memorized_fib(num, memo_dict):
    global counter, iteration_counter_list

    counter += 1
    iteration_counter_list.append((num, counter))

    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memorized_fib(num - 1, memo_dict)
        sum2 = memorized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2


memorized_fib(60, {0: 0, 1: 1})
for elem in iteration_counter_list:
    print elem