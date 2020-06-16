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
            starts.append(next(i for i, l in enumerate(lines[indexes],
                                                       start=indexes.start)
                               if l[5] == r))

        ends = starts[1:]
        ends.append(indexes.stop)

        self._residues = []
        self._resSeq   = {}
        for i, r in enumerate(res_seq):
            self._residues.append(slice(starts[i], ends[i]))
            self._resSeq[r] = i

        self._iter_i = 0

    @property
    def chainID(self):
        return self._lines[self._indexes][0][4]

    @chainID.setter
    def chainID(self, value):
        ci = value[0] # Making sure the formatting remains correct
        for l in self._lines[self._indexes]:
            l[4] = ci

    def __iter__(self):
        self._iter_i = 0
        return self

    def __next__(self):
        if self._iter_i < len(self._residues):
            self._iter_i += 1
            return Residue(self._lines, self._residues[self._iter_i - 1])

        raise StopIteration

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
        return Residue(self._lines, i)

    def write(self, f=sys.stdout):
        for l in self._lines[self._indexes]:
            f.write(f"ATOM  {l[0]} "
                f"{l[1]}{l[2]}{l[3]} "
                f"{l[4]}{l[5]}{l[6]}   "
                f"{l[7]}{l[8]}{l[9]}{l[10]}{l[11]}          "
                f"{l[12]}{l[13]}\n")
        f.write("TER\n")
