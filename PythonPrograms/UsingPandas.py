import pandas as pd

def readExcel(rowname,colname):
    df = pd.read_excel("Data/Datasheet1.xlsx",sheet_name="DevopsUniv")
    val = df.loc[df['Label'] == rowname,colname].values[0]
    print(val)

readExcel("OrangeHRM","Password")