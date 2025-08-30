import sys
import NomialAnalysis
import FormulaicAnalysis

# Logic
def Logic(query):
    if query == "Q":
        sys.exit()
    for i in range(10):
        if str(i) in query or query in ["HCHO", "HCOOH"]:
            return FormulaicAnalysis.FormulaicAnalysis(query)
            break
    else:
        return NomialAnalysis.NomialAnalysis(query)

if __name__ == "__main__":
    while True:
        query = input("Query (or) Quit (Q): ")
        print(Logic(query))
