import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TextList = () => {
  const [texts, setTexts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/text/');
        setTexts(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Texts</h1>
      <ul>
        {texts.map((text) => (
          <li key={text.id}>   {text.title}  </li>
        ))}
      </ul>
    </div>
  );
};

export default TextList;
