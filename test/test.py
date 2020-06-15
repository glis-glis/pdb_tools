#!/usr/bin/env python3

# Copyright (C) 2019 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pdb_tools import PDB

def pdb_test():
    mnb = PDB(open("input/1mnb.pdb", "r"))
    zev = PDB(open("input/3zev.pdb", "r"))

    assert len(mnb._chains) == 1
    assert len(zev._chains) == 4
    for c in "ABCD":
        assert c in zev._chainIDs

def chain_test():
    zev = PDB(open("input/3zev.pdb", "r"))
    for ch, c1, c2 in zip(zev, "ABCD", "EFGH"):
        assert ch.chainID == c1
        ch.chainID = c2
        assert ch.chainID == c2

def residue_test():
    zev = PDB(open("input/3zev.pdb", "r"))
    for i, r in enumerate(next(zev)):
        r.resSeq = i
        assert int(r.resSeq) == i

pdb_test()
chain_test()
residue_test()
