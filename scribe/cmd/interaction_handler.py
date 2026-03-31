from scribe.ai_package import ai_runner
from rich import console
from rich.markdown import Markdown
from rich.panel import Panel

console = console.Console()

def handle_interaction(starting_message, change_prompt_m, func_accept, func_refuse, output_title="Generato"):
    message = starting_message
    while True:
        response = messages_print(message,output_title)
        if response == 'Y':
            return func_accept(message)
        elif response == 'N':
            return func_refuse()

        elif response == 'M':
            feedback = input("What do you want to change? (e.g., 'Make it shorter', 'Add more details'):\n> ")
            prompt_modifica = (
                f"{change_prompt_m} '{feedback}'.\n"
                f"Restituisci SOLO il testo formattato, senza altre frasi.\n\n"
                f"TESTO ORIGINALE:\n{message}"
            )
            message = ai_runner.execute_with_animation(prompt_modifica, "", "applying changes...")
        else:
            print("Not a valid choice, please enter: Y, N, or M.")

def messages_print(message,output_title):
    console.print()
    md = Markdown(message)
    pannello = Panel(md, title=f"[bold cyan]{output_title}[/bold cyan]", border_style="cyan", expand=False)
    console.print(pannello)
    console.print()
    response = input("Do you want to proceed? (Y/N/M):\n> ").strip().upper()
    return response
