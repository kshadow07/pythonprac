# Here's a Medium level question on LeetCode:

# 3Sum

# Given an array nums of n integers, are there elements a, b, and c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.
# The triplets should be in the order of [a, b, c] where a ≤ b ≤ c.
# Example 1:

# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]


list=[]
triplet={}
newlist=[]
for i in range(6):
    list.append(int(input("Enter no: ")))

for i in range(len(list)):
    for j in range(1,len(list)):
        for k in range(2,len(list)):
            if list[i]+list[j]+list[k]==0:
                 triplet = tuple(sorted([list[i], list[j], list[k]]))
                 if triplet not in newlist:
                    newlist.append(triplet)
                

print(newlist)         