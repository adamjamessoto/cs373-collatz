#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import (
    collatz_read, collatz_eval, collatz_print, collatz_solve,
    find_cycle_length, find_starting_point, find_ending_point,
    check_even_odd, acceptance_test_gen )

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 999999\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 999999)

    def test_read_3 (self) :
        r = StringIO.StringIO("528 292\n 300 450\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  528)
        self.assert_(j == 292)
        (i, j) = p.next()
        self.assert_(i == 300)
        self.assert_(j == 450)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval((1, 10))
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200))
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval((1000, 10000))
        self.assert_(v == 262)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 999999), 525)
        self.assert_(w.getvalue() == "1 999999 525\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        print w.getvalue()
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n999 1000\n99999 100000\n1000000 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        print w.getvalue()
        self.assert_(w.getvalue() == "1 1 1\n999 1000 112\n99999 100000 227\n1000000 1000000 153\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("794830 945413\n877637 958120\n425505 783680\n281057 940251\n126406 352861\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "794830 945413 525\n877637 958120 507\n425505 783680 509\n281057 940251 525\n126406 352861 443\n")
    
    # -----------------
    # find_cycle_length
    # -----------------

    def test_find_cycle_length_1 (self) :
        v = find_cycle_length(26)
        self.assert_(v == 11)

    def test_find_cycle_length_2 (self) :
        v = find_cycle_length(4)
        self.assert_(v == 3)

    def test_find_cycle_length_3 (self) :
        v = find_cycle_length(5)
        self.assert_(v == 6)

    def test_find_cycle_length_4 (self) :
        v = find_cycle_length(5)
        self.assert_(v == 6)

    def test_find_cycle_length_5 (self) :
        self.assertRaises(AssertionError, find_cycle_length, 0)

    # -------------------
    # find_starting_point
    # -------------------

    def test_find_starting_point_1 (self) :
        v = find_starting_point(1, 10)
        self.assert_(v == 1)

    def test_find_starting_point_2 (self) :
        v = find_starting_point(15, 13)
        self.assert_(v == 13)

    def test_find_starting_point_3 (self) :
        v = find_starting_point(5, 30)
        self.assert_(v == 5)

    # -----------------
    # find_ending_point
    # -----------------

    def test_find_ending_point_1 (self) :
        v = find_ending_point(1, 10)
        self.assert_(v == 10)

    def test_find_ending_point_2 (self) :
        v = find_ending_point(15, 13)
        self.assert_(v == 15)

    def test_find_ending_point_3 (self) :
        v = find_ending_point(5, 30)
        self.assert_(v == 30)

    # --------------
    # check_even_odd
    # --------------

    def test_check_even_odd_1 (self) :
        v = check_even_odd(1)
        self.assert_(v == 4)

    def test_check_even_odd_2 (self) :
        v = check_even_odd(999999)
        self.assert_(v == 2999998)

    def test_check_even_odd_2 (self) :
        v = check_even_odd(1000)
        self.assert_(v == 500)

    def test_acceptance_test_gen(self) : 
        acceptance_test_gen()

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."