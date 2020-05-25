# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from .atom import Atom

class Chain:
    def __init__(self, data, name):
        self._data = data
        if isinstance(name, int):
            self._name = data.i2ch[name]
        else:
            self._name = name

    def residues(self):
        pass

    def atoms(self):
        for i in self._data.chain_r[self._name]:
            yield Atom(self._data, i)

    def __getitem__(self, i):
        pass
