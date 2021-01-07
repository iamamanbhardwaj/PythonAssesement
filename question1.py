def GetSeatGrouping(inputString, allowedcharacters= 'GSHR'):
    #

    #Parameters:
    #   inputString (str):The string or row which is to be interpreted.
    #   list(str1): Fan codes allowed in input string.   

    #Returns:
    #   list:Returns an array of tuples containing team code and count.
    allowedchars = set(allowedcharacters)
    output = []
    if(len(inputString) == 0 or not set(inputString).issubset(allowedchars)):
        print('Input string has invalid seating characters')

    inputString = inputString+'X'
    count = 0
    charBeingTracked = inputString[0]

    for char in inputString:
        
        if( not (char == charBeingTracked) or charBeingTracked == 'X'):
            output.append((charBeingTracked,count))
            charBeingTracked = char
            count = 0
        count += 1

    return output
    
##Input: seating patterns in group of GSHR

print('Audience seated as: ')
inputString = input()

print(GetSeatGrouping(inputString))


