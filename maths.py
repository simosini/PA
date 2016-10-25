#!/usr/bin/env python3
# encoding: UTF-8

#sum all numbers less than 1000 divisible for 3 or 5
import functools

def sum3_or_5() : 
    return functools.reduce(lambda x,y : x+y, filter(lambda x : x%3 == 0 or x%5 == 0, range(3,1000)))
print (sum3_or_5())

#the first number divisible by each of the numbers between 1 and 20

def divisors(n) :
    return [x for x in range (2,int(n**(0.5)+1)) if n%x == 0]
print( divisors(4))
#return primes up to n given
def primes(n) :
    return [x for x in range (2,n) if len(divisors(x)) == 0]
print (primes(100))
#expand numbers to the max power less than 20
def expand_to_20(n) :
    return n if n*n > 20 else expand_to_20 (n*n)

def div_by_all() :
    return functools.reduce(lambda x,y : x*y, map(expand_to_20,(primes(20))))
print(div_by_all())

#calculate the sum of the digits of 2^1000
def sum_digits():
    return sum(int(x) for x in  str(2**1000))
print(sum_digits())    

#the first term in fibonacci series that contains 1000 digits
def fib_nth(n) :
    def fib() :
        a,b = 0,1
        while len(n) < 1000 :
            yield a 
            a,b = b,a+b

 
    


#if __name__ == '__main__' :
#    main()
