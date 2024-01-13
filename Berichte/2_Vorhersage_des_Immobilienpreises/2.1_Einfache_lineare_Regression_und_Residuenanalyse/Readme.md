## 2.1 Einfache lineare Regression und Residuenanalyse

Verwende ein einfaches lineares Modell zur Vorhersage von `price_cleaned` mit dem Attribut `Space extracted` oder `Floor_space_merged` (es gibt einige, wo beide fehlen (um die 800, können ignoriert werden).

Entwickle das Modell in einem Notebook. Untersuche dabei ob die Annahmen eines linearen Modells erfüllt sind mit geeigneten Darstellungen. Wie können Variablen-Transformationen verwendet werden, um die Modellvoraussetzungen besser zu erfüllen und das Modell zu verbessern?

Rapportiere und diskutiere die erreichte Genauigkeit der Vorhersage mit mehreren sinnvollen Metriken und auf unabhängigen Testdaten.

Abgabe

Notebook und daraus erstellter Bericht (ohne Code) als pdf.

- `2_1_Lineare_Regression.ipynb`: In diesem Notebook haben wir die Grundlagen unseres Projekts durch die Erstellung und Analyse einfacher linearer Regressionsmodelle gelegt. Unser Fokus lag darauf, die Immobilienpreise mit einer einzelnen Variablen vorherzusagen. Um das Potenzial dieser Methode voll auszuschöpfen, führten wir eine Reihe von Experimenten durch, darunter Variablentransformationen, das Ersetzen fehlender Werte, die Generierung neuer Features sowie das Handling von Ausreissern mittels Z-Scores und des Interquartilsabstands (IQR). Diese Bemühungen dienten dem Ziel, das bestmögliche einfache lineare Regressionsmodell zu entwickeln. Es wurde jedoch rasch deutlich, dass ein solch einfacher Ansatz für die präzise Vorhersage von Immobilienpreisen nicht ausreichend war. Diese Erkenntnis leitete uns zur nächsten Phase unseres Projekts, der Aufgabe 2.2: [Bestmögliches Regressionsmodell](https://github.com/alexschillingfhnw/cml1/tree/main/Berichte/2_Vorhersage_des_Immobilienpreises/2.2_Bestm%C3%B6gliches_Regressionsmodell_kaggle_Contest), in der wir uns auf komplexere Modellierungsansätze konzentrierten.
