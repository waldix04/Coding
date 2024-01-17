def zahlen_pyramide(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

# Benutzereingabe für die Anzahl der Zeilen in der Pyramide
anzahl_zeilen = int(input("Geben Sie die Anzahl der Zeilen für die Pyramide ein: "))

# Funktion aufrufen, um die modifizierte Zahlenpyramide zu erstellen
zahlen_pyramide(anzahl_zeilen)

