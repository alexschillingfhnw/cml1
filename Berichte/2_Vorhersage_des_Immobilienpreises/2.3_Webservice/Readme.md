## 2.3 Webservice

Erstelle einen Web-Service mit einem Modell, welche via http-Request angefragt werden kann und für ein bestimmtes Objekt eine Preis-Vorhersage zurückgibt. Da einige Feature für normale User unbekannt sind, habt ihr zwei Möglichkeiten:

Ihr verwendet euer bestes Modell und nehmt an, dass der Service von Experten benutzt wird, welche diese Werte kennen.

Ihr verwendet ein simpleres Modell, welches ausschliesslich Features braucht, die ein normaler Käufer zur Verfügung hat. Z.b., Wohnfläche, Kanton, ...

Abgabe

Skript, welches den Web-Service startet und eine kurze Anleitung, wie dieser zu verwenden ist.


### App Beschreibung

- `home.py`: Diese Datei bildet die "Mainpage" des Streamlit Apps. Es ist in der Lage die weiteren Dateien in subfolder `./pages` zu erkennen und als Unterseiten, bzw. in der Navigation als Navigationspunkte aufzulisten. <br>
Die Homeseite, gibt einen kurzen einblick um was es geht, und welcher Menüpunkt für welche Zielgruppe gedacht ist.

- `simple_regression.py`: Diese Unterseite ist als Streamlit app aufgesetzt und ergänzt home.py. Es baut auf einem der einfachen Regressionsmodelle aus 2.1 auf und verwendet für die Preisvorhersage lediglich die Anzahl Quadratmeter in bezug auf die Wohnfläche.

- `expert_model.py`: Dieses Script ist ebenfalls als Streamlit app aufgesetzt und ergänzt ebenfalls home.py. Es verwendet zur Vorhersage das Modell aus 2.2 welches für Kaggle am besten abgeschnitten hat und natürlich auch dessen Scaler für die Inputvariablen. Das App erlaubt es entweder die Daten in einem Formular manuell einzugeben, oder die Werte getrennt durch Semikolon als Liste mitzugeben. 
<br><br>
Alle Apps sind kommentiert um die einzelnen Codezeilen zu verstehen und sollten das App nachvollziehbar machen. <br><br>

#### Sample Data

Hier ein paar testzeilen aus dem X_test File, welches als liste im App predicted werden kann:<br><br>
Actual Price: 1'900'000 CHF <br>
2003.6666666666667;220.0;186.0;733.0;6.5;0.4870368092141459;38.0;1015.0;4188.0;5241.0;27.8039585297;44.392082940600005;1.1310084826;26.6729500471;2.32;0.7933010137000001;32.31231231;6.3610662359;940.677966102;9990.0;4212.0;4.281098546;6.35;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;1.0<br><br>

Actual Price: 1'850'000 CHF <br>
2003.6666666666667;230.0;186.0;702.0;7.5;0.6910894704215856;38.0;1015.0;4188.0;5241.0;27.8039585297;44.392082940600005;1.1310084826;26.6729500471;2.32;0.7933010137000001;32.31231231;6.3610662359;940.677966102;9990.0;4212.0;4.281098546;6.35;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;1.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0<br><br>

Actual Price: 850'000 CHF <br>
2016.3333333333333;131.0;206.33333333333334;320.6666666666667;4.5;2.6896171214356617;14.0;9.0;308.0;331.0;30.6763285024;51.44927536229999;4.5893719807;13.2850241546;2.23;1.9946808511;9.25566343;4.739336492900001;376.829268293;1545.0;686.0;2.2342586324;5.89;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;1.0;0.0;0.0;0.0<br><br>

Actual Price: 900'000 CHF <br>
2003.6666666666667;140.0;140.0;206.0;6.5;0.4478037082087512;38.0;1015.0;4188.0;5241.0;27.8039585297;44.392082940600005;1.1310084826;26.6729500471;2.32;0.7933010137000001;32.31231231;6.3610662359;940.677966102;9990.0;4212.0;4.281098546;6.35;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;1.0;0.0<br><br>

Actual Price: 795'000 CHF <br>
2013.0;156.0;242.0;222.0;4.5;3.0384665928009302;14.0;9.0;308.0;331.0;30.6763285024;51.44927536229999;4.5893719807;13.2850241546;2.23;1.9946808511;9.25566343;4.739336492900001;376.829268293;1545.0;686.0;2.2342586324;5.89;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;1.0;0.0<br><br>
