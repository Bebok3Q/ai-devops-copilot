import React from 'react';
import PropTypes from 'prop-types';

export const LogCard = ({ entry }) => (
  <div
    className={
      `border-l-4 p-4 rounded-2xl shadow mb-4 ` +
      (entry.is_anomalous
        ? "border-red-500 bg-red-50"
        : "border-green-500 bg-green-50")
    }
  >
    <p className="font-mono text-gray-800 mb-1">
      <strong>Error:</strong> {entry.error}
    </p>
    <p className="text-gray-600 text-sm mb-2">
      <strong>Time:</strong> {new Date(entry.timestamp).toLocaleString()}
    </p>
    {entry.patch && (
      <div className="bg-white p-2 rounded text-sm border">
        <strong>Suggested Fix:</strong> {entry.patch}
      </div>
    )}
  </div>
);

LogCard.propTypes = {
  entry: PropTypes.shape({
    id: PropTypes.number.isRequired,
    timestamp: PropTypes.string.isRequired,
    error: PropTypes.string.isRequired,
    is_anomalous: PropTypes.bool.isRequired,
    patch: PropTypes.string,
  }).isRequired,
};
