def reverse(word):
    p=len(word)
    A=' '
    for i in range (p):
        A=A+word[p-i-1]
    return A
