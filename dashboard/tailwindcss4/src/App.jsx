import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LogCard } from './components/LogCard';
import LogAnalysisResult from './components/LogAnalysisResult';
import RecentAnomalies from './components/RecentAnomalies';
import SuggestedFixes from './components/SuggestedFixes';
import BuildStats from './components/BuildStats';

function App() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://localhost:8000/log/dashboard")
      .then((res) => setLogs(res.data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  // Filtrowanie anomalii
  const recentAnomalies = logs.filter(log => log.is_anomalous);

  // Wyciąganie unikalnych sugerowanych poprawek
  const suggestedFixes = [...new Set(logs.filter(log => log.patch).map(log => log.patch))];

  // Dummy data dla statystyk buildów
  const buildStatsData = [
    { id: '#123', status: 'Sukces', duration: '5m 30s', startedAt: '2025-04-20 20:00:00' },
    { id: '#124', status: 'Niepowodzenie', duration: '2m 15s', startedAt: '2025-04-20 20:10:00' },
    { id: '#125', status: 'Sukces', duration: '6m 0s', startedAt: '2025-04-20 20:25:00' },
    { id: '#126', status: 'W trakcie', duration: '1m 45s', startedAt: '2025-04-20 20:35:00' },
    { id: '#127', status: 'Sukces', duration: '4m 20s', startedAt: '2025-04-20 20:40:00' },
  ];

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">
        🛠️ DevOps Anomaly Dashboard
      </h1>
      {loading && <p className="text-gray-600">Ładowanie logów…</p>}
      {!loading && logs.length === 0 && (
        <p className="text-gray-500">Brak wpisów w logach.</p>
      )}

      {!loading && logs.length > 0 && (
        <>
          <LogAnalysisResult logs={logs} />
          <div className="my-8 border-t border-gray-300" />
          <RecentAnomalies anomalies={recentAnomalies} />
          <div className="my-8 border-t border-gray-300" />
          <SuggestedFixes fixes={suggestedFixes} />
          <div className="my-8 border-t border-gray-300" />
          <BuildStats stats={buildStatsData} />
        </>
      )}
    </div>
  );
}

export default App;