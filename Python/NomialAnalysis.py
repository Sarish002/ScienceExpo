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
while True:
    query = input("Query: ")
    if query.endswith("ane") and not query.startswith("Phenyl"):
        for i, j in prefixes.items():
            if j == query[:-3]:
                num = int(i)
        if query not in descriptions["Hydrocarbons"]:
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Hydrocarbon.Alkane(num).formula}"
            )
        else:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Hydrocarbons"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Hydrocarbons"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Hydrocarbons"][query]["Uses"]):
                print(f"-> {i}")
    elif query.endswith("ene") and not query.endswith("benzene") and not query == "Benzene" and not query == f"Toluene":
        for i, j in prefixes.items():
            if j == query[:-3]:
                num = int(i)
        print(f"The Chemical Formula for {query} is "
            f"{Classes.OrganicCompound.Hydrocarbon.Alkene(num).formula}"
        )
    elif query.endswith("yne"):
        for i, j in prefixes.items():
            if j == query[:-3]:
                num = int(i)
        print(f"The Chemical Formula for {query} is "
            f"{Classes.OrganicCompound.Hydrocarbon.Alkyne(num).formula}"
        )
    elif query.endswith("benzene") or query in ["Benzene", f"Toluene"]:
        for i, j in prefixes.items():
            if j == query[:-9]:
                num = int(i)
        if query not in descriptions["Arenes"]:
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Arene(num).formula}"
            )
        else:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Arenes"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Arenes"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Arenes"][query]["Uses"]):
                print(f"-> {i}")
    elif query.startswith("Phenyl"):
        for i, j in prefixes.items():
            if j.lower() == query[6:-3]:
                num = int(i)
        print(f"The Chemical Formula for {query} is "
            f"{Classes.OrganicCompound.Arene(num).formula}"
        )
    elif query.endswith("ylamine") or query in descriptions["Amines"]:
        for i, j in prefixes.items():
            if j == query[:-7]:
                num = int(i)
        if query not in descriptions["Amines"]:
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Amine(num).formula}"
            )
        else:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Amines"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Amines"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Amines"][query]["Uses"]):
                print(f"-> {i}")
    elif query.endswith("anamide") or query in descriptions["Amides"]:
        for i, j in prefixes.items():
            if j == query[:-7]:
                num = int(i)
        if query not in descriptions["Amides"]:
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Amide(num).formula}"
            )
        else:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Amides"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Amides"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Amides"][query]["Uses"]):
                print(f"-> {i}")
    elif query.endswith("ol") or query in exceptions["Alcohols"] or query in descriptions["Alcohols"]:
        for i, j in prefixes.items():
            if j == query[:-4]:
                num = int(i)
        if query not in descriptions["Alcohols"] and query not in exceptions["Alcohols"]:
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Alcohol(num).formula}"
            )
        elif query in descriptions["Alcohols"]:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Alcohols"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Alcohols"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Alcohols"][query]["Uses"]):
                print(f"-> {i}")
        else:
            print(f"The Chemical Formula for {query} is"
                  f"{exceptions["Alcohols"][query]}"
                  )
    elif query.endswith("anal") or query in exceptions["Aldehydes"] or query in descriptions["Aldehydes"]:
        for i, j in prefixes.items():
            if j == query[:-4]:
                num = int(i)
        if query not in descriptions["Aldehydes"] and query not in exceptions["Aldehydes"]:
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Aldehyde(num).formula}"
            )
        elif query in descriptions["Aldehydes"]:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Aldehydes"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Aldehydes"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Aldehydes"][query]["Uses"]):
                print(f"-> {i}")
        else:
            print(f"The Chemical Formula for {query} is "
                  f"{exceptions["Aldehydes"][query]}"
                  )
    elif query.endswith("Acid") or query in exceptions["Acids"] or query in descriptions["Acids"]:
        for i, j in prefixes.items():
            if j == query[:-10]:
                num = int(i)
        if query not in descriptions["Acids"] and query not in exceptions["Acids"]:
            if query.endswith("oic Acid"):
                print(f"The Chemical Formula for {query} is "
                      f"{Classes.OrganicCompound.CarboxylicAcid(num).formula}"
                      )
            if "ulfur" in query.lower():  # Exception
                query = query.replace("ulfur", "ulf")
            if "hosphor" in query.lower():  # Exception
                query = query.replace("hosphor", "hosph")
            if query == "Hydrocyanic Acid":
                print(f"The Chemical Formula for {query} is HCN")
            elif query.endswith("ic Acid") and query.startswith("Hydro"):
                print(f"The Chemical Formula for {query} is " + Classes.Acid(query[5:-7].capitalize() + "ide").formula)
            elif query.endswith("ic Acid") and not query[:-8] != "o":
                print(f"The Chemical Formula for {query} is " + Classes.Acid(query[:-7].capitalize() + "ate").formula)
            elif query.endswith("ous Acid"):
                print(f"The Chemical Formula for {query} is " + Classes.Acid(query[:-8].capitalize() + "ite").formula)
        elif query in descriptions["Acids"]:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Acids"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Acids"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Acids"][query]["Uses"]):
                print(f"-> {i}")
        else:
            print(f"The Chemical Formula for {query} is "
                  f"{exceptions["Acids"][query]}"
                  )

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
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Ether(num1, num2).formula}"
            )
        else:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Ethers"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Ethers"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Ethers"][query]["Uses"]):
                print(f"-> {i}")

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
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Ketone(num1, num2).formula}"
            )
        else:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Ketones"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Ketones"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Ketones"][query]["Uses"]):
                print(f"-> {i}")

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
            print(f"The Chemical Formula for {query} is "
                f"{Classes.OrganicCompound.Ester(num1, num2).formula}"
            )
        elif query not in exceptions["Esters"] and query in descriptions["Esters"]:
            print(f"The Chemical Formula for {query} is ", end="")
            print(descriptions["Esters"][query]["Symbol"])
            print("Description: ")
            for i in (descriptions["Esters"][query]["Description"]):
                print(f"-> {i}")
            print("Uses: ")
            for i in (descriptions["Esters"][query]["Uses"]):
                print(f"-> {i}")

        else:
            print(f"The Chemical Formula for {query} is {exceptions["Esters"][query]}")
    print("------------------------------------------------------------------------------------")
