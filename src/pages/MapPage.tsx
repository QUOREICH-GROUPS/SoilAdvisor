import React from 'react'
import MapView from '../components/MapView'

const MapPage: React.FC = () => {
  return (
    <div className="space-y-6 fade-in">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h2 className="text-3xl font-bold text-neutral-900 mb-2">Carte des parcelles</h2>
          <p className="text-neutral-600">
            Visualisez vos parcelles et utilisez les outils de dessin pour analyser de nouvelles zones
          </p>
        </div>

        <div className="flex flex-wrap gap-2">
          <div className="inline-flex items-center gap-2 px-3 py-2 bg-primary-100 text-primary-700 rounded-lg text-sm font-medium card-hover-lift slide-up" style={{ animationDelay: '0s' }}>
            <div className="w-3 h-3 bg-primary-500 rounded-full animate-pulse-slow"></div>
            NDVI élevé
          </div>
          <div className="inline-flex items-center gap-2 px-3 py-2 bg-secondary-100 text-secondary-700 rounded-lg text-sm font-medium card-hover-lift slide-up" style={{ animationDelay: '0.1s' }}>
            <div className="w-3 h-3 bg-secondary-500 rounded-full animate-pulse-slow"></div>
            NDVI moyen
          </div>
          <div className="inline-flex items-center gap-2 px-3 py-2 bg-error-100 text-error-700 rounded-lg text-sm font-medium card-hover-lift slide-up" style={{ animationDelay: '0.2s' }}>
            <div className="w-3 h-3 bg-error-500 rounded-full animate-pulse-slow"></div>
            NDVI faible
          </div>
        </div>
      </div>

      <div className="bg-white p-4 rounded-2xl shadow-soft border border-neutral-200">
        <div className="flex items-center gap-3 mb-4">
          <div className="p-2 bg-accent-100 rounded-lg">
            <span className="text-xl">🛠️</span>
          </div>
          <div>
            <h3 className="font-semibold text-neutral-900">Outils de dessin</h3>
            <p className="text-sm text-neutral-600">
              Cliquez sur les icônes en haut à gauche de la carte pour dessiner des polygones ou rectangles
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-sm">
          <div className="flex items-center gap-2 p-3 bg-neutral-50 rounded-lg card-hover-lift slide-up" style={{ animationDelay: '0.3s' }}>
            <span className="text-lg">🔷</span>
            <span className="text-neutral-700">Polygone personnalisé</span>
          </div>
          <div className="flex items-center gap-2 p-3 bg-neutral-50 rounded-lg card-hover-lift slide-up" style={{ animationDelay: '0.4s' }}>
            <span className="text-lg">⬜</span>
            <span className="text-neutral-700">Rectangle rapide</span>
          </div>
          <div className="flex items-center gap-2 p-3 bg-neutral-50 rounded-lg card-hover-lift slide-up" style={{ animationDelay: '0.5s' }}>
            <span className="text-lg">�</span>
            <span className="text-neutral-700">Mesurer la surface</span>
          </div>
        </div>
      </div>

      <MapView />
    </div>
  )
}

export default MapPage
