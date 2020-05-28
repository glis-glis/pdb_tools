# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
import pandas as pd

from .atom import Atom

class Chain:
    """
    Class representing a protein chain. It has a pointer to the pdb-dataset
    and the chainID.
    """
    def __init__(self, data, chainID):
        self._data = data
        self._chainID = chainID

    def residues(self):
        pass

    def atoms(self):
        for i in self._data.loc[self._data.chainID == self._chainID].index:
            yield Atom(self._data, i)

    def __getitem__(self, i):
        pass

    def write(self, f=sys.stdout):
        sf = "ATOM  %5i %-4s%1s%3s %1s%4i%1s   %8s%8s%8s%6.2f%6.2f          %2s%2s\n"
        data = self._data
        for i in self._data.loc[self._data.chainID == self._chainID].index:
            sout = sf%(data.iat[i, 1], data.iat[i, 2], data.iat[i, 3], data.iat[i, 4],
                   data.iat[i, 5], data.iat[i, 6], data.iat[i, 7],
                   "%8.3f"%data.iat[i, 8], "%8.3f"%data.iat[i, 9],
                   "%8.3f"%data.iat[i, 10], data.iat[i, 11], data.iat[i, 12],
                   data.iat[i, 13], data.iat[i, 14])

            f.write(sout)

        #for a in self.atoms():
        #    a.write(f)
        f.write("TER\n")
        #print("TER", file=f)
