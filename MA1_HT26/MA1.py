"""
Solutions to module 1
Student: Joel Wittrin
E-mail: wittrin.joel@gmail.com
Reviewed by: Ivan Noreland
Review date: 9/9-26
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have test code running at the top level (i.e. outside the main function),
you have to remove it before uploading your code into Studium!
Also remove any trace and debugging printouts!

You may not import any packages other than time and math. These may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documentation and and don't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """Exc1: Computes m*n using additions"""

    if m == 0 or n == 0:
        return 0

    # minimize recursive iterations
    if m>n:
        return multiply(n, m)
    
    return n + multiply(m-1, n)


def harmonic(n: int) -> float:              
    """Exc2: Computes and returns the harmonic sum 1 + 1/2 + 1/3 + ... + 1/n"""

    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:              
    """Exc3: Returns the binary representation of x"""

    if x < 0:
        return "-" + get_binary(-x)

    if x == 0:
        return "0"
    if x == 1:
        return "1"

    return str( get_binary(x // 2) ) + str(x%2)


def reverse_string(s: str) -> str:        
    """Exc4: Returns the string s reversed """
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


def largest(a: list):
    """Exc5: Returns the largest element in a"""

    if len(a) <= 1:
        return a[0]

    rest = largest(a[1:])
    if a[0] > rest:
        return a[0]
    else:
        return rest


def count(x, s: list) -> int:                
    """Exc6: Counts the number of occurences of x on all levels in s"""
    if len(s) == 0:
        return 0
    if s[0] == x:
        return 1 + count(x, s[1:])
    if type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[1:])


def bricklek(f: str, t: str, h: str, n: int) -> list[str]:
    """Exc7: Returns a list of string instructions for how to move the tiles"""
    if n == 0:
        return []
    
    return bricklek(f, h, t, n-1) + [f+"->"+t] + bricklek(h, t, f, n-1)
    

def fib(n: int) -> int:                      
    """For Exc9: Returns the n:th Fibonacci number"""
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n):
    memory = {0:0, 1:1}

    def _fib_mem(n):
        if n not in memory:
            memory[n] = _fib_mem(n-1) + _fib_mem(n-2)
        return memory[n]
    
    return _fib_mem(n)

def main():

    print('\nCode that demonstrates my implementations\n')

    print( multiply(6, 7))
    print( harmonic(8))
    print( get_binary(13))
    print( reverse_string("Uppsala"))
    print( largest([21, 42, -5, 37]))
    print( bricklek('f', 't', 'h', 5))

    print('\n\nCode for analysing fib and fib_mem\n')

    times = []
    for i in range(31):
        tstart = time.perf_counter()
        fib(i)
        tstop = time.perf_counter()
        times.append(tstop - tstart)

    # skip index 0 as we have no i-1 to divide with, approx. will be sufficient
    for i in range(1, len(times)):
        print(f'Ratio between step {i} and {i-1}: {times[i]/times[i-1]}' )

    print('\n')
    print('Approximation for fib(50) & fib(100):')
    #we repeat tn / t(n-1) = 1.618^n / 1.618^(n-1) i.e.
    t_50 = times[-1] * 1.618 **(50-30)
    t_100 = times[-1] * 1.618 ** (100-30)
    print(f'{t_50 / 60} [minutes]')
    print(f'{t_100 / (365*24*60*60)} [yrs]')

    print('\n')
    print('Calculating fib(100)')
    tstart = time.perf_counter()
    result = fib_mem(100)
    tstop = time.perf_counter()

    print("fib_mem(100) =", result)
    print(f'Time: {tstop - tstart} [s]')



if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the non-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles: 2^50 -1 = 1125899906842623 [s]
                                                            = 35683908 [yrs]
                                                            ≈ 35.7 Myrs
  
                                                            
  Exercise 9: Time for Fibonacci: fib(50) ≈ 25 minutes,
                                  fib(100) ≈ 1 360 000 [yrs]

  
  Exercise 10: Time for fib_mem: 2.3e-05 [s], 354224848179261915075

  
  Exercise 11: Comparison sorting methods: 

    For the insertion sort:
    t(n) = c*f(n) |n=1000 -> 1 = c * 1000^2    (since f(n) = theta(n^2))
                          -> c = 10^-6
    
    t(10^6) = c*(10^6)^2 = 10^6 [s] ≈ 11.57 [days]
    t(10^9) = c*(10^9)^2 = 10^12 [s] ≈ 31 688 [yrs]

    For the merge sort:
    t(n) = c*n*log(n) |@n=1000 -> 1 = c*1000*log(1000)
                               -> c = 0.00010034333

    t(10^6) = ... ≈ 33.3 [min]
    t(10^9) = ... ≈ 34.7 [days]
  

  Exercise 12: Comparison Theta(n) and Theta(n log n):

    We can extract c similar to the previous exc. since: t(n) = c*n*log(n) -> 1 = c*10*log(10)
                                                                           -> c ≈ 0.030103

    We compare the algorithms so that: n < c*n*log(n) -> c^-1 < log(n)
                                                      -> 2^(1/c) < n
                                                      -> n > 10 000 000 048.9

    meaning that algorithm A is quicker for n > ~10B. If we use the exact definition for c we get
    2^(1/10log(10)), i.e. exactly 10^10. 
  
"""
