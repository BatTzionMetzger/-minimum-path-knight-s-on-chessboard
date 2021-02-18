from  chess import *
from bfs import *
import pickle
def test():
    i=0
    n=50
    j=0
    with open('50.pkl', 'rb') as f:
       ls_50 = pickle.load(f)
    # ls_50=[]
    for x1 in range(0,(n//4)+1):
        print("x1",x1)
        for y1 in range(0,(n//4)+1):
             for x2 in range(0,n):
                for y2 in range(0,n):
                    if find_minimum_path(x1,y1,x2,y2,n+1) !=ls_50[j] :
                        print(i,(x1,y1,x2,y2),find_minimum_path(x1,y1,x2,y2,n+1) , ls_50[j])
                        i+=1
                    j+=1
    print("i",i,"n",n)     
test()