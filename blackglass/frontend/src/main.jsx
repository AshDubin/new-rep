import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Graph from './Graph.jsx';

const TABS = ['Identity', 'Vehicle', 'Images', 'Locations', 'Breaches', 'Graph'];

function TabButton({ label, active, onClick }) {
  return (
    <button
      className={`px-3 py-2 ${active ? 'bg-gray-700' : 'bg-gray-800'} text-white`}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

function TabContent({ tab }) {
  if (tab === 'Graph') {
    const nodes = [{ id: 1, label: 'Root' }];
    const edges = [];
    return <Graph nodes={nodes} edges={edges} />;
  }
  return <div>Currently viewing: {tab}</div>;
}

function App() {
  const [tab, setTab] = useState(TABS[0]);
  return (
    <div className="bg-gray-900 min-h-screen text-gray-100 p-4">
      <h1 className="text-2xl mb-4">BlackGlass OSINT</h1>
      <div className="flex space-x-2 mb-4">
        {TABS.map((t) => (
          <TabButton key={t} label={t} active={tab === t} onClick={() => setTab(t)} />
        ))}
      </div>
      <div className="p-4 bg-gray-800 rounded">
        <TabContent tab={tab} />
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
