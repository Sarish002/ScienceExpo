import re # NEW!
import sys
import json
import Classes
with open("../JSON/OrganicPrefixes.json", 'r') as file:
    prefixes = json.load(file)
with open("../JSON/Anions.json", 'r') as file:
    anions = json.load(file)
with open("../JSON/OrganicDesciptions.json", 'r') as file:
    descriptions = json.load(file)
with open("../JSON/OrganicExceptions.json", 'r') as file:
    exceptions = json.load(file)
with open("../OrganicRatios.txt", 'r') as file:
    rules = file.read()

def Analyze(query):

    # Logic
    atomsRE = re.findall(r"[A-Z][a-z]|[A-Z]", query)
                        # REGEX (NEW!)
    atomSymList = list(atomsRE)
    atomsRE = re.findall(r"\d+|(?<=[A-Z])", query)
                        # REGEX (NEW!)
    atomNumList = list(atomsRE)
    atomNumList = [1 if i == "" else int(i) for i in atomNumList]
    mols = [0, 0, 0, 0]
    molTList = ["C", "H", "O", "N"]
    for i, j in enumerate(atomNumList):
        eleIndex = molTList.index(atomSymList[i])
        mols[eleIndex] += j
    return mols

def FormulaicAnalysis(query):

    mols = Analyze(query)
    C = mols[0];    H = mols[1]
    O = mols[2];    N = mols[3]

    # Descriptions
    for i1, j1 in descriptions.items():
        for i2, j2 in j1.items():
                if Analyze(query) == Analyze(j2["Symbol"]):
                    print(f"The Chemical Name for {query} is", i2)
                    print("Description: ")
                    for i in j2["Description"]:
                        print("->  ", i)
                    print("Uses: ")
                    for i in j2["Uses"]:
                        print("->  ", i)
                    return

    # Exceptions
    for i1, j1 in exceptions.items():
        for i2, j2 in j1.items():
            if Analyze(query) == Analyze(j2):
                print(f"The Chemical Name for {query} is", i2)
                return

    # Logic
    if (H == (2 * C) + 2) and O == 0: 
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Hydrocarbon.Alkane(C).name)
    if (H == 2 * C) and O == 0:
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Hydrocarbon.Alkene(C).name)
    if (H == (2 * C) - 2) and O == 0:
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Hydrocarbon.Alkyne(C).name)
    if (H == (2 * C) + 2) and O == 1:
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Alcohol(C).name)
    if H == O * C:
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.CarboxylicAcid(C).name)
    if (H == 2 * C and O == 1):
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Aldehyde(C).name)
    if (H == (2 * C) + 1) and O == N == 1:
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Amide(C).name)
    if (H == (2 * C) + 3):
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Amine(C).name)
    if (C - 6 == (H - 6) / 2) and O == 0:
        print(f"The Chemical Name for {query} is", Classes.OrganicCompound.Arene(C - 6).name)
    
if __name__ == "__main__":
    while True:
        query = input("Query (or) Quit (Q): ")
        if not query == "Q":
            FormulaicAnalysis(query)
        else:
            sys.exit()
        print("--------------------------")

