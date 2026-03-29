#Füge eine Tabelle der anderen hinzu

import pandas, csv

def combine(input_csv1, input_csv2):
    df1 = input_csv1
    df2 = input_csv2
    df3 = pandas.concat([df1, df2], ignore_index=True)
    csvf = df3.to_csv(index=False, quoting=csv.QUOTE_NONNUMERIC)
    return csvf