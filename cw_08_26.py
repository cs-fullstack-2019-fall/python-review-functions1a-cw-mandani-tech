# # Python review function introduction
#
# ### Problem 1
# Create a ```printNumbers``` function to print integers from -25 to 20 to the console (print in the function)

def printNumbers():
    for indx in range(-25, 21):
        print(indx)


printNumbers()


# ### Problem 2
# Create a function called checkPassword. Send two string variables to the checkPassword function to check if the strings are equal.
# Return true if they are equal and false if they are not equal. Print the function's return value.

def checkPassword(string1, string2):
    if (string1 == string2):
        return True
    else:
        return False

# !! : this could easily be user input 
result = checkPassword("I am a superwoman", "I am not a superman")
print(result)


#
# ### Problem 3
# Write a function that determines if a number passed to it is odd or even.
# Pass a number of your choosing (using input a good idea) and then using the result from the function,
# print if the number was even or not.
#
# examples:
# ```
# The number 12 is an even number!
#
# The number 5 is an odd number!
# ```

def oddOrEven(number):
    if (number % 2 == 0):
        return (f"The number {number} is an Even Number")
    else:
        return (f"The number {number} is an Odd Number")


usernumber = int(input("Please Enter a number here : "))
endResult = oddOrEven(usernumber)
print(endResult)


# ### Problem 4
# * Create a function for the challenge that you call from your ```main```
# * Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```)
# and returns a string using the passed in greeting and 'World' (ex. ```Howdy World!```)
# * From your *first* function, call the function(s) and print out the final result returned

def main():
    result1 = second()
    newResult = third(result1)
    print(newResult)


def second():
    # !! : this could easily be user input 
    greeting = " Howdy"
    return greeting


def third(g1):
    newString = g1 + "  Word!"
    return newString


main()

#
# ### Problem 5:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.

def quitOnQ():
    userNumber=""
    while (userNumber!= 'q'):
        print ("I will iterate")
        userNumber=input("Enter q to quit :")
quitOnQ()


# ### Challenge
# Create a function that accepts 2 numbers. When the function is called return the sum, difference, product,
# and quotient as 4 separate return values.
#
# Print the 4 results that are returned using f-strings.
#
# Example: If 2 and 6 are passed into the function, output should be similar to the following:
#
# ```
# The sum of 2 + 6 is 8
# The difference of 2 - 6 is  -4
# The product of 2 * 6 is 12
# The quotient of 2 / 6 is .333
# ```



def calculations():
    number1= int(input("Enter first Number :"))
    number2= int(input("Enter second Number :"))
    sum=(f"Sum of {number1} and {number2} is  ", number1+number2)
    difference=(f"Difference of {number1} and {number2} is   ", number1-number2)
    product=(f"Product of {number1} and {number2} is  ", number1*number2)
    quotient=(f"The quotient of {number1}  and {number2} is   " , number1/number2)
    return sum,difference,product,quotient
result1_sum,result2_diff,result3_pro,result4_quo = calculations()
print(result1_sum, result2_diff, result3_pro ,result4_quo)
