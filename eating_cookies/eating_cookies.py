'''
Input: an integer
Returns: an integer
'''

#Understand: Given a number of cookies in a cookie jar - how many possible combinations can the cookie monster eat those cookies - he can eat 1, 2, or 3 at a time. 

def eating_cookies(n, cache={}):
    if n < 0:
        return 0 
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
