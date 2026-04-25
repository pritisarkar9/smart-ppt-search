import React, { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = () => {
    if (!question.trim()) return;
    setAnswer(`You asked: "${question}"`);
    setQuestion("");
  };

  return (
    <div className="app">
      <div className="card">
        <div className="input-box">
          <input
            type="text"
            placeholder="Ask something..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button onClick={handleAsk}>Ask</button>
        </div>

        <div className="output">
        
          <div className="answer-box">
            {answer || "Your answer will appear here..."}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;