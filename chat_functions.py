# Importation de la fonction chat depuis la librairie ollama
from ollama import chat

# Fonction pour envoyer un message simple au modèle
def send_message(model_name: str, message: str) -> str:
    """
    Envoie un message simple au modèle et retourne sa réponse
    Args:
        model_name: Nom du modèle à utiliser (ex: 'deepseek-r1')
        message: Message à envoyer
    Returns:
        La réponse du modèle
    """
    # Création du message au format attendu par l'API
    messages = [{'role': 'user', 'content': message}]
    
    # Envoi de la requête au modèle
    response = chat(model=model_name, messages=messages)
    
    # Retour du contenu de la réponse
    return response.message.content

# Test de la fonction
if __name__ == "__main__":
    reponse = send_message('deepseek-r1', 'Dis-moi bonjour!')
    print(reponse)