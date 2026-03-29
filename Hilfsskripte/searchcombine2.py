#Fügt Elemente aus zweiter Suchtabelle hinzu, die kein Datum enthalten

import pandas as pd
import numpy as np


def append_rows_with_empty_dates(source_csv, target_csv, output_csv):
        # Lade die CSV-Dateien in DataFrames
        df_source = pd.read_csv(source_csv, dtype=str)
        df_target = pd.read_csv(target_csv, dtype=str)

        # Filtere die Zeilen aus der Quelldatei, in denen "Datum von" und "Datum bis" leer sind
        empty_dates_rows = df_target[(df_target['Datum von'].isna()) & (df_target['Datum bis'].isna())]

        # Hänge die gefilterten Zeilen an die Zieldatei an
        df_combined = pd.concat([df_source, empty_dates_rows], ignore_index=True)

        # Speichere das kombinierte DataFrame in eine neue CSV-Datei
        df_combined.to_csv(output_csv, index=False, quoting=1)
def main():
    # Beispielaufruf der Funktion
    source_csv = './EDCS-Tabellen/searchresult.csv'  # Pfad zur Quelldatei
    target_csv = './EDCS-Tabellen/searchresultb.csv'    # Pfad zur Zieldatei
    output_csv = './EDCS-Tabellen/searchresult.csv'  # Pfad zur Ausgabedatei

    append_rows_with_empty_dates(source_csv, target_csv, output_csv)
    dft = pd.DataFrame([(0), (7), (np.nan), (8)])
    dft2 = dft[[True, False, True, True]]
    print (dft2)

if __name__ == "__main__":
    main()