import React from 'react'
import { NavLink } from 'react-router-dom'

const Sidebar: React.FC = () => {
  const linkClass = (isActive: boolean) =>
    `group flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 ${
      isActive
        ? 'bg-primary-500 text-white shadow-medium'
        : 'text-neutral-700 hover:bg-primary-50 hover:text-primary-700'
    }`

  const navItems = [
    { to: '/dashboard', label: 'Tableau de bord', icon: '📊' },
    { to: '/map', label: 'Carte', icon: '🗺️' },
    { to: '/analyses', label: 'Analyses', icon: '📈' },
    { to: '/chat', label: 'Conseils IA', icon: '🤖' },
  ]

  return (
    <aside className="w-72 bg-white border-r border-neutral-200 shadow-soft">
      <nav className="p-6 space-y-2">
        <div className="mb-8">
          <h2 className="text-lg font-bold text-neutral-900 mb-2">Navigation</h2>
          <p className="text-sm text-neutral-600">Accédez à vos outils</p>
        </div>

        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/dashboard'}
            className={({isActive}) => linkClass(isActive)}
          >
            <span className="text-lg">{item.icon}</span>
            <span>{item.label}</span>
            <span className="ml-auto opacity-0 group-hover:opacity-100 transition-opacity duration-200">
              →
            </span>
          </NavLink>
        ))}

        <div className="mt-8 pt-6 border-t border-neutral-200">
          <div className="px-4 py-3 bg-neutral-50 rounded-xl">
            <h3 className="text-sm font-semibold text-neutral-900 mb-1">💡 Conseil</h3>
            <p className="text-xs text-neutral-600">
              Dessinez une parcelle sur la carte pour obtenir des recommandations personnalisées.
            </p>
          </div>
        </div>
      </nav>
    </aside>
  )
}

export default Sidebar
