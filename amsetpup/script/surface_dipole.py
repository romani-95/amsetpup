from surfaxe.analysis import cart_displacements, bond_analysis, electrostatic_potential, simple_nn, complex_nn, surface_dipole

sd = surface_dipole('potential.csv')
print(f'The surface dipole D_s is {sd} eV')
