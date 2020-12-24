#利用两个指针i, j,初始化值为0和1，当两个指针对应的值相等时，指针j+1，继续执行循环；而当两个指针对应的值不相等时，将指针i+1，并将指针j对用的值赋值给指针i，然后指针j+1，继续向下执行循环，直到循环结束


class Solution:
    def removeDuplicates(self, nums): 
        i = 0
        j = 1
        if len(nums)==2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        
        while j<len(nums):

            if nums[i] != nums[j] and nums[j] !=None :
 
                i = i+1
                nums[i] = nums[j]
                if i!=j:#这里比较关键，没有这个在[1,2,2]的情况中就会出现错误
                    nums[j] = None
                
            else:
                j = j+1

        return i+1
