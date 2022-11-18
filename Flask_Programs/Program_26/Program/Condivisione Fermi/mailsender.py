import smtplib


def sendemail(to_addr_list, subject, message, smtpserver='smtp.gmail.com:587'):
    try:
        email_text = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (from_addr, ", ".join(to_addr_list), subject, message)
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(smtp_login, smtp_password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        print(problems)
        server.quit()
        return True
    except Exception as e:
        return False


chiavi = open("configurazione.txt", 'r')
dati = chiavi.readline()
_, _, from_addr, smtp_login, smtp_password, _, _, _, _ = dati.split("|", 8)
email_file = open("maildump.csv", "r")
email = email_file.readline()
mail = email.split(";")
for indirizzo in mail:
    print(indirizzo)
    successo = sendemail(indirizzo, "Chiusura account",
                         "Gentile utente di Condivisione,\nIn vista dell'inizio di un nuovo anno scolastico, la sua utenza su Condivisione e' stata rimossa.\nPer tornare ad usufruire dei servizi di Condivisione, le sara' necessario creare una nuova utenza.\n\nGrazie per aver utilizzato Condivisione!\nQuesto messaggio e' stato creato automaticamente.")
    print(successo)
