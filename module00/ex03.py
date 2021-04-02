import string
def text_analyzer(text):
    p=len(text)
    U=0
    L=0
    P=0
    S=0
    for i in range(p):
        if text[i]==' ':
            S+=1
        if text[i].isupper()==True:
            U+=1
        if text[i].islower()==True:
            L+=1
        if text[i] in string.punctuation:
            P+=1
    return "This text contains :", p ,"caracters:", U,"upper letters",L,"lower letters",S ,"spaces", P ,"Punctuation marks" 

