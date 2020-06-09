# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys

from .atom import Atom
from .residue import Residue

class Chain:
    """
    Class representing a protein chain. It has a pointer to the pdb-lines
    and the atom indexes.
    """
    def __init__(self, lines, indexes):
        self._lines   = lines
        self._indexes = indexes

        res_seq = sorted({l[5] for l in lines[indexes]})
        starts   = []

        for r in res_seq:
            starts.append(next(i for i, l in enumerate(lines[indexes])
                               if l[5] == r))

        ends = starts[1:]
        ends.append(indexes.stop)

        self._residues = []
        self._resSeq   = {}
        for i, r in enumerate(res_seq):
            self._residues.append(slice(starts[i], ends[i]))
            self._resSeq[r] = i

    @property
    def chainID(self):
        return next(self._lines[self._indexes])[4]

    @chainID.setter
    def chainID(self, value):
        self._lines[self._indexes][4] = value

    def residues(self):
        """
        return a residues iterator
        """
        for r in self._residues:
            yield Residue(self._lines, r)

    def atoms(self):
        """
        return a atom iterator
        """
        for i in self._indexes:
            yield Atom(self._lines, i)

    def __getitem__(self, i):
        """
        return residue `i`
        """
        pass

    def write(self, f=sys.stdout):
        for l in self._lines[self._indexes]:
            f.write(f"ATOM  {l[0]} "
                f"{l[1]}{l[2]}{l[3]} "
                f"{l[4]}{l[5]}{l[6]}   "
                f"{l[7]}{l[8]}{l[9]}{l[10]}{l[11]}          "
                f"{l[12]}{l[13]}\n")
        f.write("TER\n")
