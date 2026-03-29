import pandas

input_csv1 = open ('./EDCS-Tabellen/searchresult.csv', "r", encoding='utf-8', newline = '')
input_csv2 = open ('./EDCS-Tabellen/searchresultSepulcralesReduziert.csv', "r", encoding='utf-8', newline = '')
input_csv3 = open ('./EDCS-Tabellen/searchresultWeitere.csv', "r", encoding='utf-8', newline = '')
alt = pandas.read_csv(input_csv1, low_memory=False, dtype=str)
neu1 = pandas.read_csv(input_csv2, low_memory=False, dtype=str)
neu2 = pandas.read_csv(input_csv3, low_memory=False, dtype=str)
neu3 = pandas.concat([neu1, neu2], ignore_index = True)
ueberlappung = neu1[neu1.ID.isin(alt.ID)]
print(ueberlappung)