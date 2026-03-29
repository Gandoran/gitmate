MAINTAIN_TYPE_RUST = ('fn ', 'struct ', 'enum ', 'impl ', 'pub trait ', 'mod ')
MAINTAIN_TYPE_TS = ('interface ', 'type ', 'class ', 'function ', 'export const ', 'export function ', 'export class ')
MAINTAIN_TYPE_TSX = ('export default function ', 'export function ', 'export const ', 'interface ', 'type ')
MAINTAIN_TYPE_PY = ('def ', 'class ', '@')
MAINTAIN_TYPE_JAVA = ('class ', 'interface ', 'enum ', 'public ', 'protected ', 'private ', '@')

def file_clean(file_path):
    if file_path.endswith('.rs'): regole = MAINTAIN_TYPE_RUST
    elif file_path.endswith('.ts'): regole = MAINTAIN_TYPE_TS
    elif file_path.endswith('.tsx'): regole = MAINTAIN_TYPE_TSX
    elif file_path.endswith('.py'): regole = MAINTAIN_TYPE_PY
    elif file_path.endswith('.java'): regole = MAINTAIN_TYPE_JAVA
    else: regole = None

    testo_estratto = f"\n--- FILE: {file_path} ---\n"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            if regole is None:
                testo_estratto += f.read()
            else:
                for line in f:
                    riga_pulita = line.strip() 
                    if riga_pulita.startswith(regole):
                        testo_estratto += line 
    except Exception:
        return ""
    return testo_estratto + "\n"