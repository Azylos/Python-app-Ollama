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

    # Liste pour stocker l'historique des messages
messages_history = []

def initialize_context(role_description: str) -> None:
    """
    Initialise le contexte du chatbot avec un rôle spécifique
    Args:
        role_description: Description du rôle que doit jouer le modèle
    """
    # On efface l'historique existant
    messages_history.clear()
    
    # On ajoute le message de contexte qui définit le rôle
    context_message = {
        'role': 'system',
        'content': f"Tu es un assistant spécialisé qui agit en tant que {role_description}. " \
                  f"Réponds toujours en respectant ce rôle."
    }
    messages_history.append(context_message)

def send_message_with_history(model_name: str, message: str) -> str:
    """
    Envoie un message en tenant compte de l'historique et du contexte
    Args:
        model_name: Nom du modèle à utiliser
        message: Message à envoyer
    Returns:
        La réponse du modèle
    """
    # Ajout du nouveau message à l'historique
    messages_history.append({
        'role': 'user',
        'content': message
    })
    
    # Envoi de tout l'historique au modèle
    response = chat(model=model_name, messages=messages_history)
    
    # Ajout de la réponse à l'historique
    messages_history.append(response.message)
    
    return response.message.content

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialisation du contexte
    initialize_context("expert en Python qui donne des explications claires et détaillées")
    
    # Test de la conversation
    reponse = send_message_with_history('deepseek-r1', 
        'Explique-moi ce qu\'est un décorateur en Python')
    print(reponse)