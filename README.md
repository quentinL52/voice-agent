# 🎙️ Voice Agent

**Un agent conversationnel vocal multilingue propulsé par les LLMs et LangChain.**

Ce projet implémente un assistant vocal de bout en bout qui permet des interactions naturelles à la voix. Basé sur le framework LangChain et utilisant le modèle Llama 3, il intègre des API performantes pour la reconnaissance vocale, la génération de texte et la synthèse vocale.

## 🚀 Fonctionnalités

* **Interaction vocale fluide :** Enregistrement de la voix, transcription automatique, traitement par le LLM et réponse vocale instantanée.
* **Support Multilingue :** Capable de comprendre et de converser dans plusieurs langues de manière transparente (notamment français, anglais, et portugais).
* **Modèle LLM ultra-rapide :** Utilisation de **Llama 3** via l'API Groq pour des temps de réponse quasi-instantanés.
* **Synthèse vocale de haute qualité :** Intégration d'**ElevenLabs** pour des voix naturelles et expressives.
* **Prompting modulable :** Utilisation d'un fichier `system_prompt.txt` séparé pour adapter facilement la personnalité ou le rôle de l'agent sans toucher au code.

## 🧠 Architecture du flux (Pipeline)

Le fonctionnement de l'agent suit un pipeline asynchrone logique en 4 étapes :

1.  **Speech-to-Text (STT) :** L'audio de l'utilisateur est capturé localement (`human.mp3`), puis envoyé à l'API **Groq** (via le modèle Whisper) pour une transcription textuelle.
2.  **Traitement LLM :** Le texte transcrit est injecté dans LangChain en tant que prompt utilisateur, et combiné au `system_prompt.txt`. Le modèle **Llama 3** de Groq génère alors la réponse.
3.  **Text-to-Speech (TTS) :** La réponse textuelle générée est envoyée à l'API **ElevenLabs** pour synthétiser l'audio de la réponse de l'agent.
4.  **Restitution Audio :** Le fichier audio généré en sortie est lu automatiquement en local (via `playsound`).

## 🛠️ Prérequis

L'ensemble des API utilisées dans ce projet disposent de plans gratuits (Free Tier) permettant de faire tourner l'agent sans frais.

* Python 3.8+
* Une clé API **Groq**
* Une clé API **ElevenLabs**

## ⚙️ Installation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/quentinL52/voice-agent.git](https://github.com/quentinL52/voice-agent.git)
   cd voice-agent
