import time
date=time.strftime("%x")
print(date)
m=time.strftime("%b")
print(m)
t=time.strftime("%X")
print(t)

h=time.strftime("%H")
if(int(h)>=0 and int(h)<12):
        print("Good Morning")
elif(int(h)>=12 and int(h)<17):
        print("Good Afternoon")
elif(int(h)>=17 and int(h)<=21):
     print("Good Evening")
elif(int(h)>21 and int(h)<=23):
     print("Good Night")
else:
      print("invalid!")
         
d_t=time.strftime("%c")
print(d_t)
