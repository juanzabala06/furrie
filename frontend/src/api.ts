import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Base URL of your FastAPI backend
  headers: {
    'Content-Type': 'application/json', // Ensures JSON payload
  },
});

export const fetchHello = async (name: string) => {
  try {
    const response = await api.post('/hello', { name });
    console.log(response.data); // Logs the response from the backend
    return response.data;
  } catch (error) {
    console.error('Error fetching hello:', error);
    throw error;
  }
};
