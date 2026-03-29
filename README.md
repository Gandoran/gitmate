# Gitmate

## 📖 Descrizione Dettagliata
Gitmate è un client per il sistema di codice AI "ollama", utilizzato per automatizzare processi di commit e gestione del codice. Il software permette agli sviluppatori di creare, modificare e inviare modifiche al loro repository Git in modo più efficiente, utilizzando l'intelligenza artificiale per migliorare la qualità delle code review.

Il caso d'uso principale di Gitmate è nella collaborazione di team di sviluppo software, dove gli ingegneri possono concentrarsi sul codice piuttosto che sull'amministrazione del repository. Gitmate automatizza processi come l'estrazione delle modifiche, la creazione di commit e la gestione delle code review utilizzando l'intelligenza artificiale per migliorare la qualità delle modifiche.

## 🚀 Funzionalità Principali
Gitmate offre diverse funzionalità chiave per migliorare la productivity dei team:

- **Estrazione delle modifiche**: Gitmate può estrarre automaticamente le modifiche dal repository Git, prepararle per il commit e utilizzare l'intelligenza artificiale per analizzarle.
  
- **Creazione di commit**: Una volta estratte, le modifiche vengono utilizzate per creare commit automatici, migliorando la velocità e la consistenza dei commit.

- **Gestione delle code review**: Gitmate può integrarsi con il sistema di codice AI "ollama" per gestire le code review, offrendo suggerimenti basati sull'intelligenza artificiale per migliorare la qualità delle modifiche.

- **Animazioni durante l'esecuzione dei comandi**: Gitmate offre un'esperienza utente migliorata attraverso l'utilizzo di animazioni visive durante l'esecuzione dei comandi, rendendo l'interazione con il software più fluida e accattivante.

## 🛠️ Architettura e Tecnologie
Gitmate è composto da diverse parti, ognuna sviluppata in un linguaggio di programmazione diverso per raggiungere il miglioramento delle prestazioni e della funzionalità. L'architettura del software è basata su una struttura modulare che include:

- **Backend Python**: Il backend di Gitmate è scritto in Python, utilizzando la libreria `setuptools` per la gestione della compilazione e l'esecuzione.

- **Intelligenza Artificiale Ollama**: L'intelligenza artificiale utilizzata da Gitmate per migliorare la qualità delle code review è sviluppata e ospitata dal sistema "ollama".

## 🧩 Moduli e Componenti Core
Gitmate è composto da vari moduli principali che si interagiscono tra loro per raggiungere il suo scopo. Ecco una descrizione dettagliata di ciascuno di questi componenti:

- **ai_engine.py**: Questo modulo contiene la funzione `ollama_chat`, utilizzata per inviare richieste al sistema AI "ollama" e ricevere risposte basate sulla logica del sistema.

- **ai_runner.py**: Il modulo `ai_runner.py` include la funzione `execute_with_animation`, che esegue una serie di comandi, visualizzando un'animazione durante l'esecuzione per migliorare l'esperienza dell'utente.

- **cmd_commit.py** e **cmd_readme.py**: Questi moduli contengono le funzioni `execute`, utilizzate per eseguire specifiche operazioni come la creazione di commit e l'aggiornamento del README, rispettivamente.

- **folder_extractor.py** e **git_extractor.py**: I moduli `folder_extractor.py` e `git_extractor.py` contengono funzioni per estrarre informazioni dai repository Git, come le modifiche apportate, i file modificati e altre informazioni utili per il processo di commit.

- **istructions.py**, **loading_bar.py** e **prompt_builder.py**: Questi moduli gestiscono aspetti specifici della logica del programma, inclusa la creazione di prompt per l'interfaccia utente, la gestione dell'animazione di caricamento durante i processi di esecuzione e la costruzione di prompt basati su regole predefinite.

- **template_manger.py** e **token_reducer.py**: I moduli `template_manger.py` e `token_reducer.py` si occupano della gestione delle templatizzazioni del codice e della riduzione dei token, rispettivamente, per migliorare la qualità delle modifiche e la produttività del software.

## 💻 Installazione e Avvio
Per installare Gitmate, eseguire il comando seguente:

```bash
pip install -e .
```

Successivamente, si può avviare l'applicazione tramite il comando:

```bash
gitmate -<command> -<lan>
```