import sys
import NomialAnalysis
import FormulaicAnalysis

# Logic
def Logic(query):
    if query == "Q":
        sys.exit()
    try:
        for i in range(10):
            if str(i) in query or query in ["HCHO", "HCOOH"]:
                return FormulaicAnalysis.FormulaicAnalysis(query.upper())
                break
        else:
            return NomialAnalysis.NomialAnalysis(query.title())
    except:
        return "Couldn't find an answer."
def Similar(query):
    if query == "Q":
        sys.exit()
    try:
        for i in range(10):
            if str(i) in query or query in ["HCHO", "HCOOH"]:
                return FormulaicAnalysis.Analyze(query)
                break
        else:
            return ""
    except:
        return "Couldn't find an answer."

if __name__ == "__main__":
    while True:
        query = input("Query (or) Quit (Q): ")
        print(Logic(query))