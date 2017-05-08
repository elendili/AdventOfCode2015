#!/usr/bin/python -u
import sys, argparse
import re
from random import shuffle

instructions = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg""".split('\n')
desired_molecule = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

#

# instructions = """H => HO
# H => OH
# O => HH
# e => H
# e => O""".split('\n')
# desired_molecule = "HOHOHO"

replacements = [(v, k) for k, v in (re.findall('\w+', line) for line in instructions if line)]
replacements.sort(key=lambda g: len(g[0]),reverse=True)

def next_min_molecules(om,nm_set,replacements):
    min_len=len(om)
    for index,item in enumerate(replacements):
        mol1,mol2=item
        indexes_of_mol1=[m.start() for m in re.finditer(mol1, om)]
        lenm = len(mol1)
        for i in indexes_of_mol1:
            nm=om[:i] + mol2 + om[i+lenm:]
            if len(nm)==min_len:
                nm_set.add(nm)
            elif len(nm)<min_len:
                min_len=len(nm)
                nm_set.clear()
                nm_set.add(nm)
    return nm_set

found=False
nm_set=set()
while (not found):
    if len(nm_set)==0:
        i=1
        nm_set=next_min_molecules(desired_molecule, set(),replacements)
        shuffle(replacements)
        print 'oops'
    o_set = nm_set

    nm_set=set()
    i+=1
    for m in o_set:
        nm_set = next_min_molecules(m,nm_set,replacements)
        if 'e' in nm_set:
            found=True
            break


print 'step: ', i,' ', found