import React from 'react';

function LogAnalysisResult({ logs }) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-gray-700">Wyniki Analizy Logów</h2>
      {logs.length > 0 ? (
        <div className="space-y-2">
          {logs.map((log) => (
            <div key={log.id} className="bg-white rounded-md shadow-sm p-4 border border-gray-200">
              <p><span className="font-semibold text-gray-600">Timestamp:</span> {new Date(log.timestamp).toLocaleString()}</p>
              <p><span className="font-semibold text-gray-600">Błąd:</span> <span className={log.is_anomalous ? 'text-red-500' : 'text-gray-700'}>{log.error}</span></p>
              {log.patch && <p><span className="font-semibold text-green-500">Poprawka:</span> {log.patch}</p>}
            </div>
          ))}
        </div>
      ) : (
        <p className="text-gray-500">Brak danych analizy logów.</p>
      )}
    </div>
  );
}

export default LogAnalysisResult;