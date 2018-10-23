str = "Hello, My name is Jonas"

def reverseString(word):
    #Lets try this without using the easy methods like
    #word[::-1]
    #"".join(reversed(word))

    reversed = []
    i = len(word)
    while i:
        i -= 1
        reversed.append(word[i])
    return "".join(reversed)

print reverseString(str)
