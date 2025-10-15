🧩 1️⃣ FRONTEND — frontend/README.md
# 🌿 AgriSense Frontend — Interface Utilisateur Interactive

## 🎯 Objectif
Développer une interface moderne, intuitive et responsive pour permettre aux agriculteurs et techniciens de :
- Visualiser les parcelles agricoles sur carte interactive
- Délimiter, annoter et extraire les informations de sol (chimique, physique)
- Suivre les recommandations et indicateurs générés par l’IA

---

## ⚙️ Stack Technique
- **React.js + TypeScript**
- **TailwindCSS** pour le style moderne
- **Leaflet.js / MapLibre GL** pour la cartographie
- **Axios** pour les appels API
- **Vite** pour le build rapide
- **Recharts / Chart.js** pour les indicateurs graphiques

---

## 📁 Structure du projet


src/
├── components/ # UI réutilisables (boutons, cartes, graphiques)
├── pages/ # Écrans principaux (Dashboard, Carte, Profil)
├── hooks/ # Hooks personnalisés (useMap, useAuth)
├── services/ # Appels API vers backend et IA
├── types/ # Définition des types TS
├── App.tsx # Point d’entrée React
└── main.tsx


---

## 🧭 Fonctionnalités principales

### 🗺️ Carte interactive (Leaflet / MapLibre)
- Délimitation de zones (dessin polygonal)
- Plot de points (capteurs, échantillons)
- Extraction d’informations : composition chimique et physique
- Affichage des couches NDVI / EVI / historique météo

### 📊 Tableau de bord
- Indicateurs dynamiques (rendement, humidité, anomalies)
- Recommandations exportables en PDF
- Historique des analyses par parcelle

### 💬 Module Chat / LLM
- Interaction directe avec le moteur IA via chat
- Réponses personnalisées selon les données de la parcelle sélectionnée

---

## 🔧 Commandes utiles
```bash
# Installation
npm install

# Lancer en mode développement
npm run dev

# Build production
npm run build

🔗 API Connexions

Backend (FastAPI) → http://localhost:8000/api

AI Engine (vLLM / FastAPI) → http://localhost:8500

📦 Bonnes pratiques

Utiliser TypeScript strict ("strict": true)

Organiser le code en composants atomiques

Garder la carte comme composant central (<MapView />)

Séparer logique et UI

✨ Objectif de la partie Frontend

Fournir une expérience fluide, claire et réactive
pour explorer les données spatiales et suivre les recommandations IA.
