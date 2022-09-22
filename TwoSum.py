my_numbers = [3, 5, -4, 8, 11, 1, -1, 6]

target = 10


def two_number_sum(list_of_numbers, target):
    result = []

    for number in list_of_numbers:
        for index in range(len(list_of_numbers)):
            if number == list_of_numbers[index]:
                continue
            #         print(f'{number}+{list_of_numbers[index]} = {number+list_of_numbers[index]}')
            sum_numbers = number + list_of_numbers[index]
            if sum_numbers == target and number not in result:
                result.append(number)
                result.append(list_of_numbers[index])
    return result


print(two_number_sum(my_numbers, target))