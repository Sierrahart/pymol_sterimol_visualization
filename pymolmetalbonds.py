#PyMOL Metal Bonds v1.2, J.A.Cadge 2020
#Finds Metal-Element bond lengths up to 2.5 Angstroms (2.8 Angstroms for M-I) and
#draws lost bond from .xyz conversion. (Currently for C, P, N, I)
#Runs with pymolform2.pml

from pymol import cmd, stored

au_c_bonds = cmd.find_pairs('metals', 'n. c', cutoff=2.5)
for pair in au_c_bonds:
    cmd.bond(pair[0], pair[1])
    
au_p_bonds = cmd.find_pairs('metals', 'n. p', cutoff=2.5)
for pair in au_p_bonds:
    cmd.bond(pair[0], pair[1])

au_n_bonds = cmd.find_pairs('metals', 'n. n', cutoff=2.5)
for pair in au_n_bonds:
    cmd.bond(pair[0], pair[1])
    
au_i_bonds = cmd.find_pairs('metals', 'n. i', cutoff=2.8)
for pair in au_i_bonds:
    cmd.bond(pair[0], pair[1])
    
pd_cl_bonds = cmd.find_pairs('metals', 'n. cl', cutoff=2.8)
for pair in pd_cl_bonds:
    cmd.bond(pair[0], pair[1])
