from datetime import datetime
from os import path

def isTime(string:str) -> bool:

    try:
        datetime.strptime(string, "%H:%M:%S")
        return True
    except:
        pass
        #print(f"'{string}' is not a valid H:M:S")

    try:
        datetime.strptime(string, "%M:%S")
        return True
    except:
        return False
        #print(f"{string} is not a valid M:S")



def main():

    scriptDir = path.dirname(path.abspath(__file__))
    newFile = ''

    try:
        with open(scriptDir + "\original.txt", "r", encoding="utf-8") as original:
            for x in original:
                
                y = x.rstrip()
                if isTime(y):
                    continue
                else:
                    newFile += y + ' '
    except:
        print("""\nplease have an "original.txt"\n""")


    print(scriptDir + "\\original.txt\n")

    try:
        with open(scriptDir + "\\cleaned.txt", "w", encoding="utf-8") as new:
            new.write(newFile)
        print("Done", end='')

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    input()