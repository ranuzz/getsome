import React, { useState } from 'react'
import './App.css'

function App() {

  const [iframeSrc, setIframeSrc] = useState<string>('https://makeall.dev/')

  const urls = [
    'https://makeall.dev/posts/glitch-vs-stackblitz/',
    'https://mapps.makeall.dev/',
    'https://gleaner.in/',
    'https://ranuzz.github.io/'
  ]

  const getsomeLocal = () => {
    const index = Math.floor(Math.random() * urls.length)
    setIframeSrc(urls[index])
  }

  const getsome = () => {
    fetch('/getsome')
      .then(response => {
        if (!response.ok) {
          console.error('getsome failed you today ! sorry :(')
        }
        return response.text()
      })
      .then(url => setIframeSrc(url))
      .catch(error => console.log(error))
  }

  return (
    <div>
      <iframe src={iframeSrc} className="curframe"></iframe>
      <div className='getsomepanel'>
        <div className='btnone gspbtn' onClick={getsome}>
          R
        </div>
        <div className='btntwo gspbtn'>
          S
        </div>
        <div className='btnthree gspbtn'>
          X
        </div>
      </div>
    </div>
  )
}

export default App
