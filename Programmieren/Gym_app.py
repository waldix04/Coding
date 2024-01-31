# Die gewichtscheiben sollen berechnet werden um auf ein gezieltes Übungsgewciht zu kommen. 
# Beispiel: 100 KG soll in verschiedenen arten in [25,20,15,10,5,2.5,1.25] aufgeteilt werden. 
# 1. Möglichkeit: 4*25 , 2. Möglichkeit: 2*25,2*20,2*10
# Wichtig: Da viele maschienen mit zwei seiten ausgerüstet sind muss auch gleichmäßig verteilt werden

#Gewicht = float(input("Geben Sie Ihr wunsch Gewicht ein"))
#Scheiben = (25,20,15,10,5,2.25,1.25)

def kombiniere_gewichte(verfuegbare_gewichte, wunschgewicht):
    verfuegbarer_gewichts_stack = []  # Stapelspeicher für die verfügbaren Gewichte
    aktuelles_gewicht = 0
    kombination = []

    verfuegbare_gewichte.sort(reverse=True)

    while verfuegbare_gewichte or verfuegbarer_gewichts_stack:
        if verfuegbare_gewichte and aktuelles_gewicht + verfuegbare_gewichte[0] <= wunschgewicht:
            gewicht = verfuegbare_gewichte[0]
            verfuegbarer_gewichts_stack.append(gewicht)
            aktuelles_gewicht += gewicht
        elif verfuegbarer_gewichts_stack:
            gewicht = verfuegbarer_gewichts_stack.pop()
            aktuelles_gewicht -= gewicht
        else:
            break

        if aktuelles_gewicht == wunschgewicht and all(verfuegbarer_gewichts_stack.count(gewicht) % 2 == 0 for gewicht in verfuegbarer_gewichts_stack):
            kombination = list(verfuegbarer_gewichts_stack)
            break

    return kombination

# Beispielaufruf
verfuegbare_gewichte = [20, 15, 10, 5, 2.5]  # Hier die verfügbaren Gewichtsplatten angeben
wunschgewicht = 100

ergebnis = kombiniere_gewichte(verfuegbare_gewichte, wunschgewicht)

if ergebnis:
    print(f"Kombination gefunden: {ergebnis}")
else:
    print("Keine passende Kombination gefunden.")

