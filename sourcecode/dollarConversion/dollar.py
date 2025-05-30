import sys
import requests

class App():
    def __init__(self):
        self.apiUrl = "https://mx.dolarapi.com/v1/cotizaciones/usd"
        self.argumentCount = len(sys.argv)
        self.exitCode3 = False
        self.exitCode4 = False

    def convert(self, mxnvalue):
        try:
            mxnvalue = float(mxnvalue)
        except:
            print(" ")
            print("Usage: dollar [value]")
            print("     [value]: float (required)")
            print("     The USD dollar value to convert to MXN")
            print("""

Developed by minaroblox, creator of
CLI-Engine, also installable with brew.

""")
            print("Argument entered wasn't a number!")
            print("Error Code: 3")
            return "Error Code: 3"
            
        response = requests.get(self.apiUrl)
        
        if response.status_code == 200:
            data = response.json()
            dollarvalue = float(data["compra"])
            newvalue = dollarvalue * mxnvalue
            return newvalue

        else:
            print(f"Failed to fetch data: {response.status_code}")
            print("Please report this to https://mx.dolarapi.com/")
            print(f"In case, this is the requests url: {self.apiUrl}")
            print("Error Code: 4")
            return "Error Code: 4"
        
    def main(self):
        # First check.
        if self.argumentCount == 1:
            print(" ")
            print("Usage: dollar [value]")
            print("     [value]: float (required)")
            print("     The USD dollar value to convert to MXN")
            print("""

Developed by minaroblox, creator of
shellAI, also installable with brew.

""")
            print("Not enough arguments!")
            print("You cannot convert dollar to MXN without a dollar value!")
            print("Error Code: 1")
            pass
        elif self.argumentCount > 2:
            print(" ")
            print("Usage: dollar [value]")
            print("     [value]: float (required)")
            print("     The USD dollar value to convert to MXN")
            print("""

Developed by minaroblox, creator of
CLI-Engine, also installable with brew.

""")
            print("Too much arguments!")
            print("You only need 1 argument!")
            print("Error Code: 2")
            pass
        else:
            # Argument check.

            dollarArgument = sys.argv[1]
            if dollarArgument == "--help":
                print(" ")
                print("Usage: dollar [value]")
                print("     [value]: float (required)")
                print("     The USD dollar value to convert to MXN")
                print("""

Developed by minaroblox, creator of
CLI-Engine, also installable with brew.

""")
            else:
                valueGiven = self.convert(dollarArgument)
                if valueGiven == "Error Code: 3":
                    self.exitCode3 = True
                    
                elif valueGiven == "Error Code: 4":
                    self.exitCode4 = True
                
                if self.exitCode4 == True or self.exitCode3 == True:
                    pass
                else:
                    # Convert
                    print(f"Value given: ${dollarArgument} USD")
                    print(f"Translated value: ${valueGiven} MXN")


if __name__ == "__main__":
    app = App()
    app.main()
