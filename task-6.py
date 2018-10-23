str = "kkkjsflslsljsfjsjvjjjjjslabcdaefghijklsjkdflselewewwwwwejfslldcfiJJSJjJjjJjjsjsjjs"

#Method that loops through the given string and checks if the current letter
#is in the currentSubString.
def findLongestSubString(string):
    longest = []
    currentSubString = []
    for i, temp in enumerate(string): 
        currentSubString = []
        newString = string[i:]
        for letter in newString:
            if letter in currentSubString:
                if len(currentSubString) > len(longest):
                    longest = currentSubString
                currentSubString = []
            else:
                currentSubString.append(letter)
    if len(longest) > 3:
        print "Longest substring is:", len(longest)
    else:
        print "No substring is longer than 3 chars"

findLongestSubString(str)
