if __name__ == '__main__':
    selected_numbers = []
    final_selected_numbers = []
    doubles = ['11', '22', '33', '44', '55', '66', '77', '88', '99']
    for count in range(382345, 843168):
        number = list(map(int, list(str(count))))
        if (number[0] <= number[1] <= number[2] <= number[3] <= number[4] <=
                number[5]):
            selected_numbers.append(count)
    for selected_number in selected_numbers:
        if any(x in str(selected_number) for x in doubles):
            final_selected_numbers.append(selected_number)
    print(len(final_selected_numbers))




