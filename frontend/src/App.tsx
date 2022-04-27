import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Websocket} from "./websocket/websocket";

function App() {
  return (
    <div className="App">
      <Websocket />
    </div>
  );
}

export default App;
