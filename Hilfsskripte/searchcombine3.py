#Entferne die Inhalte einer Tabelle aus der anderen

import pandas, csv

def main():
    input_csv1 = open ('./EDCS-Tabellen/searchresultSepulcrales.csv', "r", encoding='utf-8', newline = '')
    input_csv2 = open ('./EDCS-Tabellen/searchresultSepulcralesMinus.csv', "r", encoding='utf-8', newline = '')
    df1 = pandas.read_csv(input_csv1, low_memory=False, dtype=str)
    df2 = pandas.read_csv(input_csv2, low_memory=False, dtype=str)
    df3 = df1[~df1.ID.isin(df2.ID)]
    csvf = df3.to_csv(index=False, quoting=csv.QUOTE_NONNUMERIC)
    outfile = open("./EDCS-Tabellen/searchresultSepulcralesReduziert.csv", "w", encoding='utf-8', newline='')
    outfile.write(csvf)
    outfile.close()

if __name__ == "__main__":
    main()