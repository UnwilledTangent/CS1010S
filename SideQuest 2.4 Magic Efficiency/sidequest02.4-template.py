#
# CS1010S --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: O(4^n)

# n * 3^n
# Ans: O(3^n)

# 1000000000n^2
# Ans: O(n^2)

# 2^n/1000000000
# Ans: O(2^n)

# n^n + n^2 + 1
# Ans: O(n^n)

# 4^n + 2^n
# Ans: O(4^n)

# 1^n
# Ans: O(1)

# n^2
# Ans: O(n^2)

# Faster order of growth in each group:

# i. O(4^n)
# ii. O(2^n)
# iii. O(n^n)
# iv. O(n^2)


##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########

# Time complexity of bar:O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n)

def improved_foo(params):
    if n == 0:
        return 0
    return n*(n+1)//2 + improved_foo(n-1)

# Improved time complexity: O(n)
# Improved space complexity: O(1)
