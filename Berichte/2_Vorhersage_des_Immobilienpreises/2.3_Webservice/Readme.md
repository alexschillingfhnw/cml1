## 2.3 Webservice

Erstelle einen Web-Service mit einem Modell, welche via http-Request angefragt werden kann und für ein bestimmtes Objekt eine Preis-Vorhersage zurückgibt. Da einige Feature für normale User unbekannt sind, habt ihr zwei Möglichkeiten:

Ihr verwendet euer bestes Modell und nehmt an, dass der Service von Experten benutzt wird, welche diese Werte kennen.

Ihr verwendet ein simpleres Modell, welches ausschliesslich Features braucht, die ein normaler Käufer zur Verfügung hat. Z.b., Wohnfläche, Kanton, ...

Abgabe

Skript, welches den Web-Service startet und eine kurze Anleitung, wie dieser zu verwenden ist.


### App Beschreibung

- `home.py`: Diese Datei bildet die "Mainpage" des Streamlit Apps. Es ist in der Lage die weiteren Dateien in subfolder `./pages` zu erkennen und als Unterseiten, bzw. in der Navigation als Navigationspunkte aufzulisten. <br>
Die Homeseite, gibt einen kurzen einblick um was es geht, und welcher Menüpunkt für welche Zielgruppe gedacht ist.<br>
Die App kann gestartet werden, in dem man mit dem Terminal in den Ordner von home.py wechselt (oder den kompletten pfad beim aufrufen angibt) und dann streamlit run ./home.py ausführt.

- `simple_regression.py`: Diese Unterseite ist als Streamlit app aufgesetzt und ergänzt home.py. Es baut auf einem der einfachen Regressionsmodelle aus 2.1 auf und verwendet für die Preisvorhersage lediglich die Anzahl Quadratmeter in bezug auf die Wohnfläche.

- `expert_model.py`: Dieses Script ist ebenfalls als Streamlit app aufgesetzt und ergänzt ebenfalls home.py. Es verwendet zur Vorhersage das Modell aus 2.2 welches für Kaggle am besten abgeschnitten hat und natürlich auch dessen Scaler für die Inputvariablen. Das App erlaubt es entweder die Daten in einem Formular manuell einzugeben, oder die Werte getrennt durch Semikolon als Liste mitzugeben. 
<br><br>
Alle Apps sind kommentiert um die einzelnen Codezeilen zu verstehen und sollten das App nachvollziehbar machen. <br><br>
