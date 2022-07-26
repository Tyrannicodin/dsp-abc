from math import ceil
from csv import reader
from formulas import Parser
from formulas.errors import FormulaError

def pm(matrix):
    #Prints a 2d list nicely
    #https://stackoverflow.com/a/13214945
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return '\n'.join(table)

class resources:
    """Parse the resources given by a csv file
    """    
    CSV_CONVERT = { #Convert between the calculator and numerical ids 
    }

    def __init__(self, file:str):
        """Args:
            file (str): The file to read the data from
        """        
        with open(file, "r") as f:
            lines = f.readlines() #Get the data
        self.filename = file.split("\\")[-1] #For later use when saving
        self.parser = Parser() #Avoid creating lots of objects, this parses the formulas given in the csv file
        self.link = lines.pop(0).rstrip("\n") #This is the link to the resource calculator page
        self.data = [] #Setup list
        lines = reader(lines) #Parses csv data
        for l in lines:
            row = []
            for arg in l:
                try: #Attempt to parse formula, if unable to it will stay unchanged
                    arg = self.parser.ast(arg)[1].compile()()
                except FormulaError:
                    pass
                row.append(arg)
            self.data.append(row)
        del self.parser #No longer needed

    def save(self, path:str):
        """Save the parsed data to a file

        Args:
            path (str): The path the data will be saved at
        """        
        with open(path, "w") as f:
            f.write(pm(self.data))