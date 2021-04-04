import string
def filter(phrase,n):
    L=[]
    phrase=phrase.split()
    for i in range (len(phrase)):
        if phrase[i]  not in string.punctuation and len(phrase[i])>n:
            L.append(phrase[i])
   
    return L
