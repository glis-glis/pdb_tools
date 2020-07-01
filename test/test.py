#!/usr/bin/env python3

# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math
import os
import random
import string
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pdb_tools import PDB
from pdb_tools import FASTA
from pdb_tools.amino import acids

def pdb_test():
    mnb = PDB(open("input/1mnb.pdb", "r"))
    zev = PDB(open("input/3zev.pdb", "r"))

    assert len(mnb) == len(mnb._chains) == 1
    assert len(zev) == len(zev._chains) == 4
    for c in "ABCD":
        assert c in zev._id2i

def chain_test():
    zev = PDB(open("input/3zev.pdb", "r"))
    assert len(zev) == 4
    assert len(zev[0]) == 307
    for ch, c1, c2 in zip(zev, "ABCD", "EFGH"):
        assert ch.chainID == c1
        ch.chainID = c2
        assert ch.chainID == c2

def residue_test():
    zev = PDB(open("input/3zev.pdb", "r"))
    assert len(zev[0][0]) == 7
    for ch in zev:
        for i, r in enumerate(ch):
            assert r.resName in acids[3]
            r.resSeq = i
            r.resName = "AAAAA"
            assert int(r.resSeq) == i
            assert r.resName == "AAA"

def rand_name(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

def atom_test():
    pdb = PDB(open("input/1mnb.pdb", "r"))
    i = 1
    for ch in pdb:
        for res in ch:
            for a in res:
                a.serial = i
                assert a.serial == i
                i += 1

                n      = rand_name(i%8 + 4)
                a.name = n
                assert a.name == n[:4]

                n        = rand_name(i%3 + 1)
                a.altLoc = n
                assert a.altLoc == n[0]

                n       = rand_name(i%3 + 1)
                a.iCode = n
                assert a.iCode == n[0]

                x = random.uniform(-1e7, 1e7)
                a.x = x
                assert math.isclose(a.x, x, rel_tol=1e-02)
                a.x = 1e8
                assert math.isclose(a.x, 1e7, rel_tol=1e-02) # max in pdb

                y = random.uniform(-1e7, 1e7)
                a.y = y
                assert math.isclose(a.y, y, rel_tol=1e-02)
                a.y = 1e8
                assert math.isclose(a.y, 1e7, rel_tol=1e-02) # max in pdb

                z = random.uniform(-1e7, 1e7)
                a.z = z
                assert math.isclose(a.z, z, rel_tol=1e-02)
                a.z = 1e8
                assert math.isclose(a.z, 1e7, rel_tol=1e-02) # max in pdb

                occ = random.uniform(-1e5, 1e5)
                a.occupancy = occ
                assert math.isclose(a.occupancy, occ, rel_tol=1e-02)
                a.occupancy = 1e6
                assert math.isclose(a.occupancy, 1e5, rel_tol=1e-02) # max of pdb

                temp = random.uniform(-1e5, 1e5)
                a.tempFactor = temp
                assert math.isclose(a.tempFactor, temp, rel_tol=1e-02)
                a.tempFactor= 1e6
                assert math.isclose(a.tempFactor, 1e5, rel_tol=1e-02) # max of pdb

                n         = rand_name(i%3 + 2)
                a.element = n
                assert a.element == n[:2]

                n         = rand_name(i%3 + 2)
                a.charge  = n
                assert a.charge == n[:2]

                # Warning: This is only for testing!
                # In real code, use res.resName = n, to set the same value
                # for all atoms in a residue
                n         = rand_name(i%6 + 3)
                a.resName = n
                assert a.resName == n[:3]

                # Warning: This is only for testing!
                # In real code, use ch.chainID= n, to set the same value
                # for all atoms in a chain
                n         = rand_name(i%2 + 1)
                a.chainID = n
                assert a.chainID == n[0]

                # Warning: This is only for testing!
                # In real code, use res.resSeq = i, to set the same value
                # for all atoms in a residue
                a.resSeq = i
                assert a.resSeq == i




def fasta_test():
    fasta = FASTA(open("output/1mnb.fasta", "r"))
    assert len(fasta) == 1
    for s in fasta[0]:
        assert s in acids[1]

if __name__ == "__main__":
    pdb_test()
    chain_test()
    residue_test()
    atom_test()
    fasta_test()
