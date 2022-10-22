numbers_list_1 = [2, 6, 9, 8, 8, 15, 1, 5, 88]
numbers_list_2 = [2, 56,7,8,4,99,10]
odd_list = []
even_list = []

def odd_or_even(number_list):
    odd_list = []
    even_list = []
    for i in number_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return f'This is Odd List : {odd_list}\nAnd This is Even List : {even_list}'
odd_and_even_list = odd_or_even(numbers_list_1)
print(odd_and_even_list)


