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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, find_cycle_length, find_starting_point, find_ending_point

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    
    # def test_find_cycle_length_1 (self) :
    #     v = find_cycle_length(22)
    #     self.assert_(v == 16)

    # def test_find_cycle_length_2 (self) :
    #     v = find_cycle_length(4)
    #     self.assert_(v == 3)

    # def test_find_cycle_length_3 (self) :
    #     v = find_cycle_length(5)
    #     self.assert_(v == 6)

    # def test_find_starting_point_1 (self) :
    #     v = find_starting_point(1, 10)
    #     self.assert_(v == 1)

    # def test_find_starting_point_2 (self) :
    #     v = find_starting_point(15, 13)
    #     self.assert_(v == 13)

    # def test_find_starting_point_3 (self) :
    #     v = find_starting_point(5, 30)
    #     self.assert_(v == 5)

    # def test_find_ending_point_1 (self) :
    #     v = find_ending_point(1, 10)
    #     self.assert_(v == 10)

    # def test_find_ending_point_2 (self) :
    #     v = find_ending_point(15, 13)
    #     self.assert_(v == 15)

    # def test_find_ending_point_3 (self) :
    #     v = find_ending_point(5, 30)
    #     self.assert_(v == 30)

    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)

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
        v = collatz_eval((201, 210))
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."