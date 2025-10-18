import sys
import json
import Classes

# Reading the source files
with open("../JSON/OrganicPrefixes.json", 'r') as file:
    prefixes = json.load(file)

with open("../JSON/OrganicDescriptions.json", 'r') as file:
    descriptions = json.load(file)
with open("../JSON/OrganicExceptions.json", 'r') as file:
    exceptions = json.load(file)

def NomialAnalysis(query):

    # Alkanes
    if query.endswith("ane") and not query.startswith("Phenyl"):
        for i, j in prefixes.items():
            if j == query[:-3]:
                num = int(i)
        if query not in descriptions["Hydrocarbons"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Hydrocarbon.Alkane(num).formula}"
            )
        else:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Hydrocarbons"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Hydrocarbons"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Hydrocarbons"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)

    # Alkenes
    elif query.endswith("ene") and not query.endswith("benzene") and not query == "Benzene" and not query == f"Toluene":
        for i, j in prefixes.items():
            if j == query[:-3]:
                num = int(i)
        return (f"The Chemical Formula for {query} is "
            f"{Classes.OrganicCompound.Hydrocarbon.Alkene(num).formula}"
        )

    # Alkynes
    elif query.endswith("yne"):
        for i, j in prefixes.items():
            if j == query[:-3]:
                num = int(i)
        return (f"The Chemical Formula for {query} is "
            f"{Classes.OrganicCompound.Hydrocarbon.Alkyne(num).formula}"
        )

    # Arenes (Benzene)
    elif query.endswith("benzene") or query in ["Benzene", f"Toluene"]:
        for i, j in prefixes.items():
            if j == query[:-9]:
                num = int(i)
        if query not in descriptions["Arenes"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Arene(num).formula}"
            )
        else:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Arenes"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Arenes"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Arenes"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)

    # Arenes (Phenyl)
    elif query.startswith("Phenyl"):
        for i, j in prefixes.items():
            if j.lower() == query[6:-3]:
                num = int(i)
        return (f"The Chemical Formula for {query} is "
            f"{Classes.OrganicCompound.Arene(num).formula}"
        )

    # Amines
    elif query.endswith("ylamine") or query in descriptions["Amines"]:
        for i, j in prefixes.items():
            if j == query[:-7]:
                num = int(i)
        if query not in descriptions["Amines"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Amine(num).formula}"
            )
        else:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Amines"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Amines"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Amines"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)

    # Amides
    elif query.endswith("anamide") or query in descriptions["Amides"]:
        for i, j in prefixes.items():
            if j == query[:-7]:
                num = int(i)
        if query not in descriptions["Amides"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Amide(num).formula}"
            )
        else:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Amides"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Amides"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Amides"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)

    # Alcohols
    elif query.endswith("anol") or query in exceptions["Alcohols"] or query in descriptions["Alcohols"]:
        for i, j in prefixes.items():
            if j == query[:-4]:
                num = int(i)
        if query not in descriptions["Alcohols"] and query not in exceptions["Alcohols"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Alcohol(num).formula}"
            )
        elif query in descriptions["Alcohols"]:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Alcohols"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Alcohols"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Alcohols"][query]["Uses"]):
                formula += (f"> {i}\n")
            print(formula)
            return "".join(formula)
        else:
            return (f"The Chemical Formula for {query} is "
                  f"{exceptions["Alcohols"][query]}"
                  )

    # Aldehydes
    elif query.endswith("anal") or query in exceptions["Aldehydes"] or query in descriptions["Aldehydes"]:
        for i, j in prefixes.items():
            if j == query[:-4]:
                num = int(i)
        if query not in descriptions["Aldehydes"] and query not in exceptions["Aldehydes"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Aldehyde(num).formula}"
            )
        elif query in descriptions["Aldehydes"]:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Aldehydes"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Aldehydes"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Aldehydes"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)
        else:
            return (f"The Chemical Formula for {query} is "
                  f"{exceptions["Aldehydes"][query]}"
                  )

    # Carboxylic Acids / Mineral Acids
    elif query.endswith("Acid") or query in exceptions["Acids"] or query in descriptions["Acids"]:
        for i, j in prefixes.items():
            if j == query[:-10]:
                num = int(i)
        if query not in descriptions["Acids"] and query not in exceptions["Acids"]:
            if query.endswith("oic Acid"):
                return (f"The Chemical Formula for {query} is "
                      f"{Classes.OrganicCompound.CarboxylicAcid(num).formula}"
                      )
        elif query in descriptions["Acids"]:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Acids"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Acids"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Acids"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)
        else:
            return (f"The Chemical Formula for {query} is "
                  f"{exceptions["Acids"][query]}"
                  )

    # Ethers
    if query.endswith("Ether"):
        prefixez = list(query.split("yl "))[:-1]
        for i, j in prefixes.items():
            if not query.startswith("Di"):
                if j == prefixez[0]:
                    num1 = int(i)
                elif j == prefixez[1]:
                    num2 = int(i)
            if query.startswith("Di"):
                if j == prefixez[0][2:].capitalize():
                    num1 = int(i)
                    num2 = int(i)
        if query not in descriptions["Ethers"]:
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Ether(num1, num2).formula}"
            )
        else:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Ethers"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Ethers"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Ethers"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)

    # Ketones
    if query.endswith("Ketone") or query.endswith("one"):
        if query not in descriptions["Ketones"]:
            prefixez = list(query.split("yl "))[:-1]
            for i, j in prefixes.items():
                if not query.startswith("Di"):
                    if j == prefixez[0]:
                        num1 = int(i)
                    elif j == prefixez[1]:
                        num2 = int(i)
                if query.startswith("Di"):
                    if j == prefixez[0][2:].capitalize():
                        num1 = int(i)
                        num2 = int(i)
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Ketone(num1, num2).formula}"
            )
        else:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Ketones"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Ketones"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Ketones"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)

    # Esters
    if (query.endswith("anoate") or query in descriptions["Esters"] or
            query in exceptions["Esters"]):
        if query not in descriptions["Esters"] and query not in exceptions["Esters"]:
            prefixez = list(query.split("yl "))
            for i, j in prefixes.items():
                if not query.startswith("Di"):
                    if j == prefixez[1][:-6].capitalize():
                        num2 = int(i)
                    elif j == prefixez[0]:
                        num1 = int(i)
                if query.startswith("Di"):
                    if j == prefixez[0][:-6].capitalize():
                        num1 = int(i)
                        num2 = int(i)
            return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Ester(num1, num2).formula}"
            )
        elif query not in exceptions["Esters"] and query in descriptions["Esters"]:
            formula = (f"The Chemical Formula for {query} is ")
            formula += (descriptions["Esters"][query]["Symbol"])
            formula += "\n"
            formula += ("Description: " + "\n")
            for i in (descriptions["Esters"][query]["Description"]):
                formula += (f"> {i}\n")
            formula += "\n"
            formula += ("Uses: " + "\n")
            for i in (descriptions["Esters"][query]["Uses"]):
                formula += (f"> {i}\n")
            return "".join(formula)
        else:
            return (f"The Chemical Formula for {query} is {exceptions["Esters"][query]}")
    if query.endswith("anethiol"):
        for i, j in prefixes.items():
            if j == query[:-8]:
                num = int(i)
        return (f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Thiol(num).formula}"
            )

    return ("Couldn't find an answer.")

if __name__ == "__main__":
    while True:
        query = input("Query (or) Quit (Q): ")
        if not query == "Q":
            print(NomialAnalysis(query))
        else:
            sys.exit()
        print("--------------------------")