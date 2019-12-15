

# 숫자 오름차순
a=[1,2,3]
temp=0
print(a)

def number(a):
    temp=0
    max=a[0]
    ind=0
    for i in a:
        if max< a[ind] :
        temp=a[ind]
        a[ind]=a[ind+1]
        a[ind+1]=temp

        index=ind+1

print(a)

#문자 오름차순
