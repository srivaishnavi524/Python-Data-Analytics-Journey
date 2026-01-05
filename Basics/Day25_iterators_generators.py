# nums =[7, 5, 9, 5]
# it = iter(nums) # iter convers the nums in list into iterator
# print(it.__next__()) # 7
# print(next(it)) # 5
# for i in nums:
#     print(i)
#------------------------------------
# class TopTen:
#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
        
# values = TopTen()
# for i in values:
#     print(i)
#---------------------------------------------------
# GENERATORS:
# yield is same as return but return we can write only once , but yield we can write n number of times.
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq # yield give next next values
        n += 1
values = topten()

for i in values:
    print(i)
    
  
# print(values) # gives the o/p of the object value  for topten 


