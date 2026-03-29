from scribe import ai_runner

def handle_interaction(starting_message, change_prompt_m, func_accept, func_refuse, output_title="Generato"):
    message = starting_message
    while True:
        print(f"\n{output_title}:\n\n{message}\n")
        response = input("Do you want to proceed? (Y/N/M):\n> ").strip().upper()
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
            message = ai_runner.execute_with_animation(prompt_modifica, "", "Applicazione modifiche...")
        else:
            print("Not a valid choice, please enter: Y, N, or M.")