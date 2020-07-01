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

    def _parse_seq(self, fasta_seq):
        """
        Parse `fasta_seq`, which needs to be an iterator yielding strings.
        Throws if the number of comments is not the same as number of sequences
        """
        for l in fasta_seq:
            if l.startswith(">"):
                self._sqs.append("")
                self._comments.append(l.strip())
                continue

            self._sqs[-1] = "".join([self._sqs[-1], l.strip()])
        assert len(self._sqs) == len(self._comments)

    def __init__(self, fasta_seq=sys.stdin):
        """
        Constructor, takes file-handler as input, otherwise the standard input.
        Fasta seq can be either a file or a list of strings.
        """
        self._sqs      = []
        self._comments = []
        if fasta_seq:
            self._parse_seq(fasta_seq)

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

    def write(self, f=sys.stdout):
        """Write fasta sequence"""
        for c, s in zip(self._comments, self._sqs):
            lo = [c]
            while len(s) > 70:
                lo.append(s[:70])
                s = s[70:]
            lo.append(s)
            f.write("\n".join(lo))
            f.write("\n")
