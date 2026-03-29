from scribe import folder_extractor, prompt_builder,istructions
from scribe.template_manger import choose_and_add_template
from scribe.ai_runner import execute_with_animation

def execute(lan):
    text = folder_extractor.extract_project_text()
    print(f"Token used by the text: %.1f" %(len(text)/4))
    prompt_base = prompt_builder.build_prompt(istructions.REGOLE_README, lan)
    prompt_finale = choose_and_add_template(text, prompt_base)
    message = execute_with_animation(prompt_finale, text, "Writing the README.md")
    print(f"\nREADME generated:\n\n{message}\n")
    response = input("Do you want to save it as README.md? (Y/N): ")
    if response.lower() == 'y':
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(message)
        return "README.md saved!"
    else:
        return "README discarded"