import React from 'react';

function RecentAnomalies({ anomalies }) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-red-700">Ostatnie Anomalie</h2> {/* Zmieniono na text-red-700 (ciemniejszy odcień czerwieni) */}
      {anomalies.length > 0 ? (
        <div className="space-y-2">
          {anomalies.map((anomaly) => (
            <div key={anomaly.id} className="bg-white rounded-md shadow-sm p-4 border border-red-300">
              <p><span className="font-semibold text-gray-600">Timestamp:</span> {new Date(anomaly.timestamp).toLocaleString()}</p>
              <p><span className="font-semibold text-red-500 font-bold">Anomalia:</span> {anomaly.error}</p>
              {anomaly.patch && <p><span className="font-semibold text-green-500">Poprawka:</span> {anomaly.patch}</p>}
            </div>
          ))}
        </div>
      ) : (
        <p className="text-gray-500">Brak ostatnich anomalii.</p>
      )}
    </div>
  );
}

export default RecentAnomalies;