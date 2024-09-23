// src/App.tsx

import React from 'react';
import HelloForm from './components/HelloForm';
import './App.css'; // Ensure you import the CSS file
import logo from './assets/furrie.svg'; // Import the logo image

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="Furr.ie Logo" />
        <h1>Welcome to furr.ie</h1>
        <HelloForm />
      </header>
    </div>
  );
};

export default App;
