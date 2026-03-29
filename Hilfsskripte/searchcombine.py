#Fügt Elemente aus zweiter Suchtabelle hinzu, die kein Datum enthalten
import csv, pandas as pd

def append_empty_date_rows(input_csv1, input_csv2):
        df1 = pd.read_csv(input_csv1, low_memory=False, dtype=str)
        df2 = pd.read_csv(input_csv2, low_memory=False, dtype=str)
        for index, row in df2.iterrows():
            if (pd.isna(row["Datum von"])) & (pd.isna(row["Datum bis"])):
                df1 = pd.concat([df1, pd.DataFrame([row])], ignore_index=True)
        csvf = df1.to_csv(index=False, quoting=csv.QUOTE_NONNUMERIC)
        outfile = open("./EDCS-Tabellen/searchresultt.csv", "w", encoding='utf-8', newline='')
        outfile.write(csvf)
        outfile.close()
def main():
    input_csv1 = open ('./EDCS-Tabellen/searchresult.csv', "r", encoding='utf-8', newline = '')
    input_csv2 = open ('./EDCS-Tabellen/searchresultb.csv', "r", encoding='utf-8', newline = '')
    append_empty_date_rows(input_csv1, input_csv2)

if __name__ == "__main__":
    main()