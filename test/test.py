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
    for ch in zev.chains():
        assert ch.chainID in "ABCD"
        ch.chainID = chr(ord(ch.chainID) + 4)
        assert ch.chainID in "EFGH"

def residue_test():
    zev = PDB(open("input/3zev.pdb", "r"))
    for r in next(zev.chains()).residues():
        #print(r.resName, r.resSeq)
        r.resSeq = 0
        print(r.resName, r.resSeq)
    
residue_test()
