import React, { useState } from 'react'

const ChatPage: React.FC = () => {
  const [messages, setMessages] = useState<Array<{role:string,text:string}>>([
    { role: 'assistant', text: 'Bonjour ! Je suis votre assistant agricole IA. Posez-moi des questions sur vos parcelles, le NDVI, les recommandations de fertilisation ou d\'irrigation.' }
  ])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const send = async () => {
    if (!input.trim()) return

    const userMsg = { role: 'user', text: input }
    setMessages(m => [...m, userMsg])
    setInput('')
    setIsLoading(true)

    // Simulation d'une réponse IA
    setTimeout(() => {
      const responses = [
        "D'après les données NDVI de votre parcelle, je recommande un apport supplémentaire d'azote. Le NDVI actuel est de 0.45, ce qui indique un stress nutritionnel.",
        "Votre pH de 6.1 est optimal pour la plupart des cultures. Cependant, surveillez l'humidité qui est actuellement basse à 23%.",
        "Pour la Parcelle 2 avec un NDVI faible, je suggère une fertilisation équilibrée NPK et une irrigation immédiate pour améliorer la vigueur végétale.",
        "Les analyses montrent une bonne texture du sol argileuse. Continuez les pratiques de conservation pour maintenir cette structure favorable."
      ]

      const randomResponse = responses[Math.floor(Math.random() * responses.length)]
      setMessages(m => [...m, { role: 'assistant', text: randomResponse }])
      setIsLoading(false)
    }, 1500)
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6 fade-in">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-neutral-900 mb-2">Conseils IA Agricole</h2>
        <p className="text-neutral-600">Discutez avec l'intelligence artificielle pour obtenir des recommandations personnalisées</p>
      </div>

      {/* Zone de conversation */}
      <div className="card p-6">
        <div className="flex items-center gap-3 mb-6">
          <div className="p-3 bg-accent-100 rounded-xl">
            <span className="text-2xl">🤖</span>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-neutral-900">Assistant Agricole IA</h3>
            <p className="text-sm text-neutral-600">Analyste vos données en temps réel</p>
          </div>
        </div>

        <div className="space-y-4 mb-6 max-h-96 overflow-y-auto">
          {messages.map((m, i) => (
            <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-xs lg:max-w-md px-4 py-3 rounded-2xl ${
                m.role === 'user'
                  ? 'bg-primary-500 text-white'
                  : 'bg-neutral-100 text-neutral-900'
              }`}>
                <p className="text-sm">{m.text}</p>
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-neutral-100 px-4 py-3 rounded-2xl">
                <div className="flex items-center gap-2">
                  <div className="flex gap-1">
                    <div className="w-2 h-2 bg-neutral-400 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                    <div className="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                  </div>
                  <span className="text-sm text-neutral-600">L'IA analyse vos données...</span>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Zone de saisie */}
        <div className="flex gap-3">
          <div className="flex-1 relative">
            <textarea
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Demandez un conseil : ex. 'Quel engrais pour ma parcelle P1 ?' ou 'Mon NDVI est faible, que faire ?'"
              className="input-field resize-none"
              rows={2}
              disabled={isLoading}
            />
          </div>
          <button
            onClick={send}
            disabled={isLoading || !input.trim()}
            className="btn-primary px-6 py-3 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span className="hidden sm:inline">Envoyer</span>
            <span className="sm:hidden">📤</span>
          </button>
        </div>
      </div>

      {/* Suggestions rapides */}
      <div className="card p-6">
        <h3 className="text-lg font-semibold text-neutral-900 mb-4">Questions suggérées</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {[
            "Quel engrais appliquer sur ma parcelle P1 ?",
            "Mon NDVI est faible, que dois-je faire ?",
            "Quand irriguer mes cultures ?",
            "Comment améliorer la texture de mon sol ?"
          ].map((question, index) => (
            <button
              key={index}
              onClick={() => setInput(question)}
              className="text-left p-3 bg-neutral-50 hover:bg-primary-50 rounded-xl border border-neutral-200 hover:border-primary-200 transition-all duration-200"
            >
              <span className="text-sm text-neutral-700">{question}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}

export default ChatPage
