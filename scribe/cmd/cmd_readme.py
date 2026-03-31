from scribe.extractor import tree_generator
from scribe.extractor import folder_extractor
from scribe.ai_package import template_manger
from scribe.ai_package import ai_runner
from scribe.cmd import interaction_handler
from scribe.ai_package import istructions, prompt_builder

def execute(lan):
    text = folder_extractor.extract_project_text()
    tree = tree_generator.get_project_structure()
    print(f"Tokens used by the text: {len(text)//4}")
    base_prompt = prompt_builder.build_prompt(istructions.REGOLE_README, lan)
    final_prompt = template_manger.add_template(text+tree, base_prompt) + tree
    message = ai_runner.execute_with_animation(final_prompt, text, "Writing the README.md",profile="heavy")
    readme_completo = f"{message}\n\n## Project Structure:\n{tree}"
    return interaction_handler.handle_interaction(
        starting_message=readme_completo,
        change_prompt_m="Modifica il seguente README rispettando questa richiesta:",
        func_accept=save_readme,
        func_refuse=undo_readme,
        output_title="README Generated"
    )

def add_project_tree(self):
    tree = tree_generator.get_project_structure()
    return self + f"{tree}\n\nCodice:\n"

def save_readme(msg):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(msg)
    return "README.md saved!"

def undo_readme():
    return "README discarded"