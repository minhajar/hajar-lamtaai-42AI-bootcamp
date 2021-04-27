import time

def ft_progress(listy):
    L=list(listy)
    position=">"
    for i in listy:
        print("\r","ETA :",round(0.01*len(L),2),"s [{}%]".format(i//10),"[",position,' '*(20-len(position)),"{}/1000 ".format(i+1),"| elapsed time {} s".format(round(i*0.01,2),end='')
        if i%50==0:
            position= "="+position
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
    
