dict_days = {
    "Monday": "Thu hai",
    "Tuesday": "Thu ba",
    "Wednesday": "Thu tu",
}

loop = True
while loop:
    for word in dict_days.keys():
        print(word, end=' ')

    print()
    input_word = input("Code? ")
    if input_word in dict_days:
        mean = dict_days[input_word]
        print(mean)
    else:
        yes_or_no = input("Add word? (Y/N)").lower()
        if yes_or_no == 'y':
            mean_input = input("Meaning? ")
            dict_days[input_word] = mean_input
        else:
            loop = False

    