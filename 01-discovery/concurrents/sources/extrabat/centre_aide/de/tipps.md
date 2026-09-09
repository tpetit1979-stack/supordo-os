---
url: https://servicescompris.extrabat.com/de/tipps
url_finale: https://servicescompris.extrabat.com:443/de/tipps/
date_collecte: 2026-09-09
destination: centre_aide
---

Die Antwort wird etwas technisch ausfallen.

Das Problem ist darauf zurückzuführen, dass die E-Mail in Ihrem Namen vom Extrabat-Server gesendet wird und dass die Konfigurationen Ihrer Domain es unserem Server nicht erlauben, E-Mails zu senden (vom Server blockierte E-Mails).

Sie müssen über Ihren Website-Host eine E-Mail-Adresse @ <Ihre_Domain> .com erstellen. Da die Domain Ihnen gehört, ist dies möglich. Wir können nicht auf öffentliche Server wie Yahoo, Gmail, Hotmail, Orange … zugreifen. Es ist jedoch möglich, Sicherheitsregeln für Ihre  Domain(@ <Ihre_Domain> .com) hinzuzufügen.

Dies wird als SPF-Sicherheit bezeichnet, ein Mechanismus zur Verhinderung von SPAM. Der Manager Ihrer Domain sollte dem DNS die folgende Regel hinzufügen:

„v = spf1 include: _spf.extrabat.com -all“

Dies garantiert nicht, dass die Mail gesendet wird, sollte jedoch die „Zustellbarkeit“ verbessern.

Dies geschieht häufig bei privaten Adressen von Kunden wie @ wanadoo.fr, @ hotmail.fr usw., da diese Anbieter andere Mailserver nicht zulassen.

Darüber hinaus reagieren sie mehr oder weniger empfindlich auf bestimmte verwendete Begriffe (Sonderangebote usw.). Dies ist immer häufiger der Fall.

Unsere Empfehlungen:

Setzen Sie in den Einstellungen jedes Benutzers (Zahnradsymbol rechts neben dem Avatar) das Feld auf „JA“, um eine Empfangsbestätigung vom Nachrichtenempfänger anzufordern

Überprüfen Sie für jedes Benutzerprofil, ob auch eine E-Mail-Adresse vorhanden ist, falls in den Einstellungen dieses Benutzers das Feld „Kopie per E-Mail erhalten”, auf „JA“ gesetzt ist.

Führen Sie einen Test mit 5 Kunden durch: Wenn Sie ein Angebot senden, rufen Sie den Kunden an, um sicherzustellen, dass er das Angebot erhalten hat.

 

Wenn dies dennoch nicht zufriedenstellend funktioniert, können Sie „Extrabat“ -E-Mails von Ihrer professionellen E-Mail-Adresse aus senden.

Dazu müssen Sie die Assistenz bitten, das Modul „SMTP Configurator“ zu aktivieren.