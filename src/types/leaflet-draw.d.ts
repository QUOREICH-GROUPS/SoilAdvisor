import 'leaflet'
import 'leaflet-draw'

declare module 'leaflet' {
  namespace Control {
    class Draw extends Control {
      constructor(options?: DrawConstructorOptions)
    }
  }

  namespace Draw {
    namespace Event {
      const CREATED: string
      const EDITED: string
      const DELETED: string
      const DRAWSTART: string
      const DRAWSTOP: string
      const DRAWVERTEX: string
      const EDITSTART: string
      const EDITMOVE: string
      const EDITRESIZE: string
      const EDITVERTEX: string
      const EDITSTOP: string
      const DELETESTART: string
      const DELETESTOP: string
    }
  }

  interface DrawConstructorOptions {
    position?: ControlPosition
    draw?: DrawOptions
    edit?: EditOptions
  }

  interface DrawOptions {
    polyline?: any
    polygon?: any
    rectangle?: any
    circle?: any
    marker?: any
    circlemarker?: any
  }

  interface EditOptions {
    featureGroup: FeatureGroup
    edit?: any
    remove?: any
  }
}
