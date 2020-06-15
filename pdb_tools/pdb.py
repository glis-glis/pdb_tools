# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
import re

from .chain import Chain

BB   = ["N", "CA", "C", "O"]

three21 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

aas = set(three21.keys())

one23 = {v: k for k, v in three21.items()}

class PDB:
    """
    Class representing a Protein Data Bank file. The underlying structure is
    a pandas dataset, however, it can be accesseed using
    pdb[<chain>][<residue-num>][<atom-name>], i.e.
    pdb['A'][1]["CA"] will yield the CA-atom of the first residue of chain 'A'.
    """

    def __init__(self, pdb_file=sys.stdin):
        """
        Constructor, takes file-handler as input, otherwise the standard input.
        """
        self._names  = {"serial": 0, "name": 1, "altLoc": 2, "resName": 3,
                        "chainID": 4, "resSeq": 5, "iCode": 6,
                        "x": 7, "y": 8, "z": 9,
                        "occupancy": 10, "tempFactor": 11,
                        "element": 12, "charge": 13}

        r = re.compile("^ATOM  (.{5}) "
                       "(.{4})(.{1})(.{3}) "
                       "(.{1})(.{4})(.{1})   "
                       "(.{8})(.{8})(.{8})(.{6})(.{6})          "
                       "(.{2})(.{2})$", re.M)

        self._lines = [list(t) for t in r.findall(pdb_file.read())]
        ch_names    = sorted({l[4] for l in self._lines})
        starts      = []

        for ch in ch_names:
            starts.append(next(i for i, l in enumerate(self._lines) if l[4] == ch))

        ends = starts[1:]
        ends.append(len(self._lines))

        self._chains   = []
        self._chainIDs = {}
        for i, ch in enumerate(ch_names):
            self._chains.append(slice(starts[i], ends[i]))
            self._chainIDs[ch] = i


    def __getitem__(self, ch):
        """Returns chain with either chainID `ch` or with index `ch`."""
        pass

    def chains(self):
        """Returns an iterator with all chains"""
        for ch in self._chains:
            yield Chain(self._lines, ch)

    def atoms(self):
        """Return all atoms"""
        pass

    def write(self, f=sys.stdout):
        """Write pdb to file-handler, otherwise standard output."""
        for ch in self.chains():
            ch.write(f)
        f.write("END\n")
