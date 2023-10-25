# 2. Vorhersage des Immobilienpreises (1/2)

Ziel dieser Teilaufgabe ist die Vorhersage des Preises (Attribut `PurchasePrice`).

Die Aufgabenstellung ist zwei Teilschritte gegliedert, die Verständnisgewinn und erfolgreiches Lösen der Aufgabenstellung unterstützen sollen:

## 2.1 Einfache lineare Regression und Residuenanalyse

Verwende ein einfaches lineares Modell zur Vorhersage von `price_cleaned` mit dem Attribut `Space extracted` oder `Floor_space_merged` (es gibt einige, wo beide fehlen (um die 800, können ignoriert werden).

Entwickle das Modell in einem Notebook. Untersuche dabei ob die Annahmen eines linearen Modells erfüllt sind mit geeigneten Darstellungen. Wie können Variablen-Transformationen verwendet werden, um die Modellvoraussetzungen besser zu erfüllen und das Modell zu verbessern?

Rapportiere und diskutiere die erreichte Genauigkeit der Vorhersage mit mehreren sinnvollen Metriken und auf unabhängigen Testdaten.

Abgabe

Notebook und daraus erstellter Bericht (ohne Code) als pdf.

## 2.2 Bestmögliches Regressionsmodell - kaggle-Contest

Entwickle mit beliebigen Algorithmen das bestmögliche Modell im Sinne des Mean absolute percentage error (MAPE). Vergleiche dabei mindestens drei algorithmische Ansätze, wobei ein multiples lineares Modell Teil davon sein soll als Benchmark. Untersuche die ‘Variable Importance’ für dein bestes Modell.

Abgabe

Notebook und daraus erstellter Bericht (ohne Code) als pdf, welche die Entwicklung deines besten Modells, sowie der zwei weiteren Modelle dokumentiert, inklusive verwendeter Features, Preprocessing, Model Selection Prozess und Untersuchung der ‘Variable Importance’.

Eingabe der Vorhersage des Preises für den Testdatensatz mit deinem bestmöglichen Modell auf kaggle.

## 2.3 Webservice

Erstelle einen Web-Service mit einem Modell, welche via http-Request angefragt werden kann und für ein bestimmtes Objekt eine Preis-Vorhersage zurückgibt. Da einige Feature für normale User unbekannt sind, habt ihr zwei Möglichkeiten:

Ihr verwendet euer bestes Modell und nehmt an, dass der Service von Experten benutzt wird, welche diese Werte kennen.

Ihr verwendet ein simpleres Modell, welches ausschliesslich Features braucht, die ein normaler Käufer zur Verfügung hat. Z.b., Wohnfläche, Kanton, ...

Abgabe

Skript, welches den Web-Service startet und eine kurze Anleitung, wie dieser zu verwenden ist.

