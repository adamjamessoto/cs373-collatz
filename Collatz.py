#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

import random
import StringIO


"""
global array to use as a cache
"""
cache = [0] * 1000000

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        yield [b, e]
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval ((i, j)) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """

    if(find_starting_point(i, j)) :
        start = i
        end = j

    else :
        start = j
        end = i

    max = 0
    mid_end = end >> 1

    """
    Using the fact that there are two integers, b and e, 
    let m = e / 2. If b < m, then 
    max_cycle_length(b, e) = max_cycle_length(m, e)
    """

    if(start < mid_end) :
        for num in range (start, end + 1) :
            cycle = find_cycle_length(num)

            if(cycle > max) : 
                max = cycle

    else :
        for num in range (start, end + 1) : 
            cycle = find_cycle_length(num)

            if(cycle > max) : 
                max = cycle

    assert max > 0
    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """

    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)

def find_cycle_length(n) :
    """
    going to  calculate the length of a cycle

    n is odd: (3 * n + 1) / 2 = n + (n >> 1) + 1
    n is even: (n / 2) = (n >> 1)
    """
    assert n > 0

    global cache 

    if(n == 1) :
        return 1

    if(n < 1000000 and cache[n] != 0) :
        return cache[n]

    
    if((n % 2) == 0) :
        num = n >> 1
        cycle_length = 1 + find_cycle_length(num)

    else :
        num = n + (n >> 1) + 1
        cycle_length = 2 + find_cycle_length(num)
    
    if(n < 1000000) :
        cache[n] = cycle_length


    assert cycle_length > 0
    return cycle_length

def find_starting_point(i, j) :
    if(i <= j) :
        return True

    return False 

def acceptance_test_gen() :
    """
    creating acceptance tests by generating
    random numbers and printing the pairs
    """

    for x in range(2000) :
        first = random.randint(1, 1000000)
        second = random.randint(1, 1000000)

        if(first == second) :
            second = random.randint(1, 1000000)

        line = str(first) + " " + str(second)

        print line
        