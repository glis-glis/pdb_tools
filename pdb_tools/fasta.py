# Copyright (C) 2020 Andreas Füglistaler <andreas.fueglistaler@epfl.ch>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys

class FASTA:
    """
    Class representing a FASTA file, i.e. a protein sequence.
    """

    def __init__(self, fasta_file=sys.stdin):
        """
        Constructor, takes file-handler as input, otherwise the standard input.
        """
        self._sqs = []
        for l in fasta_file:
            if l.startswith(">"):
                self._sqs.append("")
                continue

            self._sqs[-1] = "".join([self._sqs[-1], l.strip()])

        self._iter_i = 0

    def __getitem__(self, i):
        """
        Return `i`th sequence.
        """
        return self._sqs[i]

    def __iter__(self):
        self._iter_i = 0
        return self

    def __next__(self):
        if self._iter_i < len(self._sqs):
            self._iter_i += 1
            return self._sqs[self._iter_i - 1]

        raise StopIteration

    def __len__(self):
        return len(self._sqs)

    def alignement(self):
        """Return iterator over alignements"""
        l = min([len(sq) for sq in self._sqs])
        for i in range(l):
            yield tuple(sq[i] for sq in self._sqs)
