from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            j = x + 1
            for y in range(len(nums)):
                if j == len(nums): break

                sum = nums[x] + nums[j]
                print(nums[x], nums[j])

                if sum == target:
                    return [x, j]
                
                j = j + 1



solut = Solution()

print(solut.twoSum([2,7,11,15], 9))
print(solut.twoSum([3,2,4], 6))
print(solut.twoSum([3,3], 6))
