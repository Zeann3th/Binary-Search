
def binary_search_engine(numbers, target):
        midpoint = (len(numbers))//2

        if numbers[midpoint] == target:
            print("The answer is: " + str(target))
            return 0
        else:
            if numbers[midpoint] < target:
                return binary_search_engine(numbers[midpoint+1:], target)
            elif numbers[midpoint] > target:
                return binary_search_engine(numbers[:midpoint], target)

nums = range(101)
targ = int(input("Enter a number from 1 to 10 for the engine to guess: "))

binary_search_engine(nums, targ)
