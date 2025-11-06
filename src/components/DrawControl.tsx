import { useEffect } from 'react'
import { useMap } from 'react-leaflet'
import L from 'leaflet'
import 'leaflet-draw'

interface DrawControlProps {
  onDrawCreated: (layer: L.Layer) => void
}

const DrawControl: React.FC<DrawControlProps> = ({ onDrawCreated }) => {
  const map = useMap()

  useEffect(() => {
    const drawnItems = new L.FeatureGroup()
    map.addLayer(drawnItems)

    const drawControl = new L.Control.Draw({
      edit: {
        featureGroup: drawnItems
      },
      draw: {
        polygon: true,
        rectangle: true,
        circle: false,
        marker: false,
        circlemarker: false,
        polyline: false
      }
    })

    map.addControl(drawControl)

    const onCreate = (e: any) => {
      const layer = e.layer
      drawnItems.addLayer(layer)
      onDrawCreated(layer)
    }

    map.on(L.Draw.Event.CREATED, onCreate)

    return () => {
      map.off(L.Draw.Event.CREATED, onCreate)
      map.removeControl(drawControl)
      map.removeLayer(drawnItems)
    }
  }, [map, onDrawCreated])

  return null
}

export default DrawControl
