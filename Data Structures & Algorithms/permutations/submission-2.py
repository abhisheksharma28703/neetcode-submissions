class Solution:
    def permute(self, nums):
        ans = []
        temp = []
        visited = [False] * len(nums)

        def backtrack():

            if len(temp) == len(nums):
                ans.append(temp[:])
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue

                visited[i] = True
                temp.append(nums[i])

                backtrack()

                temp.pop()
                visited[i] = False

        backtrack()
        return ans