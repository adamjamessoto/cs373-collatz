#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------




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
    start = find_starting_point(i, j)
    end = find_ending_point(i, j)
    max = 0

    for num in range (start, end) : 
        cycle = find_cycle_length(num)

        if(cycle > max) : 
            max = cycle

    # v = 1
    # assert v > 0
    # return v

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
    """
    global cache 


    if(n == 1) :
        return 1

    if(n < 1000000 and cache[n] != 0) :
        return cache[n]

    num = check_even_odd(n)
    cycle_length = 1 + find_cycle_length(num)


    if(n < 1000000) :
        cache[n] = cycle_length

    return cycle_length


def find_starting_point(i, j) :
    """
    given 2 interger, this method 
    returns the smallest of the 2
    """
    start = i

    if(j <= i) : 
        start = j

    return start

def find_ending_point(i, j) : 
    """
    given 2 integers, this method
    returns the largest of the 2
    """
    end = j

    if(i >= j) :
        end = i

    return end

def check_even_odd(i) :
    if((i % 2) == 0) :
        i = i / 2

    else :
        i = (3 *i) + 1

    return i


























