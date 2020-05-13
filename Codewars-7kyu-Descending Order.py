# Task: make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Example: Input: 145263 Output: 654321, Input: 123456789 Output: 987654321

# Solution (I know this solution is very bad but I cant solve that in other way):
def descending_order(num): 
  
    count = [0 for x in range(10)]
    
    string = str(num)
  
    for i in range(len(string)): 
        count[int(string[i])] = count[int(string[i])] +  1
  
    result = 0
    multiplier = 1
  
    for i in range(10): 
        while count[i] > 0: 
            result = result + ( i * multiplier ) 
            count[i] = count[i] - 1
            multiplier = multiplier * 10

    return result

num = 123456789
descending_order(num)
