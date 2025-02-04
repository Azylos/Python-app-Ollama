# 🚀 Projet IA - Utilisation de Ollama avec DeepSeek-R1  

## 🎯 Objectif  
Ce projet a pour but d'utiliser **Ollama** pour exécuter un modèle de langage localement. Développement d'une application Python qui interagit avec **DeepSeek-R1**, avec la possibilité de choisir entre trois types d'interfaces pour votre application finale.

***

## 🛠️ Prérequis  
Avant de commencer, assurez-vous d’avoir :  
- **Python 3.8+** installé  
- **Ollama** installé ([Télécharger](https://ollama.com/download))  
- **DeepSeek-R1** téléchargé 

📌 **Installer la librairie `ollama-python`** :  
```bash
pip install ollama
```

***

## Types d'Interfaces Disponibles

### 1. Application Console
Créez une application console interactive avec un contexte spécifique :

- Choisissez un rôle spécialisé pour votre chatbot (ex: expert Python, spécialiste cybersécurité, coach agile...)
- Interaction en mode conversation avec historique
- Commandes spéciales (ex: /help, /clear pour effacer l'historique, /model pour changer de modèle)
- Affichage coloré des messages pour distinguer l'utilisateur et l'assistant

📌 **Dépendances suggérées `pour les couleurs dans la console`** :  
```bash
pip install colorama
```

***

### 2. Interface Graphique
Développez une interface graphique personnalisée avec Tkinter :

- Interface adaptée au contexte choisi (ex: interface type IDE pour un assistant programmation, interface sécurisée pour un expert cybersécurité)
- Zone de chat scrollable avec mise en forme adaptée au contexte
- Champ de saisie avec autocomplétion des commandes
- Menu de configuration pour changer le modèle et le rôle de l'assistant

📌 **Dépendances supplémentaires** :  
```bash
pip pip install tk customtkinter
```

***

### 3. Application Web
Créez une application web moderne avec Flask :

- Interface web responsive adaptée au contexte choisi (ex: terminal pour assistant DevOps, interface médicale pour assistant santé)
- API REST avec endpoints spécialisés selon le contexte
- Système de sessions pour gérer plusieurs conversations
- Support du streaming des réponses pour une expérience plus fluide
- Possibilité de sauvegarder et charger des conversations

📌 **Dépendances supplémentaires** :  
```bash
pip install flask flask-cors flask-socketio
```

***
## Types d'Interfaces choisi

- Choix de l'interface graphique

***

## 🚀 Lancer le modèle  
Exécutez la commande suivante pour démarrer le modèle DeepSeek-R1 :  

```bash
ollama run deepseek-r1
```