import tkinter as tk
import customtkinter as ctk
import ollama
import re 
import threading  # Pour exécuter l'IA sans bloquer l'interface

# Configuration de l'apparence
ctk.set_appearance_mode("dark")  # Mode sombre

# Fenêtre principale
window = ctk.CTk()
window.title("Chatbot IDE - DeepSeek-R1")
window.geometry("800x600")

# Couleurs personnalisées pour le thème mauve sombre
BG_COLOR = "#2A003F"  # Fond principal (Mauve foncé)
TEXT_COLOR = "#D4A5FF"  # Texte principal (Lilas clair)
BUTTON_COLOR = "#6A0DAD"  # Mauve profond pour les boutons
INPUT_BG = "#3B005A"  # Fond de l'éditeur de texte
TERMINAL_BG = "#1F0033"  # Fond de la zone de sortie

# Historique des messages et contexte initial
messages_history = []
user_role = None  # Spécialisation à choisir
loading_label = None  # Référence pour l'affichage de chargement

# Fonction pour nettoyer la réponse de l'IA (suppression de <think> et contenu)
def clean_response(response_text):
    cleaned_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)  # Supprime tout entre <think>...</think>
    return cleaned_text.strip()  # Supprime les espaces inutiles

# Fonction pour afficher une barre de chargement
def show_loading():
    global loading_label
    loading_label = ctk.CTkLabel(window, text="⏳ L'IA réfléchit...", fg_color="transparent", text_color="white")
    loading_label.pack()
    window.update_idletasks()

# Fonction pour cacher la barre de chargement
def hide_loading():
    global loading_label
    if loading_label:
        loading_label.pack_forget()
        loading_label = None

# Fonction pour initialiser le contexte du chatbot
def initialize_context(role_description: str):
    """
    Initialise le contexte du chatbot avec un rôle spécifique.
    """
    global user_role
    messages_history.clear()  # Réinitialise l'historique
    user_role = role_description  # Stocke le rôle choisi
    context_message = {
        'role': 'system',
        'content': f"Tu es un assistant spécialisé en {role_description}. Réponds toujours en respectant ce rôle."
    }
    messages_history.append(context_message)
    chat_display.insert(tk.END, f"\n🔹 Contexte défini : {role_description}\n", "info")
    chat_display.see(tk.END)

# Fonction pour exécuter l'IA en arrière-plan
def send_message():
    global user_role
    user_message = text_editor.get("1.0", tk.END).strip()
    if not user_message:
        return

    # Vérifie si c'est le premier message et demande le rôle
    if user_role is None:
        if "dev" in user_message.lower():
            initialize_context("expert en développement logiciel")
        elif "cyber" in user_message.lower():
            initialize_context("spécialiste en cybersécurité")
        else:
            chat_display.insert(tk.END, "\n❌ Veuillez choisir : 'dev' pour développement ou 'cyber' pour cybersécurité.\n", "error")
            chat_display.see(tk.END)
            text_editor.delete("1.0", tk.END)
            return

    # Ajoute le message utilisateur à l'historique
    chat_display.insert(tk.END, f"\n🧑‍💻 Vous :\n{user_message}\n", "user")
    chat_display.see(tk.END)
    messages_history.append({"role": "user", "content": user_message})

    # Afficher la barre de chargement
    show_loading()

    # Exécuter l'IA en arrière-plan pour éviter le blocage de l'UI
    def process_ai():
        response = ollama.chat(model="deepseek-r1", messages=messages_history)
        bot_response = clean_response(response['message']['content'])

        # Supprimer la barre de chargement
        hide_loading()

        # Afficher la réponse de l'IA
        chat_display.insert(tk.END, f"\n🤖 IA ({user_role}) :\n{bot_response}\n", "bot")
        chat_display.see(tk.END)
        messages_history.append(response['message'])

        # Effacer l'entrée utilisateur après envoi
        text_editor.delete("1.0", tk.END)

    threading.Thread(target=process_ai, daemon=True).start()  # Thread pour éviter de bloquer l'interface

# Appliquer le fond personnalisé à la fenêtre principale
window.configure(bg=BG_COLOR)

# Zone de texte type IDE pour saisir les messages
text_editor = ctk.CTkTextbox(
    window, width=780, height=100, wrap="word", font=("Consolas", 12), fg_color=INPUT_BG, text_color=TEXT_COLOR
)
text_editor.pack(pady=10, padx=10)

# Bouton d'envoi
send_button = ctk.CTkButton(
    window, text="Exécuter", command=send_message, fg_color=BUTTON_COLOR, text_color="white"
)
send_button.pack(pady=5)

# Zone d'affichage des messages (Terminal de sortie)
chat_display = ctk.CTkTextbox(
    window, width=780, height=400, wrap="word", font=("Courier", 12), fg_color=TERMINAL_BG, text_color=TEXT_COLOR
)
chat_display.pack(pady=10, padx=10)
chat_display.insert(tk.END, "💬 Bienvenue dans le Chatbot IDE DeepSeek-R1 !\n Tapez 'dev' pour un expert en développement ou 'cyber' pour un spécialiste en cybersécurité.\n\n")
chat_display.tag_config("user", foreground="#FF9CEE")  # Rose clair pour l'utilisateur
chat_display.tag_config("bot", foreground="#A370F7")  # Violet clair pour l'IA
chat_display.tag_config("info", foreground="#FFD700")  # Jaune pour les infos
chat_display.tag_config("error", foreground="red")  # Rouge pour erreurs

# Lancer l'interface
window.mainloop()
