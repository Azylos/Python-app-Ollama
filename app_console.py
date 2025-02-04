from colorama import Fore, init
from ollama import chat
import re 

# Initialisation de colorama pour la coloration du terminal
init(autoreset=True)

# Liste pour stocker l'historique des messages
messages_history = []
user_role = None  # Spécialisation choisie par l'utilisateur

# Fonction pour nettoyer la réponse de l'IA (suppression de <think> et contenu)
def clean_response(response_text):
    cleaned_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)  # Supprime tout entre <think>...</think>
    return cleaned_text.strip()  # Supprime les espaces inutiles

# Fonction pour initialiser le contexte du chatbot
def initialize_context(role_description: str):
    global user_role
    messages_history.clear()  # Réinitialiser l'historique
    user_role = role_description
    context_message = {
        'role': 'system',
        'content': f"Tu es un assistant spécialisé qui agit en tant que {role_description}. " \
                  f"Réponds toujours en respectant ce rôle."
    }
    messages_history.append(context_message)
    print(Fore.YELLOW + f"🔹 Contexte défini : {role_description}\n")

# Fonction pour envoyer un message à l'IA et recevoir une réponse
def send_message(message: str):
    messages_history.append({"role": "user", "content": message})
    response = chat(model="deepseek-r1", messages=messages_history)
    bot_response = clean_response(response['message']['content'])
    messages_history.append(response['message'])
    return bot_response

# Fonction principale du chatbot en mode console
def chatbot_console():
    global user_role
    print(Fore.CYAN + "💬 Bienvenue dans le Chatbot DeepSeek-R1 en mode Console !")
    print(Fore.YELLOW + "🔹 Choisissez votre expert :")
    print(Fore.GREEN + "[1] Développement (dev)  |  [2] Cybersécurité (cyber)  |  [3] Technicien Réseau (tech)  |  [4] Kali Linux / Hacking (kali)")

  # Choix du rôle de l'utilisateur
    while user_role is None:
        role_choice = input(Fore.BLUE + "🎯 Entrez votre choix (1/2/3/4 ou dev/cyber/tech/kali) : ").strip().lower()

        # Convertir l'entrée en entier si c'est un chiffre
        if role_choice.isdigit():
            role_choice = int(role_choice)

        if role_choice in ["dev", 1]:
            initialize_context("expert en développement logiciel")
        elif role_choice in ["cyber", 2]:
            initialize_context("spécialiste en cybersécurité")
        elif role_choice in ["tech", 3]:
            initialize_context("technicien réseau (serveurs, Docker, Linux, etc.)")
        elif role_choice in ["kali", "hack", 4]:
            initialize_context("spécialiste en Kali Linux et hacking avancé")
        else:
            print(Fore.RED + "❌ Choix invalide. Réessayez.")

    print(Fore.GREEN + f"✅ Mode sélectionné : {user_role}\n")

    # Boucle de chat
    while True:
        user_message = input(Fore.LIGHTBLUE_EX + "🧑‍💻 Vous : ")
        
        # Commandes spéciales
        if user_message.lower() in ["/quit", "/exit"]:
            print(Fore.RED + "\n👋 Fin de la session. À bientôt !")
            break
        elif user_message.lower() == "/clear":
            messages_history.clear()
            print(Fore.YELLOW + "🧹 Historique effacé.")
            continue
        elif user_message.lower() == "/help":
            print(Fore.YELLOW + "📜 commande possible : \n /clear : efface l'historique \n /change : changer d'expert \n /exit : quitter l'app")
            continue
        elif user_message.lower() == "/change":
            print(Fore.YELLOW + "\n🔄 Changement d'expert en cours...\n")
            user_role = None
            chatbot_console()
            return

        # Obtenir la réponse de l'IA
        print(Fore.MAGENTA + "⏳ L'IA réfléchit...\n")
        response = send_message(user_message)
        print(Fore.LIGHTGREEN_EX + f"🤖 IA ({user_role}) : {response}\n")

if __name__ == "__main__":
    chatbot_console()