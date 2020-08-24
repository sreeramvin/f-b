import React,{useState} from 'react';
import { Button } from 'reactstrap';

import './App.css';

function App() {
  const [loading,setLoading]=useState(false);
  const [items,setItems]=useState({});

  const search = (evt) =>{
    evt.preventDefault()
    fetch(`http://127.0.0.1:8000/api/todo/`)
    .then(res =>res.json())
    .then(result=>{
      setItems(result);
      setLoading(true);
      console.log(result);
    }
    );
  }


  return (
    <div>
    <div className="App">
      <Button color="danger" onClick={search}>Danger!</Button>
    </div>
    {loading?(
      <div>
      {items.map(el => (
        <li key={el.id}>{el.title}</li>
      ))}
      </div>

    ):(<div>not available</div>)
  }
  </div>
  );
}

export default App;
