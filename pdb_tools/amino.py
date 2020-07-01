# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

acids = {1: ['C', 'D', 'S', 'Q', 'K', 'I', 'P', 'T', 'F', 'N', 'G',
             'H', 'L', 'R', 'W', 'A','V', 'E', 'Y', 'M'],
         3: ['CYS', 'ASP', 'SER', 'GLN', 'LYS','ILE', 'PRO', 'THR', 'PHE',
         'ASN','GLY', 'HIS', 'LEU', 'ARG', 'TRP','ALA', 'VAL', 'GLU', 'TYR',
             'MET']}

three21 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

one23 = {v: k for k, v in three21.items()}
