# SoilAdvisor

## ⚙️ 2️⃣ BACKEND — `backend/README.md`

```markdown
# 🌾 AgriSense Backend — API & Données Spatiales

## 🎯 Objectif
Fournir des services backend robustes pour :
- Gérer les données importées et satellites
- Exposer les APIs pour le frontend et le moteur IA
- Centraliser les informations spatiales dans PostGIS

---

## ⚙️ Stack Technique
- **Python 3.11+**
- **FastAPI**
- **PostgreSQL + PostGIS**
- **SQLAlchemy + Alembic** (ORM & migrations)
- **GeoPandas / Rasterio / Shapely**
- **Celery + Redis** (tâches asynchrones)
- **Docker Compose**

---

## 📁 Structure du projet


app/
├── main.py # Point d’entrée API
├── routers/ # Routes : /users, /fields, /data, /analytics
├── models/ # ORM (SQLAlchemy)
├── schemas/ # Pydantic models
├── services/ # Logique métier
├── utils/ # Fonctions utilitaires (auth, géo, logs)
├── database.py # Connexion Postgres/PostGIS
└── config.py


---

## 🧭 Fonctionnalités principales

### 📥 Importation de données
- Données locales (CSV, JSON, GeoTIFF)
- Données satellites (Sentinel-2, NDVI, EVI via API)
- Météo locale (NOAA / OpenWeather)

### 🧹 Prétraitement
- Nettoyage, conversion d’unités, vérification cohérence
- Géoréférencement automatique via shapefile ou lat/long

### 🌍 Base spatiale PostGIS
Tables principales :
- `parcelles` : géométries + métadonnées
- `analyses_sol` : pH, humidité, nutriments
- `rendements_histo` : productions passées
- `satellite_data` : NDVI, EVI, indices de végétation

### 🔗 API REST
Endpoints principaux :
- `/api/parcelles`
- `/api/analyse`
- `/api/forecast`
- `/api/recommandation`

---

## 🔧 Commandes utiles
```bash
# Créer l'environnement
python -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn app.main:app --reload

🔐 Sécurité & Authentification

JWT Tokens

Rôles : Admin, Technicien, Agriculteur

CORS activé pour le frontend

🌍 Intégrations externes

SentinelHub API pour NDVI / EVI

OpenWeather API pour météo
## 🧱 Déploiement & Collaboration GitHub

### 🔧 Étapes de mise en place

1. **Créer un repo principal :**

   ```bash
   git init agrisense
   cd agrisense
   ```

2. **Ajouter les sous-projets :**

   ```bash
   git submodule add ./frontend
   git submodule add ./backend
   git submodule add ./ai_engine
   ```

3. **Chaque équipe travaille sur sa branche :**

   * `frontend-dev`
   * `backend-dev`
   * `ai-dev`

4. **Push des branches séparées :**

   ```bash
   git checkout -b frontend-dev
   git add .
   git commit -m "Frontend initial setup"
   git push origin frontend-dev
   ```

5. **Merge final dans `main` après validation :**

   ```bash
   git checkout main
   git merge frontend-dev
   git merge backend-dev
   git merge ai-dev
   ```

6. **Déploiement avec Docker Compose :**

   ```yaml
   version: '3.9'
   services:
     backend:
       build: ./backend
       ports: ["8000:8000"]
     frontend:
       build: ./frontend
       ports: ["5173:5173"]
     ai_engine:
       build: ./ai_engine
       ports: ["8500:8500"]
     db:
       image: postgis/postgis
       ports: ["5432:5432"]
       environment:
         POSTGRES_USER: admin
         POSTGRES_PASSWORD: admin
         POSTGRES_DB: agrisense
   ```

---

## 🧠 Exemple de flux complet

1. L’agriculteur se connecte au **tableau de bord**.
2. Il **sélectionne une parcelle** sur la carte.
3. Le **backend** interroge PostGIS et renvoie les données sol/météo.
4. Le **module AI** exécute une prédiction (rendement, anomalies).
5. Le **LLM** formule une recommandation textuelle (“Augmenter l’irrigation de 10%”).
6. Le **frontend** affiche les cartes et recommandations.


 

> Il relie les trois parties (Frontend, Backend, AI Engine) et présente le projet complet avec badges, schéma d’architecture, stack technique et étapes d’installation.
> Tout est open source, structuré et prêt à publier 🚀

---


```markdown
# 🌾 AgriSense — Plateforme Agricole Intelligente Open Source

[![Made with React](https://img.shields.io/badge/Frontend-React.js-blue?logo=react)](./frontend)
[![Backend FastAPI](https://img.shields.io/badge/Backend-FastAPI-green?logo=fastapi)](./backend)
[![AI Engine](https://img.shields.io/badge/AI-Engine-orange?logo=pytorch)](./ai_engine)
[![Database](https://img.shields.io/badge/Database-PostgreSQL+PostGIS-blue?logo=postgresql)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 🌍 Présentation Générale

**AgriSense** est une solution **intelligente et open source** pour la gestion agricole basée sur :
- des **données terrain** (pH, humidité, nutriments, rendement),
- des **données satellites** (NDVI, EVI, météo),
- un **moteur IA** pour la prédiction et les recommandations agricoles.

Le système permet :
1. L’analyse des sols et du rendement.
2. La cartographie interactive des parcelles.
3. Des recommandations intelligentes via un LLM fine-tuné.

---

## 🧩 Architecture Globale du Système

```

```
             +-----------------------+
             |    FRONTEND (React)   |
             |  - Carte interactive  |
             |  - Tableau de bord    |
             |  - Chat IA intégré    |
             +----------+------------+
                        |
                        v
           +------------+-------------+
           |   BACKEND (FastAPI)      |
           |  - API REST & Auth       |
           |  - PostGIS + Données     |
           |  - Prétraitement données |
           +------------+-------------+
                        |
                        v
            +-----------+------------+
            |   AI ENGINE (Python)   |
            | - ML : sol, rendement  |
            | - LLM : Mistral/LLaMA  |
            | - Recommandations IA   |
            +------------------------+
```

```

---

## 🧱 Structure du dépôt

```

agrisense/
├── frontend/       # Interface utilisateur (React + Tailwind)
├── backend/        # API FastAPI + PostgreSQL/PostGIS
├── ai_engine/      # Moteur IA et LLM fine-tuné
├── data/           # Données brutes / satellite
├── docs/           # Documentation et schémas
└── README.md       # (ce fichier)

````

---

## ⚙️ Technologies utilisées

| Catégorie         | Outils / Frameworks                            |
|-------------------|------------------------------------------------|
| **Frontend**      | React.js, TypeScript, TailwindCSS, Leaflet.js  |
| **Backend**       | Python, FastAPI, PostgreSQL, PostGIS, SQLAlchemy |
| **AI Engine**     | PyTorch, Scikit-learn, LangChain, HuggingFace, vLLM |
| **Cartographie**  | Leaflet, GeoPandas, Rasterio, MapLibre         |
| **Infrastructure**| Docker, Docker Compose, Redis, Celery          |

---

## 🪄 Installation complète

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/<ton-username>/agrisense.git
cd agrisense
````

### 2️⃣ Lancer chaque module

#### 🧭 Backend

```bash
cd backend
uvicorn app.main:app --reload
```

#### 🧠 AI Engine

```bash
cd ai_engine
uvicorn api.main:app --reload --port 8500
```

#### 💻 Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🔗 Communication entre les modules

| Module    | Port par défaut | Description                              |
| --------- | --------------- | ---------------------------------------- |
| Frontend  | 5173            | Interface utilisateur React              |
| Backend   | 8000            | API FastAPI (parcelles, analyses, météo) |
| AI Engine | 8500            | Prédictions, recommandations, LLM        |

---

## 🚀 Workflow Git Recommandé

### 1️⃣ Initialisation des dépôts séparés

```bash
git init
git remote add origin https://github.com/<username>/agrisense.git
```

### 2️⃣ Création des branches par module

```bash
git checkout -b frontend
git checkout -b backend
git checkout -b ai_engine
```

### 3️⃣ Développement séparé

Chaque responsable travaille dans sa branche :

* `frontend` → interface React
* `backend` → FastAPI + PostGIS
* `ai_engine` → modèles IA / LLM

### 4️⃣ Fusion finale

Une fois testés :

```bash
git checkout main
git merge backend
git merge ai_engine
git merge frontend
```

### 5️⃣ Pousser sur GitHub

```bash
git push origin main
```

---

## 🧠 Objectifs finaux

* Automatiser la collecte et l’analyse des données agricoles
* Fournir des conseils précis et géolocalisés
* Rendre les technologies IA accessibles aux agriculteurs africains
* 100% open source et extensible 🌍

---

## 📜 Licence

Ce projet est sous licence **MIT** — libre de modifier, redistribuer et adapter.

---

## 👨‍💻 Équipe

| Rôle                         | Responsable          | Dossier      |
| ---------------------------- | -------------------- | ------------ |
| 🎨 Interface utilisateur     | Responsable Frontend | `frontend/`  |
| 🧩 Données & API             | Responsable Backend  | `backend/`   |
| 🤖 Intelligence Artificielle | Responsable AI / ML  | `ai_engine/` |

---

## 🌟 Vision

> *"Révolutionner la productivité agricole en Afrique grâce à la donnée, l’intelligence artificielle et la cartographie interactive."*
> — Projet AgriSense 🌿

````

---

Souhaites-tu que je te crée aussi les **commandes Docker Compose** (pour lancer les 3 services ensemble automatiquement) ?  
👉 Cela permettrait de faire tourner tout le système avec un simple :  
```bash
docker compose up
````





## 🌍 Objectif final

AI Engine API pour les recommandations

✨ Objectif de la partie Backend

Centraliser et sécuriser la gestion des données spatiales,
et servir de passerelle entre la base, le frontend et le moteur IA.
