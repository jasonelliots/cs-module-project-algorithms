'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

#Understand: For a given array of numbers, there is a window of a certain size(k). That window starts at the beginning of the array and slides to the end of the array one index at a time. Find the max value contained within the window at each position. 
def sliding_window_max(nums, k):
    maxWindowVals = []
    # check first K items of array, increase starting index by 1, repeat until window reaches last item of array
    windowStart = 0 

    while windowStart <= len(nums) - k: 

        newWindow = nums[windowStart:windowStart+k]
        windowMax = max(newWindow)
        maxWindowVals.append(windowMax)
        windowStart += 1

    return maxWindowVals



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
