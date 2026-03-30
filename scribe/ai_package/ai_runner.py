import sys
import os
import threading
from scribe.ai_package import ai_engine
from scribe.cmd import loading_bar

def _wait_and_handle_errors(worker_thread, result_dict):
    try:
        while worker_thread.is_alive():
            worker_thread.join(0.1)             
        if result_dict["error"]:
            raise result_dict["error"]
    except KeyboardInterrupt:
        print("\n\n Operation aborted by the user.")
        os._exit(0) 
    except ConnectionError:
        print("\n Error: cannot connect to ollama. Make sure the Ollama app is open and running on your PC.")
        sys.exit(1)
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        sys.exit(1)

def execute_with_animation(istruzioni, dati, testo_barra="I'm reasoning", profile="light"):
    result = {"message": "", "error": None}
    def worker_ollama():
        try:
            result["message"] = ai_engine.ollama_chat(istruzioni, dati,profile)
        except Exception as e:
            result["error"] = e
    stop_event = threading.Event()
    anim_thread = threading.Thread(target=loading_bar.print_bar, args=(stop_event, testo_barra), daemon=True)
    ollama_thread = threading.Thread(target=worker_ollama, daemon=True)
    anim_thread.start()
    ollama_thread.start()
    try:
        _wait_and_handle_errors(ollama_thread, result)
    finally:
        stop_event.set()
        
    return result["message"]