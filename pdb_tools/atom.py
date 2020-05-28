# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys

names  = ["tag", "serial", "name", "altLoc", "resName", "chainID",
            "resSeq", "iCode", "x", "y", "z", "occupancy", "tempFactor",
            "element", "charge"]

k2i = {n: i for i, n in enumerate(names)}

class Atom(object):
    def __init__(self, data, index):
        object.__setattr__(self, "_data", data)
        object.__setattr__(self, "_i", index)
        object.__setattr__(self, "_keys", data.keys())

    def __getattr__(self, key):
        #if key in object.__getattribute__(self, "_keys"):
        return self._data.at[self._i, key]

        #return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        #if key in object.__getattribute__(self, "_keys"):
        self._data.at[self._i, key] = value
        #else:
        #    object.__setattr__(self, key, value)

    def write(self, f=sys.stdout):
        #f.write(self.serial, self.name, self.altLoc, self.resName, self.chainID,
        #      self.resSeq, self.iCode, self.x, self.y, self.z,
        #      self.occupancy, self.tempFactor, self.element, self.charge)

        sf = "ATOM  %5i %-4s%1s%3s %1s%4i%1s   %8s%8s%8s%6.2f%6.2f          %2s%2s\n"
        #sout = sf%(self.serial, self.name, self.altLoc, self.resName, self.chainID,
        #           self.resSeq, self.iCode,
        #           "%8.3f"%self.x, "%8.3f"%self.y, "%8.3f"%self.z,
        #           self.occupancy, self.tempFactor, self.element, self.charge)
        data = self._data
        i    = self._i

        sout = sf%(data.iat[i, 1], data.iat[i, 2], data.iat[i, 3], data.iat[i, 4],
                   data.iat[i, 5], data.iat[i, 6], data.iat[i, 7],
                   "%8.3f"%data.iat[i, 8], "%8.3f"%data.iat[i, 9],
                   "%8.3f"%data.iat[i, 10], data.iat[i, 11], data.iat[i, 12],
                   data.iat[i, 13], data.iat[i, 14])

        f.write(sout)
        #print(sout, file=f)
