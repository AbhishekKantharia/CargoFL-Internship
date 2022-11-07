from operator import itemgetter, attrgetter

l = []
while True:
    s = str(input("Enter a String Separated by Commas:- "))
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))