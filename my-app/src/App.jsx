import { useState, useEffect } from 'react'
import './App.css'
import Comment from './Comment'

function App() {
  const [comment, setComment] = useState([])
  
  const fetchComments =  async () => {
    try {
      const response = await fetch('http://localhost:8000/api/comments/');
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      const json = await response.json();
      const comments = json.comments
      setComment(comments)
    } catch (error) {
      console.error(error.message);
    }
  }

  useEffect(()=> {
    fetchComments()
  }, [])

  return (
    <>
      {
        comment.map((c)=> {
          return <Comment id={c.id} author={c.author} text={c.text} date={c.date} likes={c.likes} image={c.image}></Comment>
        })
      }
    </>
  )
}

export default App
