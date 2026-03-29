import sys
import threading
from scribe import ai_engine, loading_bar

def execute_with_animation(istruction, date, bar_text="I'm reasoning"):
    stop_event = threading.Event()
    an_thread = threading.Thread(target=loading_bar.print_bar, args=(stop_event, bar_text))
    an_thread.start()
    message = ""
    try:
        message = ai_engine.ollama_chat(istruction, date)
    except ConnectionError:
        print("\n Error: cannot connect to ollama. Make sure the Ollama app is open and running on your PC.")
        sys.exit(1)
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        sys.exit(1)
    finally:
        stop_event.set()
        an_thread.join()
        
    return message