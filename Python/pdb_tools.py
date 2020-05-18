# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
import numpy as np

BB   = ["N", "CA", "C", "O"]

three21 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
			'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
			'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
			'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

aas = set(three21.keys())

one23 = {v: k for k, v in three21.items()}

class Pdb:
	def __init__(self, pdb_file=sys.stdin):
		self._data = Data(pdb_file)

	def __getitem__(self, i):
		pass

	def residues(self, start, end=None):
		pass

	def chain(self, name):
		pass

	def atoms(self):
		for i in range(self._data.length):
			yield Atom(self._data, i)

	def print(self, f=sys.stdout):
		pass

class Data:
	def __init__(self, pdb_file):
		atom_lines = [l for l in pdb_file if l.startswith("ATOM")]
		self.length = len(atom_lines)
		self.atom   = np.zeros(self.length, dtype='U4')
		self.res    = np.zeros(self.length, dtype='U3')
		self.res_n  = np.zeros(self.length, dtype='i')
		self.chain  = np.zeros(self.length, dtype='U1')
		self.pos    = np.zeros((self.length, 3), dtype='f')
		self.occ    = np.zeros(self.length, dtype='f')
		self.temp   = np.zeros(self.length, dtype='f')
		self.ele    = np.zeros(self.length, dtype='U1')
		self.charge = np.zeros(self.length, dtype='U2')

		self.chains = {}
		self.res    = {}
		self._parse_lines(atom_lines)

	def _parse_lines(self, als):
		for i, al in enumerate(als):
			self.atom[i]   = al[12:16]
			self.res[i]    = al[17:20]
			self.res_n[i]  = int(al[22:26])
			self.chain[i]  = al[21::22]
			self.pos[i]    = np.r_[float(al[30:38]), float(al[38:46]),
								  float(al[46:54])]
			self.occ[i]    = float(al[54:60])
			self.temp[i]   = float(al[60:66])
			self.ele[i]    = al[76:78]
			self.charge[i] = al[79:81]

			if not self.chain[i] in self.chains:
				self.chains[self.chain[i]] = i

			if not self.res_n[i] in self.res:
				self.res[self.res_n[i]] = i



class Chain:
	def residues(self, start, end=None):
		pass
	def __getitem__(self, i):
		pass

class Residue:
	def __getitem__(self, i):
		pass
	def type(self):
		pass
	def num(self):
		pass
	def chain(self):
		pass
	def atoms(self):
		pass
	def atom(self, name):
		pass

class Atom:
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
