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

class Atom(object):
    """
    Class representing one atom.
    Internaly, it has a pointer to the list of all atoms and an index in the list.
    """
    def __init__(self, lines, index):
        object.__setattr__(self, "_lines", lines)
        object.__setattr__(self, "_index", index)

    def __getattr__(self, key):
        if key in keys:
            ls = object.__getattribute__(self, "_lines")
            i  = object.__getattribute__(self, "_index")
            return ls[i][key2i[key]]

        return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        if key in keys:
            ls = object.__getattribute__(self, "_lines")
            i  = object.__getattribute__(self, "_index")
            ls[i][key2i[key]] = value
        else:
            object.__setattr__(self, key, value)

    def write(self, f=sys.stdout):
        l = self._lines[self._index]
        f.write(f"ATOM  {l[0]} "
                f"{l[1]}{l[2]}{l[3]} "
                f"{l[4]}{l[5]}{l[6]}   "
                f"{l[7]}{l[8]}{l[9]}{l[10]}{l[11]}          "
                f"{l[12]}{l[13]}\n")
