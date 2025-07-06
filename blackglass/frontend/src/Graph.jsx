import React, { useEffect, useRef } from 'react';
import { DataSet, Network } from 'vis-network/standalone';

export default function Graph({ nodes, edges }) {
  const container = useRef(null);

  useEffect(() => {
    const data = { nodes: new DataSet(nodes), edges: new DataSet(edges) };
    const options = { nodes: { color: '#00ffff' }, edges: { color: '#555' } };
    const network = new Network(container.current, data, options);
    return () => network.destroy();
  }, [nodes, edges]);

  return <div ref={container} style={{ height: '400px' }} />;
}
