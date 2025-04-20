import React from 'react';

function BuildStats({ stats }) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-gray-800">Statystyki Ostatnich Buildów</h2> {/* Zmieniono na text-gray-800 */}
      {stats.length > 0 ? (
        <table className="table-auto w-full">
          <thead>
            <tr className="bg-gray-200 text-gray-700">
              <th className="px-4 py-2">ID Builda</th>
              <th className="px-4 py-2">Status</th>
              <th className="px-4 py-2">Czas trwania</th>
              <th className="px-4 py-2">Data rozpoczęcia</th>
            </tr>
          </thead>
          <tbody>
            {stats.map((stat) => (
              <tr key={stat.id} className="border-b border-gray-200">
                <td className="px-4 py-2">{stat.id}</td>
                <td className={`px-4 py-2 font-semibold ${
                  stat.status === 'Sukces' ? 'text-green-500' :
                  stat.status === 'Niepowodzenie' ? 'text-red-500' :
                  stat.status === 'W trakcie' ? 'text-yellow-500' : 'text-gray-700'
                }`}>{stat.status}</td>
                <td className="px-4 py-2">{stat.duration}</td>
                <td className="px-4 py-2">{new Date(stat.startedAt).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-gray-500">Brak statystyk buildów.</p>
      )}
    </div>
  );
}

export default BuildStats;