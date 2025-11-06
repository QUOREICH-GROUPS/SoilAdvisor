# Soil Advisor - Frontend

Frontend professionnel pour Soil Advisor construit avec Vite + React + TypeScript + Tailwind.

## 🎯 Fonctionnalités implémentées

### ✅ Carte interactive avec Leaflet Draw
- Affichage des parcelles existantes (GeoJSON)
- **Dessin et délimitation de nouvelles parcelles** (polygones, rectangles)
- Overlay NDVI simulé (raster semi-transparent)
- Popups interactifs affichant les données par parcelle
- **Panneau latéral automatique** avec extraction des statistiques :
  - Surface calculée
  - NDVI moyen
  - Composition chimique (pH, N, P, K)
  - Composition physique (humidité, texture)
  - Recommandations personnalisées

### 📊 Tableau de bord
- Indicateurs clés en temps réel (pH moyen, NDVI, humidité)
- Graphiques interactifs (Recharts) :
  - Évolution NDVI temporelle
  - Diagramme en barres des nutriments (N, P, K)
- **Export des données** :
  - CSV (fonctionnel)
  - PDF (placeholder pour jsPDF/pdfmake)

### 💬 Chat LLM
- Interface de conversation avec backend LLM
- Envoi de questions sur les parcelles et indicateurs
- Réponses contextualisées (placeholder endpoint `/api/chat`)

### 🔐 Authentification
- Page de connexion simple
- JWT stub (localStorage)
- Déconnexion fonctionnelle

## 🚀 Démarrage rapide

### Installation

Depuis ce dossier, installez les dépendances :

```powershell
npm install
```

### Lancement du serveur de développement

```powershell
npm run dev
```

L'application sera accessible sur **http://localhost:5173**

### Build de production

```powershell
npm run build
```

Les fichiers optimisés seront dans le dossier `dist/`.

## 📁 Structure du projet

```
frontend/
├── src/
│   ├── components/         # Composants réutilisables
│   │   ├── Header.tsx      # Entête avec logout
│   │   ├── Sidebar.tsx     # Navigation latérale
│   │   ├── MapView.tsx     # Carte Leaflet + Draw + stats panel
│   │   ├── DrawControl.tsx # Contrôle de dessin Leaflet
│   │   └── ExportTools.tsx # Export CSV/PDF
│   ├── pages/              # Pages principales
│   │   ├── Dashboard.tsx   # Tableau de bord
│   │   ├── MapPage.tsx     # Page carte
│   │   ├── ChatPage.tsx    # Chat LLM
│   │   └── Login.tsx       # Connexion
│   ├── data/
│   │   └── plots.geojson   # Données exemples parcelles
│   ├── types/
│   │   └── leaflet-draw.d.ts # Types TypeScript pour Leaflet Draw
│   ├── App.tsx             # Composant principal + routing
│   ├── main.tsx            # Point d'entrée React
│   └── styles.css          # Styles Tailwind + Leaflet
├── package.json
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.cjs
└── README.md
```

## 🔧 Configuration et intégration backend

### Connexion au backend

Pour connecter l'interface à votre backend réel :

1. **API Chat LLM** : Modifiez l'endpoint dans `src/pages/ChatPage.tsx` (ligne ~18)
   ```typescript
   const res = await fetch('http://votre-backend.com/api/chat', { ... })
   ```

2. **Données parcelles** : Remplacez `src/data/plots.geojson` par vos vraies données ou chargez-les dynamiquement via API

3. **Authentification** : Implémentez un vrai système JWT dans `src/pages/Login.tsx`

4. **Statistiques NDVI/Sol** : Dans `src/components/MapView.tsx`, remplacez les valeurs simulées (ligne ~57) par un appel API :
   ```typescript
   // Envoyer le polygon au backend pour extraction
   const response = await fetch('/api/analyze-parcel', {
     method: 'POST',
     body: JSON.stringify({ geometry: geoJSON.geometry })
   })
   const stats = await response.json()
   ```

### Overlay NDVI réel

Pour afficher des tuiles NDVI réelles au lieu du placeholder :

**Option 1 : WMS (Web Map Service)**
```typescript
<WMSTileLayer
  url="http://votre-serveur/geoserver/wms"
  layers="ndvi_layer"
  format="image/png"
  transparent={true}
  opacity={0.6}
/>
```

**Option 2 : Tuiles XYZ**
```typescript
<TileLayer
  url="http://votre-serveur/tiles/ndvi/{z}/{x}/{y}.png"
  opacity={0.6}
/>
```

## 🎨 Personnalisation du thème

Le thème est configurable via Tailwind. Modifiez `tailwind.config.cjs` :

```javascript
theme: {
  extend: {
    colors: {
      primary: '#2ecc71',    // Vert agriculture
      secondary: '#3498db',
      danger: '#e74c3c'
    }
  }
}
```

## 📦 Dépendances principales

| Package | Usage |
|---------|-------|
| `react` + `react-dom` | Framework UI |
| `react-router-dom` | Routing |
| `leaflet` + `react-leaflet` | Cartographie |
| `leaflet-draw` | Outils de dessin |
| `recharts` | Graphiques |
| `@tanstack/react-query` | Gestion requêtes API |
| `zustand` | State management |
| `tailwindcss` | Styles CSS |

## 🐛 Dépannage

### Erreurs TypeScript avec Leaflet Draw

Les types personnalisés sont dans `src/types/leaflet-draw.d.ts`. Si vous voyez des erreurs, assurez-vous que :
- `@types/leaflet` et `@types/leaflet-draw` sont installés
- `tsconfig.json` inclut le dossier `src`

### Carte ne s'affiche pas

Vérifiez que les CSS Leaflet sont bien importés dans `src/styles.css` :
```css
@import 'leaflet/dist/leaflet.css';
@import 'leaflet-draw/dist/leaflet.draw.css';
```

### Problèmes d'icônes Leaflet

Ajoutez dans `src/components/MapView.tsx` (avant le composant) :
```typescript
import icon from 'leaflet/dist/images/marker-icon.png'
import iconShadow from 'leaflet/dist/images/marker-shadow.png'

let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow
})
L.Marker.prototype.options.icon = DefaultIcon
```

## 🚀 Améliorations futures suggérées

- [ ] Implémenter export PDF avec jsPDF
- [ ] Ajouter authentification multi-utilisateurs (rôles)
- [ ] Mode hors-ligne (PWA avec service workers)
- [ ] Thème sombre/clair dynamique
- [ ] Notifications temps réel (WebSockets)
- [ ] Gestion avancée des couches (NDVI, EVI, température, humidité)
- [ ] Comparaison temporelle (slider de dates)
- [ ] Rapports automatiques périodiques

## 📝 Notes importantes

- Les données affichées sont **simulées** pour la démo
- Le calcul de surface est approximatif (non géodésique)
- L'endpoint `/api/chat` doit être implémenté côté backend
- Pour la production, ajoutez la validation des données et la gestion d'erreurs

## 📞 Support

Pour toute question sur l'intégration ou la personnalisation, consultez :
- [Documentation React-Leaflet](https://react-leaflet.js.org/)
- [Documentation Leaflet Draw](https://leaflet.github.io/Leaflet.draw/)
- [Documentation Recharts](https://recharts.org/)

---

**Version:** 1.0.0  
**Dernière mise à jour:** Novembre 2025
