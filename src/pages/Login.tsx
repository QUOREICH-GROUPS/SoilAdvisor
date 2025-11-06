import React, { useState } from 'react'

const Login: React.FC = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)

    // Simulation d'une connexion
    setTimeout(() => {
      if (username && password) {
        localStorage.setItem('token', 'fake-jwt-token')
        window.location.reload()
      }
      setIsLoading(false)
    }, 1000)
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 via-white to-accent-50">
      <div className="absolute inset-0 opacity-30">
        <div className="absolute inset-0 bg-gradient-to-br from-primary-100/20 to-accent-100/20"></div>
      </div>

      <div className="relative z-10 w-full max-w-md mx-4">
        <div className="card p-8 fade-in">
          <div className="text-center mb-8">
            <div className="w-20 h-20 bg-gradient-to-br from-primary-500 to-primary-700 rounded-3xl flex items-center justify-center text-white text-3xl font-bold mx-auto mb-4 shadow-large animate-bounce-subtle">
              🌱
            </div>
            <h2 className="text-2xl font-bold text-neutral-900 mb-2">Bienvenue</h2>
            <p className="text-neutral-600">Connectez-vous à votre espace agricole</p>
          </div>

          <form onSubmit={submit} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-2">
                Nom d'utilisateur
              </label>
              <input
                type="text"
                value={username}
                onChange={e => setUsername(e.target.value)}
                className="input-field"
                placeholder="Votre nom d'utilisateur"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-2">
                Mot de passe
              </label>
              <input
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                className="input-field"
                placeholder="Votre mot de passe"
                required
              />
            </div>

            <button
              type="submit"
              disabled={isLoading}
              className="w-full btn-primary py-3 text-base font-semibold disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? (
                <div className="flex items-center justify-center gap-2">
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                  Connexion en cours...
                </div>
              ) : (
                'Se connecter'
              )}
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-sm text-neutral-600">
              Démo: utilisez n'importe quel nom d'utilisateur et mot de passe
            </p>
          </div>
        </div>

        <div className="mt-8 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-white/80 backdrop-blur-sm rounded-full text-sm text-neutral-600 shadow-soft">
            <div className="w-2 h-2 bg-success rounded-full animate-pulse-slow"></div>
            Système opérationnel
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login
