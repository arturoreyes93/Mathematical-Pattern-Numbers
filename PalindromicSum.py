#  File: PalindromicSum.py

#  Description: inputs a range of numbers and outputs the number of that range that has the longest cycle length when adding the reverse of that number to itself until attaining a palindromic number

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 02/19

#  Date Last Modified: 02/19

def main():

# define the needed functions

# function 1: reverse the number

    def rev_num(n):

        rev_n = 0

        while n>0:

            rev_n = (rev_n*10)+(n%10)

            n = n//10

        return rev_n

#function 2: check if number is palindromic
    
    def is_palindromic(n):

        return n == rev_num(n)

#function 3: count the iterations until a palindromic number is obtained
    def cycle_length(n):

        counter_length = 0

        while not(is_palindromic(n)):

            n = n + rev_num(n)

            counter_length +=1

        return counter_length 

# prompt the user to enter range values

    start = eval( input( "Enter starting number of the range: "))

    while start<0 :

        start = eval( input( "Enter starting number of the range: "))

    end = eval( input( "Enter ending number of the range: "))

    while end<0 or end<=start :

        end = eval( input( "Enter ending number of the range: "))

# write program algorithm

# check the cycle length of all numbers in range

    num = start

    while num < end :

        length = cycle_length(num) 

        

# create a variable for the number with the longest cycle length

        if cycle_length(num) > length :

            longest_num = num
            max_cycle = cycle_length(num)

        num += 1

    print (" The number " + str(longest_num) + " has the longest cycle length of " + str(max_cycle) + ".")



main()
    
