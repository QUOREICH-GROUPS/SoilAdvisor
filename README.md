# SoilAdvisor

---

## 🧠 3️⃣ AI ENGINE — `ai_engine/README.md`

```markdown
# 🤖 AgriSense AI Engine — Intelligence Artificielle & LLM

## 🎯 Objectif
Développer et déployer les modèles d’analyse, de prédiction et de recommandation IA pour les cultures agricoles.

---

## ⚙️ Stack Technique
- **Python 3.11+**
- **PyTorch / TensorFlow**
- **Scikit-learn / XGBoost**
- **GeoPandas, Rasterio, NumPy, Pandas**
- **Hugging Face Transformers**
- **LangChain + vLLM / Ollama**
- **FastAPI** (serveur d’inférence)

---

## 📁 Structure du projet
ai_engine/
├── notebooks/ # Expérimentations Jupyter
├── data/ # Données d’entraînement
├── models/ # Modèles enregistrés
├── src/
│ ├── preprocess/ # Nettoyage et formatage
│ ├── train/ # Scripts d'entraînement ML
│ ├── inference/ # Prédictions
│ └── llm/ # Fine-tuning LLM (Mistral, LLaMA)
├── api/
│ └── main.py # API FastAPI exposant les modèles
└── requirements.txt


---

## 🧭 Fonctionnalités principales

### 🌱 Machine Learning
- **Classification des sols**
- **Prédiction de rendement**
- **Détection d’anomalies / stress hydrique**
- **Segmentation d’images satellite**

### 💬 LLM Fine-tuné
- Modèle : `Mistral-7B` ou `LLaMA 3`
- Corpus : documents agricoles, rapports FAO, fiches techniques
- Fonction : interpréter et expliquer les résultats ML
- Connecté au frontend via endpoint `/chat`

### 🔗 Endpoints API
- `/predict` → exécute une prédiction (rendement, sol, NDVI)
- `/recommend` → génère une recommandation textuelle
- `/chat` → interaction utilisateur-LLM

---

## 🔧 Commandes utiles
```bash
# Créer l’environnement
python -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur IA
uvicorn api.main:app --reload --port 8500

🧠 Bonnes pratiques

Sauvegarder les modèles dans /models

Journaliser les résultats de prédiction

Utiliser GPU pour l’entraînement local si possible

Fine-tuning avec HuggingFace PEFT (efficace sur petit hardware)

✨ Objectif de la partie AI Engine

Transformer les données spatiales en connaissances exploitables,
grâce à une IA explicable et adaptée au contexte agricole.
