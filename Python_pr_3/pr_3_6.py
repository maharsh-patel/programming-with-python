"""Go to String below and if the length of a word is even print "even!"""


str = input("Enter a string: ")

words = str.split()

for word in words:
    if len(word) % 2 == 0:
        print( word, "is even")
else:
        print(word , "are odd")