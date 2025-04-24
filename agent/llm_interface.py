import requests

class LLMClient:
    """
    Classe permettant de communiquer avec un modèle local via Ollama (par défaut : mistral).
    """

    def __init__(self, model="mistral"):
        """
        Initialise le client avec le nom du modèle (par défaut : 'mistral').

        :param model: Nom du modèle à utiliser dans Ollama (ex : 'mistral', 'mistral:7b', etc.)
        """
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"

    def run(self, prompt: str, code_snippet: str) -> str:
        """
        Envoie une requête à Ollama avec un prompt et un extrait de code.

        :param prompt: Prompt de départ (rôle à jouer par l'IA)
        :param code_snippet: Code Python à analyser
        :return: Réponse générée par le modèle
        """
        full_prompt = f"{prompt}\n\n```python\n{code_snippet}\n```"

        response = requests.post(
            self.ollama_url,
            json={
                "model": self.model,
                "prompt": full_prompt,
                "stream": False
            }
        )

        # Gestion d’erreur basique
        if not response.ok:
            raise Exception(f"Erreur Ollama : {response.status_code} {response.text}")

        return response.json()["response"]
