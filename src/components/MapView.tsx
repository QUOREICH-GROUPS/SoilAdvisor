import React, { useState, useEffect } from 'react'
import { MapContainer, TileLayer, GeoJSON, ImageOverlay } from 'react-leaflet'
import L from 'leaflet'
import DrawControl from './DrawControl'
import 'leaflet/dist/leaflet.css'

function style(feature: any) {
  const ndvi = feature.properties?.ndvi ?? 0
  const color = ndvi > 0.6 ? '#2ecc71' : ndvi > 0.3 ? '#f1c40f' : '#e74c3c'
  return {
    color,
    weight: 2,
    fillOpacity: 0.35
  }
}

const onEachFeature = (feature: any, layer: L.Layer) => {
  const p = feature.properties
  const html: string = `<div class="">
    <strong>${p.name}</strong><br/>
    NDVI: ${p.ndvi}<br/>
    pH: ${p.ph}<br/>
    N: ${p.N}, P: ${p.P}, K: ${p.K}
  </div>`

  if ('bindPopup' in layer) {
    (layer as any).bindPopup(html)
  }
}

interface ParcelStats {
  area: number
  ndvi: number
  ph: number
  N: number
  P: number
  K: number
  humidity: number
  texture: string
}

const MapView: React.FC = () => {
  const center: [number, number] = [48.862, 2.345]
  const [drawnParcel, setDrawnParcel] = useState<ParcelStats | null>(null)
  const [plots, setPlots] = useState<any>(null) // Ajout de l'état
  
  // Chargement du GeoJSON
  useEffect(() => {
    fetch('/plots.geojson')
      .then(response => response.json())
      .then(data => setPlots(data))
      .catch(error => console.error('Erreur chargement GeoJSON:', error))
  }, [])

  const ndviBounds: L.LatLngBoundsExpression = [
    [48.855, 2.335],
    [48.870, 2.355]
  ]

  const handleDrawCreated = (layer: L.Layer) => {
    const geoJSON = (layer as any).toGeoJSON()
    
    let area = 0
    if ('getLatLngs' in layer) {
      const latlngs = (layer as any).getLatLngs()[0]
      if (latlngs && latlngs.length > 0) {
        area = Math.abs(latlngs.reduce((acc: number, point: L.LatLng, i: number, arr: L.LatLng[]) => {
          const next = arr[(i + 1) % arr.length]
          return acc + (next.lng - point.lng) * (next.lat + point.lat)
        }, 0)) * 111000 * 111000 / 2
      }
    }

    const stats: ParcelStats = {
      area: Math.round(area),
      ndvi: 0.45 + Math.random() * 0.3,
      ph: 5.5 + Math.random() * 1.5,
      N: 0.5 + Math.random() * 1.0,
      P: 0.3 + Math.random() * 0.8,
      K: 0.4 + Math.random() * 0.6,
      humidity: 15 + Math.random() * 20,
      texture: ['Argileuse', 'Sableuse', 'Limoneuse'][Math.floor(Math.random() * 3)]
    }

    setDrawnParcel(stats)
  }

  return (
    <div className="flex gap-4">
      <div className="flex-1 h-[600px] rounded shadow overflow-hidden">
        <MapContainer center={center} zoom={14} style={{ height: '100%', width: '100%' }}>
          <TileLayer
            attribution='&copy; OpenStreetMap contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          
          <ImageOverlay
            url="https://via.placeholder.com/800x600/2ecc71/ffffff?text=NDVI+Overlay"
            bounds={ndviBounds}
            opacity={0.3}
          />

          {plots && <GeoJSON data={plots} style={style} onEachFeature={onEachFeature} />}
          <DrawControl onDrawCreated={handleDrawCreated} />
        </MapContainer>
      </div>

      {drawnParcel && (
        <div className="w-80 bg-white p-4 rounded shadow space-y-3">
          <h3 className="text-lg font-semibold border-b pb-2">Parcelle dessinée</h3>
          
          <div className="space-y-2 text-sm">
            <div className="flex justify-between">
              <span className="text-gray-600">Surface:</span>
              <span className="font-medium">{drawnParcel.area} m²</span>
            </div>
            
            <div className="border-t pt-2 mt-2">
              <h4 className="font-medium mb-1">Indicateurs de végétation</h4>
              <div className="flex justify-between">
                <span className="text-gray-600">NDVI moyen:</span>
                <span className="font-medium">{drawnParcel.ndvi.toFixed(2)}</span>
              </div>
            </div>

            <div className="border-t pt-2 mt-2">
              <h4 className="font-medium mb-1">Composition chimique</h4>
              <div className="space-y-1">
                <div className="flex justify-between">
                  <span className="text-gray-600">pH:</span>
                  <span className="font-medium">{drawnParcel.ph.toFixed(1)}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Azote (N):</span>
                  <span className="font-medium">{drawnParcel.N.toFixed(2)} %</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Phosphore (P):</span>
                  <span className="font-medium">{drawnParcel.P.toFixed(2)} %</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Potassium (K):</span>
                  <span className="font-medium">{drawnParcel.K.toFixed(2)} %</span>
                </div>
              </div>
            </div>

            <div className="border-t pt-2 mt-2">
              <h4 className="font-medium mb-1">Composition physique</h4>
              <div className="space-y-1">
                <div className="flex justify-between">
                  <span className="text-gray-600">Humidité:</span>
                  <span className="font-medium">{drawnParcel.humidity.toFixed(1)} %</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Texture:</span>
                  <span className="font-medium">{drawnParcel.texture}</span>
                </div>
              </div>
            </div>

            <div className="border-t pt-2 mt-2">
              <h4 className="font-medium mb-2">Recommandations</h4>
              <div className="bg-green-50 p-2 rounded text-xs">
                {drawnParcel.ndvi < 0.4 ? (
                  <p>⚠️ NDVI faible. Recommandation: apport d'engrais azoté et irrigation.</p>
                ) : drawnParcel.ndvi < 0.6 ? (
                  <p>✓ NDVI modéré. Surveillance recommandée.</p>
                ) : (
                  <p>✓ NDVI élevé. Parcelle en bonne santé.</p>
                )}
                {drawnParcel.ph < 6.0 && (
                  <p className="mt-1">⚠️ pH acide. Chaulage recommandé.</p>
                )}
              </div>
            </div>

            <button
              onClick={() => setDrawnParcel(null)}
              className="w-full mt-3 px-3 py-2 bg-gray-200 text-gray-700 rounded text-sm hover:bg-gray-300"
            >
              Fermer
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default MapView