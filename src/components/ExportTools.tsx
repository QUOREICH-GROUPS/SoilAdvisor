import React from 'react'

interface ExportData {
  parcelles: Array<{
    name: string
    ndvi: number
    ph: number
    N: number
    P: number
    K: number
  }>
}

const ExportTools: React.FC<{ data: ExportData }> = ({ data }) => {
  const exportToCSV = () => {
    const headers = ['Parcelle', 'NDVI', 'pH', 'N (%)', 'P (%)', 'K (%)']
    const rows = data.parcelles.map(p => [p.name, p.ndvi, p.ph, p.N, p.P, p.K])
    
    let csv = headers.join(',') + '\n'
    rows.forEach(row => {
      csv += row.join(',') + '\n'
    })

    const blob = new Blob([csv], { type: 'text/csv' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `soil-advisor-export-${Date.now()}.csv`
    a.click()
    window.URL.revokeObjectURL(url)
  }

  const exportToPDF = () => {
    // Placeholder for PDF export
    // In production, use libraries like jsPDF or pdfmake
    alert('Export PDF sera implémenté avec jsPDF ou pdfmake. Pour l\'instant, utilisez l\'export CSV ou l\'impression du navigateur.')
  }

  return (
    <div className="flex gap-2">
      <button
        onClick={exportToCSV}
        className="px-4 py-2 bg-blue-600 text-white rounded text-sm hover:bg-blue-700"
      >
        📊 Exporter CSV
      </button>
      <button
        onClick={exportToPDF}
        className="px-4 py-2 bg-red-600 text-white rounded text-sm hover:bg-red-700"
      >
        📄 Exporter PDF
      </button>
    </div>
  )
}

export default ExportTools
