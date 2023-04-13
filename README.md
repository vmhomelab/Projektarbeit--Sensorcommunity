# Overview
### Aufgabe: Daten eines Sensors von der Website www.sensorcommunity/de mit einem Python Skript downloaden, aufbereiten und grafisch darstellen.

Dieses Repository ist Teil der Projektarbeit, die wir im Fach Anwendungsentwicklung erhalten haben. Wir sollten uns einen Sensor auf der Website aussuchen, Dann sollten wir mithilfe eine Python Skripts die Daten des Sensors vom FTP-Server runterladen in einer Datenbank (in meinem Fall SQL speichern) und aufbereiten. Heißt Zeilen mit fehlenden Daten oder falschen Daten aussortieren und die übrig gebliebenen Daten aufbereiten (Durschnitte errechnen etc.).

Als Datenbank nutze ich SQL installiert auf einer VM mit WIndows Server 2022.

Nachdem alle Daten runtergeladen und aufbereitet wurden musste ein Skript geschrieben, womit die Daten aus der Datenbank ausgelesen und auf einer (G)UI dargestellt werden. Hier habe ich mich für django zum Erstellen der Website entschieden.

Für mehr Information zu django schaut hier vorbei: https://www.djangoproject.com/![SC_Home]

# Features

- [x] Stellt Temperatur und Feuchtigkeit in einem eigenen Graphen für das gesamte Jahr 2022 dar
- [x] Es kann für einzelne Monate die Temperatur und Luftfeuchtigkeit angezeigt werden

Upcoming

- [ ] Stellt Luftqualität in einem Graphen für das Jahr 2022 dar
- [ ] Es kann für einzelne Monate die Luftfeuchtigkeit angezeigt werden

# Screenshots
<details><summary>Hier klicken</summary>
<p>
  
![Screenshot von der Website](https://github.com/vmhomelab/Projektarbeit-Sensor-Community/blob/fab9385af8651706aa77419d0a7ff6def8ecc870/SC_Home.PNG)

  </p>
</details>