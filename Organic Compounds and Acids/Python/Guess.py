import FormulaicAnalysis as Formula
import NomialAnalysis as Name

def Guess(query):
    analysis = Formula.Analyze(query)
    results = []
    resulting_Comp = []
    for i in analysis:
        new_comp = [j if j != i else i - 1 if i != 0 else 0 for j in analysis]
        results.append(new_comp)
        new_comp = [j if j != i else i + 1 for j in analysis]
        results.append(new_comp)
    for i in results:
        resulting_Comp.append(Formula.FormulaicAnalysis(
            f"C{i[0]}H{i[1]}O{i[2]}N{i[3]}S{i[4]}"
        ))
    answerKey = []
    for i in resulting_Comp:
        if i is None:
            pass
        else:
            index = resulting_Comp.index(i)
            resulting_Comp[index] = list(i.split("is "))[1]
            resulting_Comp[index] = list(resulting_Comp[index].split("\n"))[0]
            n = query not in Name.NomialAnalysis(resulting_Comp[index])
            if resulting_Comp[index] not in answerKey and n:
                answerKey.append(resulting_Comp[index])
    return answerKey

Guess("C5H11CHO")