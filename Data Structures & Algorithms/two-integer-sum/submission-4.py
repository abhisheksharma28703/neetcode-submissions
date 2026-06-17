class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         if(nums[i]+nums[j]==target):
        #             temp.append(i)
        #             temp.append(j)
        #             return temp
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[0])

        back = 0
        forw = len(nums)-1

        while back<forw:
            curr_sum = indexed_nums[back][0] + indexed_nums[forw][0]

            if(curr_sum==target):
                return sorted([indexed_nums[back][1], indexed_nums[forw][1]])
            elif curr_sum<target :
                back += 1
            else:
                forw -= 1
        return []
