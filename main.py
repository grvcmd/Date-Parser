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

input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')

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


