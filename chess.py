# import  math
def rotate(x1,y1,x2,y2,n):
  if x1>x2:
    x1=n-x1-1
    x2=n-x2-1
  if y1>y2:
    y1=n-y1-1
    y2=n-y2-1
  return x1,y1,x2,y2

def is_on_board(x1,y1,n):
  return 0<=x1<n and 0<=y1<n 

def return_list_of_area_dst(x1,y1,n):
  ls=  [(x1,y1,0)]

  if is_on_board(x1-2,y1,n):
    ls.append((x1-2,y1,2))

  if is_on_board(x1+2,y1,n):
    ls.append((x1+2,y1,2))

  if is_on_board(x1-2,y1+1,n) or is_on_board(x1+1,y1-2,n):#alacson
    ls.append((x1-1,y1-1,2))

  return ls
def return_list_of_area_src(x1,y1,n):
  ls=  [(x1,y1,0)]

  if is_on_board(x1,y1+2,n):
    ls.append((x1,y1+2,2))

  if is_on_board(x1+2,y1+1,n):
    ls.append((x1+2,y1+1,1))

  if is_on_board(x1-1,y1+1,n) and (is_on_board(x1+1,y1+2,n) or is_on_board(x1-2,y1-1,n)):
    ls.append((x1-1,y1+1,2))

  return ls

def find_perfect_path(x1,y1,x2,y2,n):
  dis_x=x2-x1
  dis_y=y2-y1
  up=0
  right=0
  if dis_x-2*dis_y>=4:
    right=max(0,(dis_x-2*dis_y)//4)
    dis_x=dis_x-(right*4)
  if dis_y-2*dis_x>=4:
    up=max(0,(dis_y-2*dis_x)//4)
    dis_y=dis_y-(up*4)
  x=max(0,(2*dis_x-dis_y)//3)
  y=max(0,(2*dis_y-dis_x)//3)
  dis_x=dis_x-2*x-y
  dis_y=dis_y-2*y-x
  if dis_x==0 and dis_y==0:
    return x+y+2*up+2*right
  return None

def find_minimum_path(x1,y1,x2,y2,n):
  ls=[]
  x1,y1,x2,y2=rotate(x1,y1,x2,y2,n)
  l1=return_list_of_area_src(x1, y1,n)
  l2=return_list_of_area_dst(x2, y2,n)

  if abs(x2-x1)>2 or abs(y2-y1)>2 or (x1==y1==0 and x2==y2==1):
    if is_on_board(x2-1,y2-3,n):
      l2.append((x2,y2-1,1))
  
    if is_on_board(x1+3,y1+1,n):
      l1.append((x1+1,y1,1))


  for point_0 in l1:
    for point_1 in l2:
      if point_0[0]==point_1[0] and point_0[1]==point_1[1]:
        ls.append(point_0[2]+point_1[2])
      else:
        _x1,_y1,_x2,_y2=rotate(point_0[0],point_0[1],point_1[0],point_1[1],n)
        steps = find_perfect_path(_x1,_y1,_x2,_y2,n)
        if steps:
          steps+=point_0[2]+point_1[2]
          ls.append(steps)

  return min(ls)
# print(find_minimum_path(3,3,4,4,10))