
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

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
targ = int(input("Enter a number from 1 to 10 for the engine to guess: "))

binary_search_engine(nums, targ)