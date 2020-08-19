'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# Understand: Need to find the one int that does not show up twice 
# Plan: See psuedo code 
# Execute:
# Reflect: 
def single_number(arr):
    
    #loop through array
    #for each item in array, count the number of occurencs
    #if count == 1, return that item 

    # for i in arr:
    #     count = arr.count(i)
    #     if count == 1:
    #         return i 
    
    for i in arr:
        if arr.count(i) == 1:
            return i

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")