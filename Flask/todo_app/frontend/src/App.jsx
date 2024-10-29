import { useEffect, useRef, useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [items, setItems] = useState([])
  const [name, setName ]= useState("")
  const [des, setDef] = useState("")

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:5000/todo")
        setItems(res.data)
      } catch (error) {
        console.error("Error fetching data:", error)
      }
    }

    fetchData()
  }, [])
  return (
    <>
      <div className="container px-3 py-4 mx-auto">
        <div className="h-[25rem] w-25-[rem]">
          {items.map((item, index) => (
            <div key={index}> 
              <h2> Name: {item.name} </h2>
              <h2> Description: {item.description}</h2>
            </div>
          ))}
        </div>
        <div className="h-[25rem] w-25-[rem]">
          <input onChange={(e)=>{
            setName(e.target.value)
          }} type="text" placeholder='name'/>
          <input onChange={(e)=>{
            setDef(e.target.value)
          }} type="text" placeholder='description'/>
          <button onClick={async()=>{
            const res = await axios.post("http://127.0.0.1:5000/todo", 
            {
              name: name,
              description: des
            }
            )
          }}>
            add todo
          </button>
          
        </div>
      </div>
    </>
  )
}

export default App
