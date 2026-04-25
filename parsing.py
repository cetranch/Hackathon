import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def avgRange(string):
    if isinstance(string, str) and '-' in string:
        try:
            low, high = string.split('-')
            return (float(low) + float(high)) / 2
        except:
            return np.nan

    return float(string)


def getData():
    seed = 94
    np.random.seed(seed)

    filename = 'Sp26_HACKATHON_Data_Shared-with-Students (1)'
    filepath = f'{filename}.csv'
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        print('File not found')
        return
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    data = data.drop(["doi", 'CGsbandgap', 'Oxidation.States_mode','CIsAlkali', 'CIsFBlock', 'CIsMetal', 'CIsMetalloid', 'CNfunfilled', 'COxidation.States', 'Gsbandgap_std', 'IsAlkali_std', 'IsFBlock_std', 'IsMetalloid_std', 'Nfunfilled_std', 'Oxidation.States_std', 'Gsbandgap_mode', 'IsAlkali_mode', 'IsFBlock_mode', 'IsMetal_mode', 'IsMetalloid_mode', 'Nfunfilled_mode', 'Gsbandgap_max', 'IsAlkali_max', 'IsDBlock_max', 'IsFBlock_max', 'IsMetal_max', 'IsMetalloid_max', 'Nfunfilled_max', 'lattice_c.a_min', 'Gsbandgap_min', 'IsAlkali_min', 'IsDBlock_min', 'IsFBlock_min', 'IsMetal_min', 'IsMetalloid_min', 'Nfunfilled_min', 'Nfvalence_min', 'Npunfilled_min', 'Npvalence_min', 'NsUnfilled_min', 'pack.factor_range', 'Gsbandgap_range', 'IsAlkali_range', 'IsFBlock_range', 'IsMetal_range', 'IsMetalloid_range', 'Nfunfilled_range', 'Oxidation.States_range', 'ZungerPP.r_d_mode'], axis=1)

    symbol_to_atomic = {
        "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
        "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
        "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30,
        "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40,
        "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50,
        "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60,
        "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
        "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
        "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90,
        "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100,
        "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109,
        "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118
    }
    col1, col2 = data.columns[0], data.columns[1]
    for col in [col1, col2]:
        data[col] = data[col].str.strip().str.capitalize().map(symbol_to_atomic)

    method_to_numeric = {
        "Electrochemical double-cell": 1,
        "Build-up": 2,
        "Grosky effect": 3,
        "Absorption through cylinders": 4,
        "Radial concentration": 5,
        "Electrochemical (260-340 K) and gas-flow permeability (340-1000 K)": 6,
        "Membrane Permeation": 7,
        "Electromigration-relaxation": 8,
        "Time-lag permeability": 9,
        "Electrochemical break-through time": 10,
        "Gas-phase absorption": 11,
        "Gas absorption": 12
    }

    isotope = {
        "Hydrogen" : 1,
        "Deuterium" : 2
    }
    xtalStruct = {
        "fcc" : 1, "bcc" : 0, "hcp" : 2
    }

    data["Method"] = data["Method"].str.strip().map(method_to_numeric)
    data["Isotope"] = data["Isotope"].str.strip().str.capitalize().map(isotope)
    data["Temperature"] = data["Temperature"].apply(avgRange)
    data["CrystalStruct"] = data["CrystalStruct"].str.strip().map(xtalStruct)
    print(data.head())

    data.to_csv("output.csv", index=False)


getData()






