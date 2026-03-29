from scribe import folder_extractor, prompt_builder, istructions
from scribe import template_manger
from scribe import ai_runner
from scribe import interaction_handler

def execute(lan):
    text = folder_extractor.extract_project_text()
    print(f"Tokens used by the text: {len(text)//4}")
    base_prompt = prompt_builder.build_prompt(istructions.REGOLE_README, lan)
    final_prompt = template_manger.add_template(text, base_prompt)
    message = ai_runner.execute_with_animation(final_prompt, text, "Writing the README.md")
    return interaction_handler.handle_interaction(
        starting_message=message,
        change_prompt_m="Modifica il seguente README rispettando questa richiesta:",
        func_accept=save_readme,
        func_refuse=undo_readme,
        output_title="README Generated"
    )

def save_readme(msg):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(msg)
    return "README.md saved!"

def undo_readme():
    return "README discarded"