# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from .atom import Atom

class Residue:
    """
    Class representing a protein residue. It has a pointer to the pdb-lines
    and the atom-indexes.
    """
    def __init__(self, lines, indexes):
        self._lines   = lines
        self._indexes = indexes

    def __getitem__(self, i):
        return Atom(self._lines, i)

    @property
    def resName(self):
        return next(self._lines[self._indexes])[3]

    @resName.setter
    def resName(self, value):
        self._lines[self._indexes][3] = value

    @property
    def resSeq(self):
        return next(self._lines[self._indexes])[5]

    @resSeq.setter
    def resSeq(self, value):
        self._lines[self._indexes][5] = value

    def atoms(self):
        """
        return a atom iterator
        """
        for i in self._indexes:
            yield Atom(self._lines, i)
