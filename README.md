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

AI Engine API pour les recommandations

✨ Objectif de la partie Backend

Centraliser et sécuriser la gestion des données spatiales,
et servir de passerelle entre la base, le frontend et le moteur IA.
