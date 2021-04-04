def operations(a,b):
    if type(a)==str or type(b)==str:
        return "ERROR only integers"
    SUM=a+b
    DIFFERENCE=a-b
    PRODUCT=a*b
    if b!=0:
        QUOTIENT=a/b
        REMAINDER=a%b
    else:
        QUOTIENT="ERROR"
        REMAINDER="ERROR"
    return SUM, DIFFERENCE, PRODUCT, QUOTIENT, REMAINDER
