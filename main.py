months = {
    'january': '1',
    'february': '2',
    'march': '3',
    'april': '4',
    'may': '5',
    'june': '6',
    'july': '7',
    'august': '8',
    'september': '9',
    'october': '10',
    'november': '11',
    'december': '12'
}

days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29' '30', '31']

input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')

# Extracts dates from input_file and outputs formatted date into new parsedDates.txt file
print('opening inputDates.txt file...')
print('parsing...')
print('outputting formatted date in parsedDates.txt file...')
print('\n' + 'OUTPUT:')

for entry in input_file:
    if entry != '-1': # as long as inputs are not -1
        line = entry.split() # they will be split by a space separator and will be analyzed in the for-loop
        if len(line) >= 3: # if length of line is >= 3 then...
            month = line[0] # assign month to index 0 of line
            day = line[1] # assign day to index 1 of line
            year = line[2] # assign year to index 2 of line
            month = month.lower() # lower-cases var. month

            if month in months: # checks if month is in month_list
                day_with_comma=day[-1] # variable day_with_comma assigned to last element of day
                if day_with_comma == ',': # checks if there is a ','' in var. day
                    day = day[:len(day)-1] # inspects length of day and deletes the last element (deletes ',')
                    month_number = months[month] # assigns value of w/e month is to month_number using month_list
                    output = month_number + '/' + day + '/' + year
                    print(output)

                    output_file.write(output + '\n')


output_file.close()
input_file.close()

# ---------------------------------------------------------------
# Converts user input of whatever date, parses it, and outputs formatted version.
print()
print('-' * 45)
print('TRY IT YOURSELF!')
print('Please use the following format: September 1, 2020')

user_date = input('What is the date: ')

for user_entry in user_date:
    if user_entry != '-1':
        tokens = user_date.split()
        if len(tokens) >= 3:
            month = tokens[0]
            day = tokens [1]
            year = tokens [2]
            month = month.lower()

            if month in months and day[:len(day)-1] in days:
                day_with_comma = day[-1]
                if day_with_comma == ',':
                    day = day[:len(day)-1]
                    month_number = months[month]
                    print('The date is:', month_number + '/' + day + '/' + year)
                    break
            else:
                print('ERROR: Please follow the format shown above.')
                break
        else:
            print('ERROR: Please follow the format shown above.')
            break


