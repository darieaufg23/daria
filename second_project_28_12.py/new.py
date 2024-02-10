from time import sleep

# Geschwindigkeit in km/h
geschwindigkeit = 78

# Informative Ausgabe über den Zweck des Programms
print("Dieses Programm hilft Ihnen dabei Wegberechnungen automatisiert durchzuführen")

# Berechnung des Reaktionswegs (Annahme: Reaktionszeit ist 3 Sekunden)
reaktionsweg = (geschwindigkeit / 10) * 3

# Berechnung des Bremswegs
bremsweg = (geschwindigkeit / 10) * (geschwindigkeit / 10)

# Berechnung des Anhaltewegs (Summe von Reaktionsweg und Bremsweg)
anhalteweg = reaktionsweg + bremsweg

# Verzögerung der Ausgabe für bessere Lesbarkeit
sleep(1)

# Ausgabe des Reaktionswegs
print("Der Reaktionsweg beträgt ", reaktionsweg, "Meter")

# Verzögerung dprint("Der Bremsweg beträgt ", bremsweg, "Meter")

# Verzögerung der Ausgabe
sleep(1)

# Ausgabe des Anhaltewegs
print("Der Anhalteweg beträgt ", anhalteweg, "Meter")
