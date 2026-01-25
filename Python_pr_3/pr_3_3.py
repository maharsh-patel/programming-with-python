#Create a program that will print out words that start with 's' from the below given statement.

string = "sammys sells seashells by the seashore"

print(string.split())

for word in string.split():
    if word.startswith('s'):
        print(word)


