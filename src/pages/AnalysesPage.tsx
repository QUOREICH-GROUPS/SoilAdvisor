import React, { useState } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, BarChart, Bar, PieChart, Pie, Cell } from 'recharts'

const AnalysesPage: React.FC = () => {
  const [selectedPeriod, setSelectedPeriod] = useState('30j')

  // Données simulées pour les analyses
  const ndviData = [
    { date: '2024-01-01', ndvi: 0.45, parcelle: 'P1' },
    { date: '2024-01-08', ndvi: 0.52, parcelle: 'P1' },
    { date: '2024-01-15', ndvi: 0.48, parcelle: 'P1' },
    { date: '2024-01-22', ndvi: 0.61, parcelle: 'P1' },
    { date: '2024-01-29', ndvi: 0.58, parcelle: 'P1' },
    { date: '2024-02-05', ndvi: 0.65, parcelle: 'P1' },
  ]

  const soilData = [
    { parametre: 'pH', valeur: 6.1, unite: '', optimal: '6.0-7.0' },
    { parametre: 'Azote', valeur: 0.12, unite: '%', optimal: '0.10-0.15' },
    { parametre: 'Phosphore', valeur: 45, unite: 'mg/kg', optimal: '40-60' },
    { parametre: 'Potassium', valeur: 180, unite: 'mg/kg', optimal: '150-200' },
    { parametre: 'Matière organique', valeur: 3.2, unite: '%', optimal: '2.5-4.0' },
    { parametre: 'Humidité', valeur: 23, unite: '%', optimal: '20-30' },
  ]

  const recommendationsData = [
    { categorie: 'Fertilisation', count: 3, color: '#10B981' },
    { categorie: 'Irrigation', count: 2, color: '#3B82F6' },
    { categorie: 'Protection', count: 1, color: '#F59E0B' },
    { categorie: 'Travail sol', count: 1, color: '#EF4444' },
  ]

  const getStatusColor = (value: number, optimal: string) => {
    const [min, max] = optimal.split('-').map(Number)
    if (value >= min && value <= max) return 'text-green-600 bg-green-100'
    return 'text-yellow-600 bg-yellow-100'
  }

  return (
    <div className="max-w-7xl mx-auto space-y-8 fade-in">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-neutral-900 mb-2">Analyses & Recommandations</h2>
        <p className="text-neutral-600">Suivez l'évolution de vos indicateurs et recevez des conseils personnalisés</p>
      </div>

      {/* Filtres de période */}
      <div className="flex justify-center">
        <div className="bg-white rounded-xl p-1 shadow-sm border border-neutral-200">
          {['7j', '30j', '90j', '1an'].map((period) => (
            <button
              key={period}
              onClick={() => setSelectedPeriod(period)}
              className={`px-4 py-2 rounded-lg font-medium transition-all duration-200 ${
                selectedPeriod === period
                  ? 'bg-primary-500 text-white shadow-sm'
                  : 'text-neutral-600 hover:text-primary-600'
              }`}
            >
              {period === '7j' ? '7 jours' : period === '30j' ? '30 jours' : period === '90j' ? '90 jours' : '1 an'}
            </button>
          ))}
        </div>
      </div>

      {/* Graphiques NDVI */}
      <div className="card p-6">
        <div className="flex items-center gap-3 mb-6">
          <div className="p-3 bg-accent-100 rounded-xl">
            <span className="text-2xl">📈</span>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-neutral-900">Évolution du NDVI</h3>
            <p className="text-sm text-neutral-600">Indice de végétation par différence normalisée</p>
          </div>
        </div>

        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={ndviData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
              <XAxis
                dataKey="date"
                stroke="#6B7280"
                fontSize={12}
                tickFormatter={(value) => new Date(value).toLocaleDateString('fr-FR', { month: 'short', day: 'numeric' })}
              />
              <YAxis stroke="#6B7280" fontSize={12} domain={[0, 1]} />
              <Tooltip
                contentStyle={{
                  backgroundColor: 'white',
                  border: '1px solid #E5E7EB',
                  borderRadius: '8px',
                  boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
                }}
                labelFormatter={(value) => `Date: ${new Date(value).toLocaleDateString('fr-FR')}`}
                formatter={(value: number) => [`${value.toFixed(2)}`, 'NDVI']}
              />
              <Line
                type="monotone"
                dataKey="ndvi"
                stroke="#10B981"
                strokeWidth={3}
                dot={{ fill: '#10B981', strokeWidth: 2, r: 4 }}
                activeDot={{ r: 6, stroke: '#10B981', strokeWidth: 2 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Analyse du sol */}
        <div className="card p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="p-3 bg-secondary-100 rounded-xl">
              <span className="text-2xl">🧪</span>
            </div>
            <div>
              <h3 className="text-lg font-semibold text-neutral-900">Analyse du Sol</h3>
              <p className="text-sm text-neutral-600">Paramètres physico-chimiques</p>
            </div>
          </div>

          <div className="space-y-4">
            {soilData.map((param, index) => (
              <div key={index} className="flex items-center justify-between p-4 bg-neutral-50 rounded-xl">
                <div className="flex-1">
                  <div className="font-medium text-neutral-900">{param.parametre}</div>
                  <div className="text-sm text-neutral-600">Optimal: {param.optimal}</div>
                </div>
                <div className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(param.valeur, param.optimal)}`}>
                  {param.valeur}{param.unite}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Recommandations par catégorie */}
        <div className="card p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="p-3 bg-accent-100 rounded-xl">
              <span className="text-2xl">💡</span>
            </div>
            <div>
              <h3 className="text-lg font-semibold text-neutral-900">Recommandations</h3>
              <p className="text-sm text-neutral-600">Répartition par catégorie</p>
            </div>
          </div>

          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={recommendationsData}
                  cx="50%"
                  cy="50%"
                  innerRadius={40}
                  outerRadius={80}
                  paddingAngle={5}
                  dataKey="count"
                >
                  {recommendationsData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    backgroundColor: 'white',
                    border: '1px solid #E5E7EB',
                    borderRadius: '8px',
                    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>

          <div className="grid grid-cols-2 gap-3 mt-4">
            {recommendationsData.map((item, index) => (
              <div key={index} className="flex items-center gap-2">
                <div
                  className="w-3 h-3 rounded-full"
                  style={{ backgroundColor: item.color }}
                ></div>
                <span className="text-sm text-neutral-700">{item.categorie}</span>
                <span className="text-sm font-medium text-neutral-900 ml-auto">{item.count}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Recommandations détaillées */}
      <div className="card p-6">
        <div className="flex items-center gap-3 mb-6">
          <div className="p-3 bg-primary-100 rounded-xl">
            <span className="text-2xl">📋</span>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-neutral-900">Recommandations Détaillées</h3>
            <p className="text-sm text-neutral-600">Actions prioritaires pour optimiser vos parcelles</p>
          </div>
        </div>

        <div className="space-y-4">
          {[
            {
              priority: 'Haute',
              title: 'Fertilisation azotée urgente',
              description: 'Le NDVI indique un déficit en azote. Appliquez 50kg/ha d\'urée dans les 7 jours.',
              parcelle: 'P1',
              color: 'bg-red-100 text-red-800'
            },
            {
              priority: 'Moyenne',
              title: 'Irrigation préventive',
              description: 'L\'humidité du sol est basse. Programmez une irrigation de 20mm.',
              parcelle: 'P2',
              color: 'bg-yellow-100 text-yellow-800'
            },
            {
              priority: 'Basse',
              title: 'Surveillance maladies',
              description: 'Conditions météo favorables aux champignons. Inspectez régulièrement.',
              parcelle: 'Toutes',
              color: 'bg-blue-100 text-blue-800'
            }
          ].map((rec, index) => (
            <div key={index} className="flex items-start gap-4 p-4 bg-neutral-50 rounded-xl hover:bg-neutral-100 transition-colors duration-200">
              <div className={`px-3 py-1 rounded-full text-xs font-medium ${rec.color} flex-shrink-0`}>
                {rec.priority}
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <h4 className="font-medium text-neutral-900">{rec.title}</h4>
                  <span className="text-sm text-neutral-600">• {rec.parcelle}</span>
                </div>
                <p className="text-sm text-neutral-700">{rec.description}</p>
              </div>
              <button className="btn-primary text-xs px-3 py-1">
                Appliquer
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default AnalysesPage