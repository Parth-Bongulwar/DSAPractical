n=3
weight=[10,20,30]
profit=[15,20,24]
capacity=30
ratio=[]
for i in range(n):
    ratio.append(profit[i]/weight[i])

for i in range(n):
    for j in range(i+1,n):
        if ratio[i]<ratio[j]:
            ratio[i],ratio[j]=ratio[j],ratio[i]
            profit[i],profit[j]=profit[j],profit[i]
            weight[i],weight[j]=weight[j],weight[i]

total=0
for i in range(n):
    if weight[i]<=capacity:
       total+=profit[i]
       capacity-=weight[i]
    else:
       total+=(profit[i]/weight[i])*capacity
       break
print("Maxm profit=",total)  
