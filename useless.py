l = []
with open('./1.txt','r') as f:
#     for i in range(32):
#         a=f.readline().split()
#         l.append(a[0]+'_'+a[1]+'_'+a[5])
# with open('./2.txt','w') as f:
#     for i in l:
#         f.write(i+'\n')
    a = f.read().split('\n')
print(type(a))
print(a)