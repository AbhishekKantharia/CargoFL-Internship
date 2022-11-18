# ![Condivisione-Fermi](/static/Condivisione.png)

Un sito per permettere la pianificazione di ripetizioni gratuite tra studenti.

È [attualmente utilizzato](https://condivisione.fermi-mo.gov.it/login) 
dall'[ITIS Enrico Fermi di Modena](https://www.fermi-mo.edu.it/pvw/app/MOIT0016/pvw_sito.php) nelle attività della 
Peer Education. Negli anni, ha aiutato centinaia di studenti gestendo l'erogazione sicura e controllata di videolezioni.

# Caratteristiche principali

* Gestione di corsi di recupero, sia da parte di volontari autorizzati che da parte di docenti.
* Alte capacità di interazione con gli utenti, sia mediante Telegram che mediante email.
* Facilmente scalabile ed estendibile a qualsiasi realtà scolastica, a patto che vi sia una pre-esistente struttura di Peer Education presente in loco.
* Funzionalità di appello: i genitori degli studenti che partecipano alle lezioni vengono sempre informati della presenza (o dell'assenza) dei propri figli.

## Requisiti

- [Git](https://git-scm.com/)
- [Python 3.6 o superiore](https://www.python.org/downloads/) con `pip` e `venv`

## Installazione

1. _Clona_ questo repository con Git ed entra nella directory creata:  
   ```bash
   git clone https://github.com/LBindustries/Condivisione-Fermi
   cd Condivisione-Fermi
   ```
   
2. Crea un nuovo _venv_ in cui installare pacchetti e attivalo:
   ```powershell
   # Su Windows Powershell
   py -m venv venv
   ./venv/bin/activate.ps1
   ```
   ```bash
   # Su Linux (Bash)
   python3 -m venv venv
   source ./venv/bin/activate
   ```

3. Installa i pacchetti richiesti all'interno del venv:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Crea un file `configurazione.txt` o una variabile di ambiente `SITE_CONFIG` con il seguente contenuto:
   ```
   cookiekey|telegramkey|fromemail|gmailusername|gmailpassword|sentrydsn|recaptchapubkey|recaptchasecret|brasamail
   ```
   Sostituisci i seguenti parametri con il loro valore corrispondente, rimuovendoli completamente nel caso si voglia 
   lasciare vuoto un parametro opzionale:
   - `cookiekey`: una chiave segreta sicura che sarà utilizzata per criptare i cookies (puoi usare una stringa casuale di 
     testo di almeno 24 caratteri, oppure generala con `python -c "import os; print(os.urandom(24))"`)
   - `telegramkey`: l'API key di un bot di Telegram ottenuta registrando un bot su [@BotFather](https://t.me/BotFather).
   - `fromemail`: _(Opzionale)_ Email completa (`example@gmail.com`) di un account [Gmail](gmail.com) usato per inviare email
   - `gmailusername`: _(Opzionale)_ Username di un account [Gmail](gmail.com) usato per inviare email
   - `gmailpassword`: _(Opzionale)_ Password di un account [Gmail](gmail.com) usato per inviare email
   - `sentrydsn`: _(Opzionale)_ Token ottenuto da un'istanza di [Sentry](https://sentry.io/) per il reporting automatico degli errori
   - `recaptchapubkey`: _(Opzionale)_ Chiave pubblica ottenuta dalla 
     [Admin Console di ReCAPTCHA](https://www.google.com/recaptcha/admin/create)
   - `recaptchasecret`: _(Opzionale)_ Chiave segreta ottenuta dalla 
     [Admin Console di ReCAPTCHA](https://www.google.com/recaptcha/admin/create)
   - `brasamail`: _(Opzionale)_ `si` per abilitare l'eliminazione **definitiva** tutti gli account utente registrati

5. Finito! Ora puoi avviare Condivisione-Fermi mentre sei all'interno del _venv_ con:
   ```bash
   python server.py
   ```

## Deployment

Condivisione-Fermi può essere usato con tutte le opzioni di deployment 
[supportate da Flask](https://flask.palletsprojects.com/en/1.1.x/deploying/), ma si suggerisce di utilizzare 
[`apache2` con `mod_wsgi`](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/) in quanto essa è la modalità 
attualmente utilizzata dall'ITIS Fermi.

Per ulteriori informazioni relative al deployment, si consiglia di fare riferiemento al [manuale](/docs/Manual.pdf).

## Documentazione

E' disponibile [un manuale (in inglese)](/docs/Manual.pdf) per l'utilizzo di Condivisione-Fermi, il quale è diviso in sezioni a seconda del tipo di utente della piattaforma (dall'utente normale, all'amministratore di sistema).

## Contributi

Per **segnalare bug**, **fare domande** o **richiedere nuove feature**, puoi 
[aprire una issue](https://github.com/LBindustries/Condivisione-Fermi/issues/new) nella pagina progetto di GitHub.

<!--Per segnalare falle di sicurezza cosa bisogna fare? Serve un file SECURITY.md 
https://github.com/LBindustries/Condivisione-Fermi/security/policy -->

Se hai sviluppato una **modifica al software**, puoi 
[aprire una pull request](https://github.com/LBindustries/Condivisione-Fermi/pulls) per richiedere di integrarla nel progetto!

<!--

## Copyright

Condivisione-Fermi è rilasciato sotto la licenza GNU LGPLv3. Per ulteriori informazioni riguardo la licenza, fare riferimento al 
[manuale](/docs/Manual.pdf).

-->
