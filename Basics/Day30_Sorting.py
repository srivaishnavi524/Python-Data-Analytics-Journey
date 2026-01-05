#bubble sort
#selection sort
#----------------------------------------------
# Bubble sort: 
# drawbacks -> multiple swapings(consume cpu power)
# def sort(nums):
#     for i in range(len(nums)-1, 0, -1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp

# nums = [ 5, 3, 6, 8, 2, 7]
# sort(nums)
# print(nums)
#-----------------------------------------------
#selection sort:

# def sort(nums):
#     for i in range(5):
#         min_pos = i
#         for j in range(i, 6):
#             if nums[j] < nums[min_pos]:
#                 min_pos = j
#         temp = nums[i]
#         nums[i] = nums[min_pos]
#         nums[min_pos] = temp

#         print(nums)

# nums = [ 5, 3, 6, 8, 2, 7]
# sort(nums)
# print(nums)
#------------------------------------------------------
