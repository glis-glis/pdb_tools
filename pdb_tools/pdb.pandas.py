# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Comments: This is just too slow, so the pandas idea got abandoned

import sys
import pandas as pd

from .chain import Chain
from .residue import Residue
from .atom import Atom

BB   = ["N", "CA", "C", "O"]

three21 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

aas = set(three21.keys())

one23 = {v: k for k, v in three21.items()}

class PDB:
    """
    Class representing a Protein Data Bank file. The underlying structure is
    a pandas dataset, however, it can be accesseed using
    pdb[<chain>][<residue-num>][<atom-name>], i.e.
    pdb['A'][1]["CA"] will yield the CA-atom of the first residue of chain 'A'.
    """

    def __init__(self, pdb_file=sys.stdin):
        """
        Constructor, takes file-handler as input, otherwise the standard input.
        """
        cspecs = [(0, 6), (6, 11), (12, 16), (16, 17), (17, 20), (21, 22),
                  (22, 26), (26, 27), (30, 38), (38, 46), (46, 54), (54, 60),
                  (60, 66), (76, 78), (78, 80)]
        names  = ["tag", "serial", "name", "altLoc", "resName", "chainID",
                  "resSeq", "iCode", "x", "y", "z", "occupancy", "tempFactor",
                  "element", "charge"]
        dtype  = {"tag": "str", "serial": "int64", "name": "str",
                  "altLoc": "str", "resName": "str", "chainID": "str",
                  "resSeq": "int64", "iCode": "str", 
                  "x": "float64", "y": "float64", "z": "float64",
                  "occupancy": "float64", "tempFactor": "float64",
                  "element": "str", "charge": "str"}
        df     = pd.read_fwf(pdb_file, colspecs=cspecs, header=None, names=names,
                             keep_default_na=False)
        self._data   = df[df.tag == "ATOM"].astype(dtype).reset_index(drop=True)
        self._chains = self._data.chainID.unique()
        del df

    def __getitem__(self, ch):
        """Returns chain with either chainID `ch` or with index `ch`."""
        if isinstance(ch, int):
            chainID = self._chains[ch]
            return Chain(self._data, chainID)

        return Chain(self._data, ch)

    def residues(self):
        pass

    def chains(self):
        """Returns an iterator with all chains"""
        for ch in self._chains:
            yield Chain(self._data, ch)

    def atoms(self):
        """Return all atoms"""
        for i in self._data.index:
            yield Atom(self._data, i)

    def write(self, f=sys.stdout):
        """Write pdb to file-handler, otherwise standard output."""
        for c in self.chains():
            c.write(f)
        f.write("END\n")

sf = "ATOM  %5i %4s%1s%3s %1s%4i%1s   %8s%8s%8s%6.2f%6.2f          %2s%2s\n"

def a2str(atom):
    if len(atom) >= 4:
        return atom[:4]

    if atom[0].isdigit():
        return "%-4s"%atom

    return " %-3s"%atom
