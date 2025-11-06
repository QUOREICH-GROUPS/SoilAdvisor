import React from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts'
import ExportTools from '../components/ExportTools'

const ndviData = [
  { date: '2025-07-01', ndvi: 0.45 },
  { date: '2025-08-01', ndvi: 0.52 },
  { date: '2025-09-01', ndvi: 0.62 },
  { date: '2025-10-01', ndvi: 0.55 }
]

const sampleData = {
  parcelles: [
    { name: 'Parcelle 1', ndvi: 0.72, ph: 6.4, N: 1.2, P: 0.9, K: 0.8 },
    { name: 'Parcelle 2', ndvi: 0.39, ph: 5.8, N: 0.6, P: 0.4, K: 0.5 }
  ]
}

const Dashboard: React.FC = () => {
  return (
    <div className="space-y-8 fade-in">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h2 className="text-3xl font-bold text-neutral-900 mb-2">Tableau de bord</h2>
          <p className="text-neutral-600">Vue d'ensemble de vos indicateurs agricoles</p>
        </div>
        <ExportTools data={sampleData} />
      </div>

      {/* Indicateurs clés */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="stat-card group card-hover-lift slide-up" style={{ animationDelay: '0s' }}>
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-primary-100 rounded-xl float">
              <span className="text-2xl">🌱</span>
            </div>
            <div className="text-right">
              <p className="text-sm text-neutral-600">pH moyen</p>
              <p className="text-2xl font-bold text-primary-600">6.1</p>
            </div>
          </div>
          <div className="w-full bg-neutral-200 rounded-full h-2">
            <div className="bg-primary-500 h-2 rounded-full animate-shimmer" style={{width: '61%'}}></div>
          </div>
        </div>

        <div className="stat-card group card-hover-lift slide-up" style={{ animationDelay: '0.1s' }}>
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-secondary-100 rounded-xl float">
              <span className="text-2xl">📈</span>
            </div>
            <div className="text-right">
              <p className="text-sm text-neutral-600">NDVI moyen</p>
              <p className="text-2xl font-bold text-secondary-600">0.58</p>
            </div>
          </div>
          <div className="w-full bg-neutral-200 rounded-full h-2">
            <div className="bg-secondary-500 h-2 rounded-full animate-shimmer" style={{width: '58%'}}></div>
          </div>
        </div>

        <div className="stat-card group card-hover-lift slide-up" style={{ animationDelay: '0.2s' }}>
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-accent-100 rounded-xl float">
              <span className="text-2xl">💧</span>
            </div>
            <div className="text-right">
              <p className="text-sm text-neutral-600">Humidité</p>
              <p className="text-2xl font-bold text-accent-600">23%</p>
            </div>
          </div>
          <div className="w-full bg-neutral-200 rounded-full h-2">
            <div className="bg-accent-500 h-2 rounded-full animate-shimmer" style={{width: '23%'}}></div>
          </div>
        </div>
      </div>

      {/* Graphiques */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="p-2 bg-primary-100 rounded-lg">
              <span className="text-xl">📊</span>
            </div>
            <div>
              <h3 className="text-lg font-semibold text-neutral-900">Évolution NDVI</h3>
              <p className="text-sm text-neutral-600">Tendance de la végétation</p>
            </div>
          </div>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={ndviData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#e5e5e5" />
              <XAxis
                dataKey="date"
                stroke="#737373"
                fontSize={12}
                tickFormatter={(value) => new Date(value).toLocaleDateString('fr-FR', { month: 'short' })}
              />
              <YAxis stroke="#737373" fontSize={12} />
              <Tooltip
                contentStyle={{
                  backgroundColor: 'white',
                  border: 'none',
                  borderRadius: '12px',
                  boxShadow: '0 4px 25px -5px rgba(0, 0, 0, 0.1)'
                }}
              />
              <Line
                type="monotone"
                dataKey="ndvi"
                stroke="#22c55e"
                strokeWidth={3}
                dot={{ fill: '#22c55e', strokeWidth: 2, r: 4 }}
                activeDot={{ r: 6, stroke: '#22c55e', strokeWidth: 2 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="card p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="p-2 bg-secondary-100 rounded-lg">
              <span className="text-xl">🧪</span>
            </div>
            <div>
              <h3 className="text-lg font-semibold text-neutral-900">Composition NPK</h3>
              <p className="text-sm text-neutral-600">Nutriments principaux</p>
            </div>
          </div>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={[{name:'Azote (N)', value:1.2, color:'#22c55e'},{name:'Phosphore (P)', value:0.9, color:'#eab308'},{name:'Potassium (K)', value:0.8, color:'#3b82f6'}]}>
              <CartesianGrid strokeDasharray="3 3" stroke="#e5e5e5" />
              <XAxis dataKey="name" stroke="#737373" fontSize={12} />
              <YAxis stroke="#737373" fontSize={12} />
              <Tooltip
                contentStyle={{
                  backgroundColor: 'white',
                  border: 'none',
                  borderRadius: '12px',
                  boxShadow: '0 4px 25px -5px rgba(0, 0, 0, 0.1)'
                }}
              />
              <Bar dataKey="value" radius={[4, 4, 0, 0]} fill="#22c55e" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Recommandations */}
      <div className="card p-6">
        <div className="flex items-center gap-3 mb-6">
          <div className="p-2 bg-accent-100 rounded-lg">
            <span className="text-xl">💡</span>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-neutral-900">Recommandations IA</h3>
            <p className="text-sm text-neutral-600">Conseils personnalisés basés sur vos données</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="p-4 bg-primary-50 rounded-xl border border-primary-200">
            <div className="flex items-start gap-3">
              <span className="text-2xl">🌱</span>
              <div>
                <h4 className="font-semibold text-primary-900 mb-1">Fertilisation recommandée</h4>
                <p className="text-sm text-primary-700">
                  Augmentez l'apport en azote sur la Parcelle 2 où le NDVI est faible.
                </p>
              </div>
            </div>
          </div>

          <div className="p-4 bg-secondary-50 rounded-xl border border-secondary-200">
            <div className="flex items-start gap-3">
              <span className="text-2xl">💧</span>
              <div>
                <h4 className="font-semibold text-secondary-900 mb-1">Irrigation optimisée</h4>
                <p className="text-sm text-secondary-700">
                  L'humidité moyenne est basse. Planifiez un arrosage cette semaine.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
