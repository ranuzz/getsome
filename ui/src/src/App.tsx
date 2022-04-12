import React, { useState } from 'react'
import { RefreshIcon, CogIcon } from '@heroicons/react/outline'
import { Dialog, Transition  } from '@headlessui/react'
import './App.css'
import { Settings } from './settings'


function App() {

  const [iframeSrc, setIframeSrc] = useState<string>('https://makeall.dev/')
  const [isSettingModalOpen, setIsSettingModalOpen] = useState(false)

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
        <div className='gspbtn' onClick={getsome}>
          <RefreshIcon className="gspicon"></RefreshIcon>
        </div>
        <div className='gspbtn' onClick={() => setIsSettingModalOpen(true)}>
          <CogIcon className="gspicon"></CogIcon>
        </div>
      </div>
      <Transition
        show={isSettingModalOpen}
        enter="transition duration-100 ease-out"
        enterFrom="transform scale-95 opacity-0"
        enterTo="transform scale-100 opacity-100"
        leave="transition duration-75 ease-out"
        leaveFrom="transform scale-100 opacity-100"
        leaveTo="transform scale-95 opacity-0"
      >
        <Dialog open={isSettingModalOpen} onClose={() => setIsSettingModalOpen(false)} className="dialog">
          <div className='dialog-container'>
            <Dialog.Overlay className="dialog-overlay" />
            <div className='dialog-body'>
              <Settings></Settings>
            </div>
          </div>
        </Dialog>
      </Transition>
    </div>
  )
}

export default App
