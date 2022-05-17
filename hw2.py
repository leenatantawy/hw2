# Paragon National Group Spring 2022
# Computer Science / Data Science Track
# HW 2

# Assigned: April 7, 2022
# Due: April 12, 2022 11:59pm

# This is the second programming assignment of the computer science track.
# For each function, a skeleton is provided, where your job is to fill the *TODO* out.
# The questions will cover the topics learned in the second lecture, which entailed
# recursive functions, for and while loops, string indexing, and linked lists.

# This function takes a natural number as an argument (so it can't be negative) 
# and returns a boolean value of true or false that shows whether the inputted 
# number is a palindrome or not. A palindrome is something that reads the same 
# backward as forward (i.e. '2002'). Use a for or while for the implementation 
# of this function.
# Ex) iterative_palindrome(1) -> true
#     iterative_palindrome(12) -> false
#     iterative_palindrome(2468642) -> true
def iterative_palindrome(n):
    store=n
    reverse=n
    while (n>0):
        last=n%10
        n=n//10
        reverse=(reverse*10)+last
    if (store==reverse):
        return True
    else:
        return False
print(iterative_palindrome(2))
print(iterative_palindrome(27))
print(iterative_palindrome(2002))


# This function is the same as iterative_palindrome() except instead of using a
# loop, implement the function in a recursive way.
# Ex) recursive_palindrome(1) -> true
#     recursive_palindrome(12) -> false
#     recursive_palindrome(2468642) -> true
def recurisve_palindrome(n):
    global reverse
    store=n
    if (n>0):
        last=n%10
        reverse=(reverse*10)+last
        recursive_palindrome(n//10)

    return reverse

print(iterative_palindrome(2))
print(iterative_palindrome(27))
print(iterative_palindrome(2002))


# Helper function for sum_factorials(). Takes a number as an argument and returns
# the factorial of that number.
# Ex) factorial(1) -> 1
#     factorial(4) -> 24
#     factorial(7) -> 5040
def factorial(n):
    fact=1
    for x in range(1,n+1):
        fact=fact*x
    return fact

print(factorial(3))

# Helper function for sum_factorials(). Takes a number as an argument and returns
# a boolean value of true or false that shows whether the inputted number is a 
# prime or not.
# Ex) is_prime(7) -> true
#     is_prime(12) -> false
#     is_prime(23) -> true
def is_prime(n):
    if n>1:
        for x in range(2,n):
            if(n%x)==0:
                return False
    return True

# Function that creates a node to help testing of sum_factorials()
class Node:
    def __init__(self, content): 
        self.content = content
        self.content = next

# Function to insert a node to the beginning of a linked list
def push(head_ptr, new_content):
    new_node = Node(0)
    new_node.content = new_content
    new_node.next = (head_ptr)
    (head_ptr) = new_node
    return head_ptr

# This function takes a pointer to the head node of the linked list as an argument
# and returns the sum of factorials of prime numbers in the linked list. Above are
# two helper functions for this that are highly recommended.
# Ex) lst = None
#     lst = push(lst, 2)
#     lst = push(lst, 14)
#     lst = push(lst, 5)
#     lst = push(lst, 3)
#     lst = push(lst, 6)
#     sum_factorials(lst) -> 128
def sum_factorials(head_ptr):
    sum = 0
    currentnode = head_ptr
    while (currentnode != None):
        if (is_prime(currentnode.content)):
            sum += factorial(currentnode.content)
        currentnode = currentnode.next
    return sum

list = None
lst = push(lst, 2)
lst = push(lst, 14)
lst = push(lst, 5)
lst = push(lst, 3)
lst = push(lst, 6)
print(sum_factorials(lst))
