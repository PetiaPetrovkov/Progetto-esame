SPARTASPORT - GESTIONE ATTIVITÀ E TORNEI SPORTIVI

SpartaSport è un portale web per la gestione di attività sportive, tornei, recensioni e partecipazioni. 
Gli utenti possono registrarsi, partecipare a eventi sportivi, lasciare recensioni e visualizzare le attività a cui sono iscritti.

==================================================
COME USARE IL SITO
==================================================

1. HOME
   - Pagina principale con accesso a tutte le funzionalità (login, attività, tornei, recensioni).

2. REGISTRAZIONE
   - Crea un account inserendo nome utente, email e password.
   - Dopo la registrazione, è possibile accedere con le proprie credenziali.

3. LOGIN / LOGOUT
   - Dopo il login, l’utente viene reindirizzato alla dashboard.
   - È possibile effettuare il logout in qualsiasi momento.

4. DASHBOARD
   - Mostra informazioni sull'utente loggato e link alle funzionalità principali.

5. ATTIVITÀ
   - Elenco delle attività sportive disponibili.
   - Possibilità di partecipare e vedere i partecipanti.
   - Gli utenti possono scrivere recensioni.

6. TORNEI
   - Visualizzazione dei tornei con data e numero massimo di partecipanti.
   - Iscrizione e gestione partecipazioni.

7. PARTECIPAZIONI
   - Pagina personale per visualizzare attività e tornei a cui si è iscritti.
   - Possibilità di annullare l’iscrizione.

8. RECENSIONI
   - Gli utenti possono recensire un’attività e visualizzare le recensioni esistenti.

9. ADMIN
   - Accesso a /admin per la gestione completa da parte dello staff (inclusa la cancellazione delle recensioni).
   - Creare un superuser con: `python manage.py createsuperuser`

==================================================
STRUTTURA DEL PROGETTO
==================================================

MODELLI:
- Utente
- AttivitaSportiva
- PartecipazioneAttivita
- Torneo
- PartecipazioneTorneo
- Recensione

VISTE PRINCIPALI:
- home_view
- login_view / logout_view
- register_view
- dashboard_view
- lista_attivita_view
- dettaglio_attivita_view
- partecipa_attivita_view
- lista_tornei_view
- dettaglio_torneo_view
- partecipa_torneo_view
- scrivi_recensione_view
- lista_recensioni_view
- mie_partecipazioni_view

TEMPLATE HTML:
- base.html
- home.html
- login.html
- register.html
- utenti/dashboard.html
- attivitasportiva/lista.html
- attivitasportiva/dettaglio.html
- tornei/lista.html
- tornei/dettaglio.html
- recensioni/scrivi.html
- recensioni/lista.html
- partecipazioni/lista.html

==================================================
ISTRUZIONI DI AVVIO
==================================================

1. Crea l’ambiente virtuale:
   python -m venv .venv

2. Attivalo:
   .venv\Scripts\activate   (su Windows)

3. Installa Django:
   pip install django

4. Esegui le migrazioni:
   python manage.py makemigrations
   python manage.py migrate

5. Crea un superuser:
   python manage.py createsuperuser

6. Avvia il server:
   python manage.py runserver

7. Vai su:
   http://127.0.0.1:8000

==================================================

Autore: [Maksym Semenkov]
