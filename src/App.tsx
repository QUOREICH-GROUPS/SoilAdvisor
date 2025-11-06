import React from 'react'
import { Routes, Route, Link, Navigate } from 'react-router-dom'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import Dashboard from './pages/Dashboard'
import MapPage from './pages/MapPage'
import ChatPage from './pages/ChatPage'
import AnalysesPage from './pages/AnalysesPage'
import Login from './pages/Login'

const App: React.FC = () => {
  const token = localStorage.getItem('token')

  if (!token) {
    return <Login />
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <div className="flex flex-1">
        <Sidebar />
        <main className="flex-1 p-6 bg-gray-50">
          <Routes>
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/map" element={<MapPage />} />
            <Route path="/chat" element={<ChatPage />} />
            <Route path="/analyses" element={<AnalysesPage />} />
          </Routes>
        </main>
      </div>
    </div>
  )
}

export default App
