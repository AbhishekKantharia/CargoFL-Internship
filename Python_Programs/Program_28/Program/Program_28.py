from math import factorial


def printPermutationsLexico(string):
    # In lexicographic sequence, print all permutations of string s.
    stringseq = list(string)

    # There will be n! permutations where n = len (seq).
    for t in range(factorial(len(stringseq))):
        # print permutation by joining all the characters using join() function
        print(''.join(stringseq))

        # Find p such that seq[per:] is the longest sequence with lexicographic
        # elements in decreasing order.
        per = len(stringseq) - 1
        while per > 0 and stringseq[per - 1] > stringseq[per]:
            per -= 1

        # reverse the stringsequence from per to end using reversed function
        stringseq[per:] = reversed(stringseq[per:])

        if per > 0:
            # Find q such that seq[q] is the smallest element in seq[per:] and seq[q] is greater
            # than seq[p - 1].Find q such that seq[q] is the smallest
            # element in seq[per:] and seq[q] is greater than seq[per - 1].
            q = per
            while stringseq[per - 1] > stringseq[q]:
                q += 1

            # swapping seq[per - 1] and seq[q]
            stringseq[per - 1], stringseq[q] = stringseq[q], stringseq[per - 1]


# Enter some random string as user input using int(input()) function.
given_string =input('Enter some random string = ')
# printing  all the perumutations
print('printing all [', given_string, '] permutations :')
# passing given string to printPermutationsLexico function
printPermutationsLexico(given_string)