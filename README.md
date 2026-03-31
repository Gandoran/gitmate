# Gitmate

## 📖 Descrizione Dettagliata
Gitmate è un client per un sistema di integrazione tra versionamento del codice (Git) e assistente AI. Il suo scopo principale è fornire strumenti avanzati per gestire e documentare i cambiamenti nel codice sorgente, utilizzando l'AI per generare documentazione automatica basata sulle modifiche apportate.

Il sistema supporta la creazione di documenti README, aggiornamento della storia del progetto (changelog), commit e rilascio. L'assistente AI viene utilizzato per analizzare le modifiche nel codice e generare contenuti strutturati che possono essere inseriti nei documenti.

## 🚀 Funzionalità Principali
- **Documentazione automatizzata**: Gitmate può generare automaticamente sezioni README basate sulle modifiche apportate al codice sorgente.
- **Gestione del changelog**: L'assistente AI viene utilizzato per creare e mantenere aggiornati i log dei cambiamenti (changelog).
- **Commit e rilascio automatizzati**: Gitmate fornisce funzionalità per gestire commit e rilasci automaticamente, assicurando che tutte le modifiche siano registrate correttamente.
- **Intelligenza artificiale**: L'AI viene utilizzato per comprendere il contesto delle modifiche nel codice e generare contenuti appropriati.

## 🛠️ Architettura e Tecnologie
Il progetto è strutturato in moduli separati, ciascuno responsabile di un aspetto specifico del sistema. I principali linguaggi utilizzati sono Python e Rust (per alcune funzionalità), con l'ecosistema di gestione dipendenze basato su `setuptools` e `pip`.

### Struttura Moduli
- **Scribble**: Contiene i principali componenti del sistema.
  - **Extractor**: Estrae informazioni dal progetto, come la struttura del file system e le modifiche Git.
  - **Git**: Interagisce con il repository Git per ottenere e gestire cambiamenti.
  - **Cmd**: Implementa comandi per eseguire azioni come aggiornare il changelog o creare commit.
  - **AI Package**: Utilizza l'AI per generare documentazione e altri contenuti basati sulle modifiche del codice.
- **Scribble AI**: Contiene le implementazioni specifiche dell'assistente AI.

### Dipendenze
Il progetto dipende da:
- `ollama`: Libreria Python per interagire con l'assistente AI.
- `pyyaml`: Libreria Python per la gestione dei file YAML.
- `rich`: Libreria Python per creare output formattati in terminale.

## 🧩 Moduli e Componenti Core
### **Scribble**
#### Extractor
- **folder_extractor.py**: Estrae il testo di un progetto a partire dalla directory radice.
- **gitignore_parser.py**: Analizza i file `.gitignore` per determinare quali file devono essere ignorati.
- **tree_generator.py**: Genera una rappresentazione strutturata del progetto come albero.

#### Git
- **git_extractor.py**: Estrae le modifiche recenti dal repository Git, incluso il nome della ramiattura corrente.

#### Cmd
- **cmd_changelog.py**: Gestisce la creazione e l'aggiornamento del changelog.
- **cmd_commit.py**: Gestisce i commit Git.
- **cmd_readme.py**: Gestisce la generazione e l'aggiornamento di documenti README.
- **cmd_release.py**: Gestionisce il processo di rilascio.
- **interaction_handler.py**: Gestisce le interazioni con l'utente, come la conferma o la rifiuto di azioni.
- **loading_bar.py**: Mostra una barra di caricamento durante l'esecuzione dei processi.

#### AI Package
- **ai_engine.py**: Carica la configurazione dell'assistente AI e utilizza Ollama per generare contenuti basati sulle modifiche del codice.
- **ai_runner.py**: Esegue comandi con animazione, gestendo gli errori e interagendo con il thread worker.
- **istructions.py**: Non implementato nel codice fornito.
- **prompt_builder.py**: Costruisce i prompt da inviare all'assistente AI per generare contenuti specifici.
- **template_manger.py**: Gestisce le templatizzazioni e calcola i token necessari.
- **token_reducer.py**: Riduce i file in base al numero di token.

### **Scribble AI**
I componenti dell'assistente AI sono implementati principalmente in Rust, ma non sono inclusi nel codice fornito.

## 💻 Installazione e Avvio
Per installare il progetto, è necessario eseguire i seguenti comandi:
```bash
pip install gitmate
```

Per avviare il sistema, utilizzare il comando:
```bash
gitmate
```

### Comandi per Gitmate
Per eseguire specifiche azioni con Gitmate, utilizza i seguenti comandi:

- **Commit**: Aggiorna il repository Git.
  ```bash
  gitmate -commit
  ```
  
- **README**: Genera o aggiorna un documento README.
  ```bash
  gitmate -readme
  ```
  
- **Changelog**: Gestisce la creazione e l'aggiornamento del changelog.
  ```bash
  gitmate -changelog
  ```
  
- **Release**: Gestionisce il processo di rilascio.
  ```bash
  gitmate -release
  ```
  
- **Lan**: Mostra informazioni sulla lingua del progetto.
  ```bash
  gitmate -lan
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