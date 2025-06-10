import React, { useState } from 'react';

function App() {
  const [snippets, setSnippets] = useState([]);
  const [currentSnippet, setCurrentSnippet] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const addSnippet = () => {
    if (currentSnippet.trim()) {
      setSnippets([...snippets, currentSnippet.trim()]);
      setCurrentSnippet('');
    }
  };

  const generateSummary = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch('http://localhost:8000/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ snippets })
      });

      if (!res.ok) {
        throw new Error('Failed to fetch summary');
      }

      const data = await res.json();
      setSummary(data.summary);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-xl mx-auto bg-white p-6 rounded-2xl shadow-xl">
        <h1 className="text-2xl font-bold mb-4">AI Journal</h1>

        <textarea
          className="w-full p-2 border rounded mb-2"
          rows="2"
          placeholder="Add a snippet about your day..."
          value={currentSnippet}
          onChange={(e) => setCurrentSnippet(e.target.value)}
        />

        <div className="flex justify-between mb-4">
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            onClick={addSnippet}
          >
            Add Snippet
          </button>
          <button
            className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
            onClick={generateSummary}
            disabled={snippets.length === 0 || loading}
          >
            {loading ? 'Summarizing...' : 'Summarize Day'}
          </button>
        </div>

        {snippets.length > 0 && (
          <div className="mb-4">
            <h2 className="font-semibold mb-2">Your Snippets:</h2>
            <ul className="list-disc pl-6">
              {snippets.map((s, i) => (
                <li key={i}>{s}</li>
              ))}
            </ul>
          </div>
        )}

        {error && (
          <div className="text-red-500 font-semibold mb-2">{error}</div>
        )}

        {summary && (
          <div className="bg-gray-50 border-t pt-4 mt-4">
            <h2 className="font-semibold mb-2">Today's Summary:</h2>
            <p>{summary}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
