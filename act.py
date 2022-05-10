# %%
arr = []
flag=True
for l in open ("insurance.csv","rt"):
    if flag:
        flag=False
        continue
    arr.append(int(l.split(",")[0]))

sum(arr)/len(arr)

# %%
len (arr)

# %%
arr.sort()
arr
if len(arr)%2==0:#Even
    i=len(arr)//2
    print((arr[i-1]+arr[i])/2)
else:
    print(arr[i])



# %%
