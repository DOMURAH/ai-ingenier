nums = [12,4,8,7,5,6,1,16,23,3]

for _ in range(len(nums),0,-1):
    nums.pop(-1)
    
print(nums)
    