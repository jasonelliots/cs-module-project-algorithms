'''
Input: a List of integers
Returns: a List of integers
'''

#Understand: move all the 0s in an array to the end of the array 
#Plan: see psuedo code 
def moving_zeroes(arr):
    #loop through each item in the array 
    # if item == 0, delete the item from the array and add 0 to the end 
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")