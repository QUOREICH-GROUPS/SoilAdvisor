import React from 'react'

const Header: React.FC = () => {
  const handleLogout = () => {
    localStorage.removeItem('token')
    window.location.reload()
  }

  return (
    <header className="bg-white shadow-soft border-b border-neutral-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-700 rounded-2xl flex items-center justify-center text-white font-bold text-lg shadow-medium animate-bounce-subtle">
            🌱
          </div>
          <div>
            <h1 className="text-xl font-bold text-neutral-900">Soil Advisor</h1>
            <p className="text-sm text-neutral-600">Intelligence agricole avancée</p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <div className="hidden md:flex items-center gap-2 text-sm text-neutral-600">
            <div className="w-2 h-2 bg-success rounded-full animate-pulse-slow"></div>
            <span>Système opérationnel</span>
          </div>

          <button
            onClick={handleLogout}
            className="btn-outline text-sm px-3 py-2 hover:bg-error hover:text-white hover:border-error transition-all duration-200"
          >
            <span className="hidden sm:inline">Se déconnecter</span>
            <span className="sm:hidden">🚪</span>
          </button>
        </div>
      </div>
    </header>
  )
}

export default Header
