#!/usr/bin/python
# -*- coding: latin-1 -*-

# Script for converting capitalized and plural art vocabulary terms to lowercae singular, 
# more appropriate for OpenRefine reconciliation to Wikidata
# by Andrew Lih (Wikipedia User:Fuzheado)

# Use pattern package - https://www.clips.uantwerpen.be/pages/pattern-en
from pattern.text.en import singularize

with open('list.txt', 'rb') as textfile:
    plurals = [line.strip() for line in textfile.readlines()]

singles = [singularize(plural.lower()) for plural in plurals]

# print singles
print("\n".join(singles))
