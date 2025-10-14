# Initial Statements
import json
from math import gcd
with open("../JSON/OrganicPrefixes.json", 'r') as file:
    prefixes = json.load(file)

# Organic Chemistry
class OrganicCompound:

    # Hydrocarbons
    class Hydrocarbon: # Can use inheritance

        # Alkanes
        class Alkane:
            def __init__(self, carbon):
                self.carbons = carbon
                self.hydrogens = (2 * carbon) + 2
                self.formula = f"C{carbon if carbon != 1 else ""}H{self.hydrogens}"
                self.name = prefixes[str(carbon)] + "ane"

        # Alkenes
        class Alkene:
            def __init__(self, carbon):
                self.carbons = carbon
                self.hydrogens = 2 * carbon
                self.formula = f"C{carbon if carbon != 1 else ""}H{self.hydrogens}"
                self.name = prefixes[str(carbon)] + "ene"

        # Alkynes
        class Alkyne:
            def __init__(self, carbon):
                self.carbons = carbon
                self.hydrogens = (2 * carbon) - 2
                self.formula = f"C{carbon if carbon != 1 else ""}H{self.hydrogens}"
                self.name = prefixes[str(carbon)] + "yne"

    # Alcohols
    class Alcohol:
        def __init__(self, carbon):
            self.name = prefixes[str(carbon)] + "anol (or) " + prefixes[str(carbon)] + "yl alcohol"
            self.formula = (f"{"C" + str(carbon) if carbon > 1 else "C"}H{(2 * carbon) + 1}OH"
                            f" (or) {"C" + str(carbon) if carbon > 1 else "C"}H{(2 * carbon) + 2}O")

    # Ethers
    class Ether:
        def __init__(self, r1, r2):
            self.radical1 = r1
            self.radical2 = r2
            n = r1 + r2
            if r1 == r2:
                self.name = ("Di" + prefixes[str(r1)].lower() +
                    "yl" + " " + "Ether")
                self.formula = (f"(C{r1 if r1 != 1 else ""}H{(2 * r1) + 1})2O"
                                f" (or) C{2 * r1}H{(4 * r1) + 2}O")
            else:
                self.name = (prefixes[str(r1)] + "yl " + prefixes[str(r2)]  +
                    "yl" + " " + "Ether")
                self.formula = (f"C{r1 if r1 != 1 else ""}H{((2 * r1) + 1)}OC{r2}H{(2 * r2) + 1} "
                                f"(or) C{n}H{(2 * n) + 2}O")

    # Carboxylic Acid
    class CarboxylicAcid:
        def __init__(self, carbon):
            self.carbons = carbon
            carbon -= 1
            self.formula = (f"{"C" + str(carbon) if carbon > 1 else "C" if carbon != 0 else ""}"
                            f"H{(2 * carbon) + 1}COOH (or) {"C" + str(carbon) if carbon > 1 else "C"}H{(2 * carbon) + 2}O2 ")
            self.name = prefixes[str(carbon + 1)] + "anoic Acid"
            if self.name == "Methanoic Acid":
                self.formula = "HCOOH (or) CH2O2"
                self.name = "Methanoic Acid (or) Formic Acid"
            if self.name == "Ethanoic Acid":
                self.name = "Ethanoic Acid (or) Acetic Acid"
            if self.name == "Butanoic Acid":
                self.name = "Butanoic Acid (or) Butyric Acid"

    # Aldehydes
    class Aldehyde:
        def __init__(self, carbon):
            self.carbons = carbon
            self.formula = (f"{"C" + str(carbon) if carbon > 1 else "C" if carbon == 1 else ""}H{(2 * carbon) + 1}CHO"
                            f" (or) C{carbon + 1}H{(2 * carbon + 2)}O")
            self.name = prefixes[str(carbon)] + "anal"
            if self.name == "Methanal":
                self.formula = "HCHO (or) CH2O"
                self.name = "Methanal (or) Formaldehyde"
            if self.name == "Ethanal":
                self.name = "Ethanal (or) Acetaldehyde"

    # Ketones
    class Ketone:
        def __init__(self, r1, r2):
            self.r1 = r1
            self.r2 = r2
            n = r1 + r2
            if r1 == r2:
                self.name = ("Di" + prefixes[str(r1)].lower() +
                    "yl" + " " + "Ketone")
                self.formula = (f"C{r1 if r1 != 1 else ""}H{(2 * r1) + 1}COC{r1 if r1 != 1 else ""}H{(2 * r1) + 1} "
                                f"(or) C{(2 * r1) + 1 }H{(4 * r1) + 2}O")
            else:
                self.name = (prefixes[str(r1)] + "yl " + prefixes[str(r2)]  +
                    "yl" + " " + "Ketone")
                self.formula = (f"C{r1 if r1 != 1 else ""}H{((2 * r1) + 1)}COC{r2}H{(2 * r2) + 1}"
                                f" (or) C{n + 1}H{(2 * n) + 2}O")
            if self.name == "Dimethyl Ketone":
                self.name = "Dimethyl Ketone (or) Acetone"

    # Esters
    class Ester:
        def __init__(self, alkylcarbons, carbon):
            self.carbons = carbon
            self.alkylcarbon = alkylcarbons
            carbons = alkylcarbons + carbon
            self.formula = (f"C{carbons if carbon > 1 else ""}H{2 * (carbons)}O2 "
                            f"(or) {"C" + str(carbon - 1) if carbon > 1 else "C" if carbon != 0 else ""}"
                            f"H{(2 * (carbon - 1)) + 1 if carbon != 1 else ""}COOC{alkylcarbons if alkylcarbons != 1 else ""}H{(2 * alkylcarbons) + 1}")
            self.name = prefixes[str(alkylcarbons)] + "yl " + prefixes[str(carbon + 1)] + "anoate"
            if self.name == "Methyl Methanoate":
                self.name = "Methyl Methanoate (or) Methyl Formate"

    # Amides
    class Amide:
        def __init__(self, carbon):
            self.carbons = carbon
            carbon -= 1
            self.formula = (f"{"C" + str(carbon) if carbon > 1 else "C" if carbon != 0 else ""}"
                            f"H{(2 * carbon) + 1 if carbon != 0 else ""}CONH2 "f"(or) C{carbon
                            + 1 if carbon != 0 else ""}H{(2 * carbon) + 3}NO")
            self.name = prefixes[str(carbon + 1)] + "anamide"
            if self.name == "Methanamide":
                self.name = "Methanamide (or) Formamide"
            if self.name == "Ethanamide":
                self.name = "Ethanamide (or) Acetamide"

    # Amines
    class Amine:
        def __init__(self, carbon):
            self.carbons = carbon
            self.formula = (f"{"C" + str(carbon) if carbon != 1 else "C"}H{(2 * carbon) + 1}NH2 "
                            f"(or) {"C" + str(carbon) if carbon != 1 else "C"}H{(2 * carbon) + 3}N")
            self.name = prefixes[str(carbon)] + "ylamine"

    # Arenes
    class Arene:
        def __init__(self, carbon):
            self.carbons = carbon
            self.formula = f"C{carbon + 6}H{(2 * carbon) + 6}"
            self.name = (f"Phenyl{OrganicCompound.Hydrocarbon.Alkane(carbon).name.lower()}"
                         f" (or) {OrganicCompound.Hydrocarbon.Alkane(carbon).name[:-3]}ylbenzene")

    class Thiol:
        def __init__(self, carbon):
            self.carbons = carbon
            self.name = prefixes[str(carbon)] + "anethiol"
            self.formula = (f"{"C" + str(carbon) if carbon > 1 else "C"}H{(2 * carbon) + 1}SH"
                            f" (or) {"C" + str(carbon) if carbon > 1 else "C"}H{(2 * carbon) + 2}S")

# Sample test runs
if __name__ == "__main__":

    # # Acids
    # print("The Acids:")
    # for form, values in anions.items():
    #     if "Bi" not in values[0]:
    #         name = values[0]
    #         print(Acid(name).name,
    #               Acid(name).formula)

    # Hydrocarbons
    print()
    print("The Hydrocarbons:")
    for carbons in range(1, 11):
        print(OrganicCompound.Hydrocarbon.Alkane(carbons).name,
              OrganicCompound.Hydrocarbon.Alkane(carbons).formula)
        if carbons > 1:
            print(OrganicCompound.Hydrocarbon.Alkene(carbons).name,
             OrganicCompound.Hydrocarbon.Alkene(carbons).formula)
            print(OrganicCompound.Hydrocarbon.Alkyne(carbons).name,
              OrganicCompound.Hydrocarbon.Alkyne(carbons).formula)

    # Alcohols
    print()
    print("The Alcohols: ")
    for carbons in range(1, 11):
        print(OrganicCompound.Alcohol(carbons).name,
              OrganicCompound.Alcohol(carbons).formula)

    # Ethers
    print()
    print("The Ethers: ")
    for carbons1 in range(1, 11):
        for carbons2 in range(1, 11):
            print(OrganicCompound.Ether(carbons1, carbons2).name,
                  OrganicCompound.Ether(carbons1, carbons2).formula)

    # Carboxylic Acids
    print()
    print("The Carboxylic Acids: ")
    for carbons in range(1, 10):
        print(OrganicCompound.CarboxylicAcid(carbons).name,
              OrganicCompound.CarboxylicAcid(carbons).formula)

    # Aldehydes
    print()
    print("The Aldehydes: ")
    for carbons in range(1, 11):
        print(OrganicCompound.Aldehyde(carbons).name,
             OrganicCompound.Aldehyde(carbons).formula)

    # Ketones
    print()
    print("The Ketones: ")
    for carbons1 in range(1, 11):
        for carbons2 in range(1, 11):
            print(OrganicCompound.Ketone(carbons1, carbons2).name,
                  OrganicCompound.Ketone(carbons1, carbons2).formula)

    # Esters
    print()
    print("The Esters: ")
    for j in range(0, 10):
        for i in range(1, 11):
            print(OrganicCompound.Ester(i, j).name,
                  OrganicCompound.Ester(i, j).formula)

    # Amides
    print()
    print("The Amides: ")
    for i in range(1, 11):
        print(OrganicCompound.Amide(i).name,
              OrganicCompound.Amide(i).formula)

    # Amines
    print()
    print("The Amines: ")
    for i in range(1, 11):
        print(OrganicCompound.Amine(i).name,
              OrganicCompound.Amine(i).formula)

    # Arenes
    print()
    print("The Arenes: ")
    for i in range(1, 11):
        print(OrganicCompound.Arene(i).name,
              OrganicCompound.Arene(i).formula)
