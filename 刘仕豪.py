n,p=map(int,input().split())
m=(n%10+int(n/10)%10*10)
hour=int(n/100)
sum=hour*60+m+p
hour=int(sum/60)
m=sum-hour*60
print("%d%02d"%(hour,m))