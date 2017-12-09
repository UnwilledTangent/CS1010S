#
# CS1010S --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <A0171149E> <Samantha Ang Ee Ning>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x,x)

# (a) What are the types of the input and output of the generic square operation?(1 mark)
# Answer:

# (b) Why would we prefer to define square in the above way, rather than: (2 marks)
# def square(x):
#    return apply_generic("square",x)
# Answer:



##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by
# the name of the operator and a tuple of strings. For example, the add operator is indexed
# by ’add ord’ and (’ordinary’, ’ordinary’); negation is indexed by ’negate ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by ’make ord’ and just a string ’ordinary’.
# Explain why we have such a difference.
# Hint: Consider the differences in the process of the creation of a Generic-Num, such as create ordinary,
# and the operations we can apply on Generic-Num, such as add. How is make ord invoked, and how is add ord invoked?

# Answer:


##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

# first_try = create_rational(9, 10)
# second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way:
# What happens:
# Why it happens:

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 =
# r3_1 =
# csq = square(sub(r2_7, r3_1))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |       |       |  -->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |       |       |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer:

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x,y))
    def reprat(x,y):
        return (x,y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)
 
    def add_rat(x,y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x,y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x,y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x,y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )
    
    def negate_rat(x):
        # input is a rational number and output is also a rational number
        return make_rat(negate(numer(x)), denom(x))
    
    def is_zero_rat(x):
        # input is a rational number and output is a boolean
        return is_zero(numer(x))
    
    def is_eq_rat(x,y):
        # inputs are two rational numbers and output is a boolean
        return is_zero(sub_rat(x,y))
                         
    put("make","rational", make_rat)
    put("add",("rational","rational"), add_rat)
    put("sub",("rational","rational"), sub_rat)
    put("mul",("rational","rational"), mul_rat)
    put("div",("rational","rational"), div_rat)
    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)



install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

######################################################
# Change the value for variable: r1_2, r2_4 and r1_8 #
######################################################
r1_2 = None
r2_4 = None
r1_8 = None

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
# gradeThis()
