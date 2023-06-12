nums = [2,11,15,7]
target = 9


for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):

                sum = nums[i] + nums[j]
                print(sum)
                if sum == target:
                    print()