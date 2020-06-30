# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
import re

from .atom import Atom
from .chain import Chain

class PDB:
    """
    Class representing a Protein Data Bank file, i.e. a protein
    structure. The underlying structure is a pandas dataset, however,
    it can be accesseed using
    pdb[<chain>][<residue-num>][<atom-name>], i.e.  pdb['A'][1]["CA"]
    will yield the CA-atom of the first residue of chain 'A'.
    """

    def __init__(self, pdb_file=sys.stdin):
        """
        Constructor, takes file-handler as input, otherwise the standard input.
        """
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

        self._chains = []
        self._id2i   = {} # chainID to chainIndex
        for i, ch in enumerate(ch_names):
            self._chains.append(slice(starts[i], ends[i]))
            self._id2i[ch] = i

        self._iter_i = 0

    def __getitem__(self, ch):
        """Returns chain with either chainID `ch` or with index `ch`."""
        if isinstance(ch, str):
            return Chain(self._lines, self._chains[self._id2i[ch.upper()]])

        return Chain(self._lines, self._chains[ch])

    def __iter__(self):
        self._iter_i = 0
        return self

    def __next__(self):
        if self._iter_i < len(self._chains):
            self._iter_i += 1
            return Chain(self._lines, self._chains[self._iter_i - 1])

        raise StopIteration

    def __len__(self):
        return len(self._chains)

    def atoms(self):
        """
        return a atom iterator
        """
        for i in range(len(self._lines)):
            yield Atom(self._lines, i)

    def residues(self):
        """
        return a residue iterator
        """
        for ch in self:
            for res in ch:
                yield res

    def write(self, f=sys.stdout):
        """Write pdb to file-handler, otherwise standard output."""
        for ch in self:#.chains():
            ch.write(f)
        f.write("END\n")
