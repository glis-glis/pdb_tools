# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import numpy as np
import pandas as pd

cspecs = [(0, 6), (6, 11), (12, 16), (16, 17), (17, 20), (21, 22), (22, 26),
          (26, 27), (30, 38), (38, 46), (46, 54), (54, 60), (60, 66), (76, 78),
          (78, 80)]
df = pd.read_fwf("3zev.pdb", colspecs=cspecs, header=None,
                 names=["tag", "serial", "name", "altLoc", "resName", "chainID",
                        "resSeq", "iCode", "x", "y", "z", "occupancy",
                        "tempFactor", "element", "charge"])

df[df[0].isin(["ATOM", "TER", "END"]) ]

class Data:
    def __init__(self, pdb_file):
        atom_lines = [l[0:80] for l in pdb_file if l.startswith("ATOM")]
        self.length = len(atom_lines)
        self.atom   = np.zeros(self.length, dtype='U4')
        self.res    = np.zeros(self.length, dtype='U3')
        self.res_n  = np.zeros(self.length, dtype='i')
        self.chain  = np.zeros(self.length, dtype='U1')
        self.pos    = np.zeros((self.length, 3), dtype='f')
        self.occ    = np.zeros(self.length, dtype='f')
        self.temp   = np.zeros(self.length, dtype='f')
        self.ele    = np.zeros(self.length, dtype='U2')
        self.charge = np.zeros(self.length, dtype='U2')

        self.i2ch    = []
        self.chain_r = {}
        self.res_r   = {}
        self._parse_lines(atom_lines)

    def _parse_lines(self, als):
        ch    = als[0][21:22]
        res   = als[0][17:20]
        ch_i  = 0
        res_i = 0

        for i, al in enumerate(als):
            self.atom[i]    = al[12:16]
            self.res[i]     = al[17:20]
            self.res_n[i]   = int(al[22:26])
            self.chain[i]   = al[21:22]
            self.pos[i]     = np.r_[float(al[30:38]), float(al[38:46]),
                                    float(al[46:54])]
            self.occ[i]     = float(al[54:60])
            self.temp[i]    = float(al[60:66])
            self.ele[i]     = al[76:78]
            self.charge[i]  = al[79:81]

            if ch != self.chain[i]:
                self.chain_r[ch] = range(ch_i, i)
                self.i2ch.append(ch)
                ch   = self.chain[i]
                ch_i = i

            if res != self.res[i]:
                self.res_r[res] = range(res_i, i)
                res   = self.res[i]
                res_i = i
        self.chain_r[ch] = range(ch_i, len(self.chain))
        self.i2ch.append(ch)
        self.res_r[res]  = range(res_i, len(self.chain))
