import ollama

print("Inviando la richiesta al modello locale. Attendi...")

# Chiamiamo il server locale di Ollama
response = ollama.chat(model='qwen2.5-coder:7b', messages=[
  {
    'role': 'user',
    'content': 'Spiega in una frase cos è un commit in Git.',
  },
])

# Stampo la risposta
print("\nRisposta dell'AI:")
print(response['message']['content'])