import React from 'react';

function SuggestedFixes({ fixes }) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-green-600">Sugerowane Poprawki</h2>
      {fixes.length > 0 ? (
        <ul className="list-disc list-inside text-gray-700">
          {fixes.map((fix, index) => (
            <li key={index}>{fix}</li>
          ))}
        </ul>
      ) : (
        <p className="text-gray-500">Brak sugerowanych poprawek.</p>
      )}
    </div>
  );
}

export default SuggestedFixes;