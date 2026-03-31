# GitMate

## 📖 Descrizione Dettagliata
GitMate è un client per un sistema di gestione di progetti che si integra con sistemi di controllo versione come Git e offre funzionalità avanzate per l'analisi, generazione e gestione del codice. Il software risolve il problema di automatisare i processi di commit, gestione dei cambiamenti, creazione di documentazioni e release, fornendo un'interfaccia più fluida e efficiente per gli sviluppatori.

Il suo caso d'uso principale è nella gestione del flusso di lavoro quotidiano degli sviluppatori, permettendogli di concentrarsi sul codice piuttosto che sulla routine delle operazioni di controllo versione. GitMate si integra con altri strumenti come Ollama (un assistente AI), YAML per la gestione della configurazione e Rich per l'output formattato.

## 🚀 Funzionalità Principali
### 1. Gestione dei Commit
- **Commit**: permette di creare commit automatizzati basati sui cambiamenti del progetto.

### 2. Generazione e Modifica della Documentazione
- **README Management**: gestisce la creazione, modifica e salvataggio della documentazione README per i progetti.
- **Changelog Management**: gestisce la creazione, modifica e salvataggio del changelog dei progetti.
- **Release Management**: gestisce la preparazione e pubblicazione di release di progetti.

### 3. Analisi e Generazione di Codice
- **AI Engine**: utilizza un assistente AI per analizzare i cambiamenti del codice e generare documentazioni e commit intelligenti.
- **Prompt Builder**: genera prompt personalizzati per l'assistente AI basati sulle regole del progetto e sui cambiamenti.

### 4. Estrazione di Informazioni
- **Folder Extractor**: estrae il testo dai file all'interno di una cartella specifica.
- **Gitignore Parser**: analizza i file `.gitignore` per determinare quali file o directory dovrebbero essere ignorati dal controllo versione.
- **Tree Generator**: genera la struttura del progetto come un albero.

### 5. Integrazione con Git
- **Git Extractor**: estrae le modifiche recenti dal repository di Git.
- **Push e Pull**: permette di inviare i commit al repository remoto e recuperare gli aggiornamenti più recenti.

## 🛠️ Architettura e Tecnologie
### Linguaggi e Framework Utilizzati
- **Python 3.9+**
- **Ollama**: un assistente AI utilizzato per l'analisi e generazione di codice.
- **PyYAML**: per la gestione della configurazione in formato YAML.
- **Rich**: per l'output formattato.

### Moduli e Struttura del Progetto
Il progetto è strutturato in diverse directory, ciascuna responsabile di un aspetto specifico dell'applicazione. La comunicazione tra i moduli avviene principalmente attraverso funzioni esposte.

- **`cmd/`**: Contiene comandi per la gestione del progetto, come commit, release e documentazione.
  - `cmd_commit.py`: Gestisce il comando di commit.
  - `cmd_release.py`: Gestisce il comando di release.
  - `cmd_readme.py`: Gestisce il comando di gestione della documentazione README.

- **`ai_package/`**: Contiene l'engine AI per l'analisi e generazione di codice.
  - `ai_engine.py`: Carica la configurazione e invia messaggi all'assistente AI.
  - `token_reducer.py`: Riduce i token nei file per una gestione più efficiente.

- **`extractor/`**: Estrae informazioni dai progetti.
  - `folder_extractor.py`: Estrae il testo da una cartella.
  - `gitignore_parser.py`: Analizza i file `.gitignore`.

- **`git/`**: Contiene funzioni per l'interazione con Git.
  - `git_extractor.py`: Estrae modifiche e commit dal repository di Git.

## 🧩 Moduli e Componenti Core
### 1. `ai_package.ai_engine`
Questo modulo contiene la logica principale per l'interfacciamento con l'assistente AI. Ha funzioni per caricare la configurazione e inviare messaggi all'assistente.
- **`load_config()`**: Carica la configurazione dell'assistente AI.
- **`ollama_chat(system_istruction, git_changes, profile="light")`**: Invia una richiesta all'assistente AI per ottenere una risposta basata sui cambiamenti del progetto.

### 2. `cmd.cmd_commit`
Gestisce il comando di gestione del commit.
- **`execute(lan)`**: Esegue il comando di generazione del commit.
- **`save_commit(msg)`**: Pubblica la versione modificata del changelog.
- **`undo_commit()`**: Annulla l'ultima commit creato.

### 3. `git.git_extractor`
Contiene funzioni per l'estrazione di informazioni dai repository Git.
- **`extract_changes()`**: Estrae le modifiche recenti dal repository.
- **`git_commit(message)`**: Fa un commit sul repository con il messaggio fornito.

### 4. `extractor.folder_extractor`
Estrae il testo dai file all'interno di una cartella specifica.
- **`extract_project_text(root_path=".")`**: Estrae il testo da tutti i file in una cartella e le sue sottocartelle.

### 5. `cmd.cmd_readme`
Gestisce il comando di gestione della documentazione README.
- **`execute(lan)`**: Esegue il comando di generazione o modifica del README.
- **`save_readme(msg)`**: Salva la versione modificata del README.

## 💻 Installazione e Avvio
Per installare GitMate, è necessario eseguire i seguenti passaggi:
1. Clonare il repository:
   ```bash
   git clone https://github.com/Gandoran/gitmate.git
   ```
2. Creare un ambiente virtuale (opzionale ma raccomandato):
   ```bash
   python -m venv venv
   source venv/bin/activate  # su Windows usa `venv\Scripts\activate`
   ```
3. Installare le dipendenze:
   ```bash
   pip install -e .
   ```
4. Eseguire GitMate:
   ```bash
   gitmate
   ```

## Project Structure:
```text
gitmate/
├── scribe
│   ├── ai_package
│   │   ├── ai_engine.py
│   │   ├── ai_runner.py
│   │   ├── istructions.py
│   │   ├── prompt_builder.py
│   │   ├── template_manger.py
│   │   └── token_reducer.py
│   ├── cmd
│   │   ├── cmd_changelog.py
│   │   ├── cmd_commit.py
│   │   ├── cmd_readme.py
│   │   ├── cmd_release.py
│   │   ├── interaction_handler.py
│   │   └── loading_bar.py
│   ├── extractor
│   │   ├── folder_extractor.py
│   │   ├── gitignore_parser.py
│   │   └── tree_generator.py
│   ├── git
│   │   └── git_extractor.py
│   ├── template
│   ├── __init__.py
│   ├── create_global_configuration.py
│   └── main.py
└── pyproject.toml
```

Questo README fornisce un'introduzione dettagliata al progetto GitMate, inclusa la sua architettura e i principali componenti utilizzati.