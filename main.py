# max_num() to find the maximum of three numbers
def max_num(a, b, c):
    return max(a, b, c)

#test
print(max_num(1, 2, 3))

#multiply all numbers in a list
def mult_list(list):
    result = 1
    for num in list:
        result *= num
    return result

#test
print(mult_list([1, 2, 3, 4]))

#reverse string
def rev_string(s):
    return s[::-1]

#test
print(rev_string("hello"))

#given range
def num_within(n, start, end):
    return start <= n <= end

#test
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

#pascal's triangle
def pascal(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow = [left+right for left,right in zip(trow+y, y+trow)]
    return n>=1

#test
pascal(5)




