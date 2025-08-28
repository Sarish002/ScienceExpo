import NomialAnalysis
import FormulaicAnalysis

# Logic
while True:
    query = input("Query: ")
    for i in range(10):
        if str(i) in query:
            FormulaicAnalysis.FormulaicAnalysis(query)
            break
    else:
        NomialAnalysis.NomialAnalysis(query)
    print("---------------")

