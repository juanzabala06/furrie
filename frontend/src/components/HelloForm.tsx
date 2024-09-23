import React, { useState } from 'react';
import { fetchHello } from '../api.ts';

const HelloForm: React.FC = () => {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetchHello(name);
      setMessage(response.message);
    } catch (error) {
      setMessage('An error occurred');
    }
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Please tell me your name?</label>
          <input
            type="text"
            id="name"
            className="form-control"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">Say Hello</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default HelloForm;
