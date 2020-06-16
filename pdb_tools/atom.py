# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys

# key to index
key2i = {"serial": 0, "name": 1, "altLoc": 2, "resName": 3,
          "chainID": 4, "resSeq": 5, "iCode": 6,
          "x": 7, "y": 8, "z": 9,
          "occupancy": 10, "tempFactor": 11,
          "element": 12, "charge": 13}

# Filed names keys
keys   = key2i.keys()

class Atom:
    """
    Class representing one atom.
    Internaly, it has a pointer to the list of all atoms and an index in the list.
    """
    def __init__(self, lines, index):
        self._lines = lines
        self._index = index

    @property
    def serial(self):
        return int(self._lines[self._index][0])

    @serial.setter
    def serial(self, value):
        self._lines[self._index][0] = ("%5d"%value)[:5]

    @property
    def name(self):
        return self._lines[self._index][1].strip()

    @name.setter
    def name(self, value):
        #I did not invent these rules!
        if len(value) >= 4:
            self._lines[self._index][1] = value[:4]
        elif value[0].isdigit():
            self._lines[self._index][1] = "%-4s"%value
        else:
            self._lines[self._index][1] = " %-3s"%value

    @property
    def altLoc(self):
        return self._lines[self._index][2]

    @altLoc.setter
    def altLoc(self, value):
        self._lines[self._index][2] = value[0]

    @property
    def resName(self):
        return self._lines[self._index][3]

    @resName.setter
    def resName(self, value):
        self._lines[self._index][3] = value[:3]

    @property
    def chainID(self):
        return self._lines[self._index][4]

    @chainID.setter
    def chainID(self, value):
        self._lines[self._index][4] = value[0]

    @property
    def resSeq(self):
        return int(self._lines[self._index][5])

    @resSeq.setter
    def resSeq(self, value):
        self._lines[self._index][5] = ("%4d"%value)[:4]

    @property
    def iCode(self):
        return self._lines[self._index][6]

    @iCode.setter
    def iCode(self, value):
        self._lines[self._index][6] = value[0]

    @property
    def x(self):
        return float(self._lines[self._index][7])

    @x.setter
    def x(self, value):
        self._lines[self._index][7] = ("%8.3f"%value)[:8]

    @property
    def y(self):
        return float(self._lines[self._index][8])

    @y.setter
    def y(self, value):
        self._lines[self._index][8] = ("%8.3f"%value)[:8]

    @property
    def z(self):
        return float(self._lines[self._index][9])

    @z.setter
    def z(self, value):
        self._lines[self._index][9] = ("%8.3f"%value)[:8]

    @property
    def occupancy(self):
        return float(self._lines[self._index][10])

    @occupancy.setter
    def occupancy(self, value):
        self._lines[self._index][10] = ("%6.2f"%value)[:6]

    @property
    def tempFactor(self):
        return float(self._lines[self._index][11])

    @tempFactor.setter
    def tempFactor(self, value):
        self._lines[self._index][11] = ("%6.2f"%value)[:6]

    @property
    def element(self):
        return self._lines[self._index][11]

    @element.setter
    def element(self, value):
        self._lines[self._index][11] = value[:2]

    @property
    def charge(self):
        return self._lines[self._index][12]

    @charge.setter
    def charge(self, value):
        self._lines[self._index][12] = value[:2]

    def write(self, f=sys.stdout):
        l = self._lines[self._index]
        f.write(f"ATOM  {l[0]} "
                f"{l[1]}{l[2]}{l[3]} "
                f"{l[4]}{l[5]}{l[6]}   "
                f"{l[7]}{l[8]}{l[9]}{l[10]}{l[11]}          "
                f"{l[12]}{l[13]}\n")
