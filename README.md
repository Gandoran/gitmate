# GitMate - Client per il tuo Sistema Awesome

## 📖 Descrizione
GitMate è un client che utilizza la tecnologia Ollama per automatizzare processi di controllo del codice sorgente (VCS) e generare documentazione automatica. Questo strumento facilita la gestione dei commit, creando messaggi di commit concisi e README professionali in modo intelligente. 

## 🚀 Funzionalità Principali
- **Generatore di Messaggio di Commit**: Automatically creates concise commit messages following the Conventional Commits standard.
- **Creazione di README**: Automatically generates professional and well-structured README files based on project code.

## 🛠️ Architettura e Tecnologie
GitMate è progettato per essere facile da installare e usare. Le principali tecnologie utilizzate includono:
- Python 3.9 o superiore
- Ollama: Libreria per generazione di testo basata su IA

## 💻 Come si usa / Installazione
Per installare GitMate, esegui il seguente comando:

```bash
pip install .
```

Dopo averlo installato, puoi utilizzare i seguenti comandi CLI:
- Per generare un messaggio di commit:
  ```bash
  gitmate -commit
  ```
- Per generare un README:
  ```bash
  gitmate -readme
  ```

Questi comandi utilizzeranno l'IA per analizzare il codice del tuo progetto e generare contenuti appropriati.