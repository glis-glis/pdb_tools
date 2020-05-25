# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys

class Atom():
    def __getattr__(self, key):
        if key == "one":
            return 1
        elif key == "two":
            return 2


class Atoold:
    def __init__(self, data, index):
        self._data = data
        self._i    = index

    @property
    def type(self):
        return self._data.atom[self._i]

    @type.setter
    def type(self, v):
        self._data.atom[self._i] = v

    @property
    def res(self):
        return self._data.res[self._i]

    @res.setter
    def res(self, v):
        self._data.res[self._i] = v

    @property
    def res_num(self):
        return self._data.res_n[self._i]

    @res_num.setter
    def res_num(self, v):
        self._data.res_n[self._i] = v

    @property
    def chain(self):
        return self._data.chain[self._i]

    @chain.setter
    def chain(self, v):
        self._data.chain[self._i] = v

    @property
    def pos(self):
        return self._data.pos[self._i]

    @pos.setter
    def pos(self, v):
        self._data.pos[self._i] = v

    @property
    def occ(self):
        return self._data.occ[self._i]

    @occ.setter
    def occ(self, v):
        self._data.occ[self._i] = v

    @property
    def temp(self):
        return self._data.temp[self._i]

    @temp.setter
    def temp(self, v):
        self._data.temp[self._i] = v

    @property
    def ele(self):
        return self._data.ele[self._i]

    @ele.setter
    def ele(self, v):
        self._data.ele[self._i] = v

    @property
    def charge(self):
        return self._data.charge[self._i]

    @charge.setter
    def charge(self, v):
        self._data.charge[self._i] = v

    def write(self, f=sys.stdout):
        sf = "ATOM  %5i %-4s %3s %1s%4i    %8s%8s%8s%6.2f%6.2f          %2s%2s"
        sout = sf%(self._i + 1, self.type, self.res, self.chain, self.res_num,
                   "%8.3f"%self.pos[0], "%8.3f"%self.pos[1], "%8.3f"%self.pos[2],
                   self.occ, self.temp, self.ele, self.charge)

        print(sout, file=f)
