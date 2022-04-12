import React, { useState } from 'react'
import { Tab } from '@headlessui/react'
import './settings.css'

function classNames(...classes: any) {
  return classes.filter(Boolean).join(' ')
}

export function Settings() {

  const [rssLinkToAdd, setRssLinkToAdd] = useState<string>('https://makeall.dev/index.xml')
  const urls = [
    'https://makeall.dev/posts/glitch-vs-stackblitz/',
    'https://mapps.makeall.dev/',
    'https://gleaner.in/',
    'https://ranuzz.github.io/'
  ]
  const tabs = [{id: 'add_rss', title: 'Add RSS'}, {id: 'rm_rss', title: 'Remove RSS'}]

  const addRss = () => {
    console.log('add rss : ', rssLinkToAdd)
  }

  const rmRss = (id: string) => {
    console.log(id)
  }

  return (
    <div className="w-full max-w-2xl px-2 py-16 sm:px-0 m-auto">
      <Tab.Group>
        <Tab.List className="flex p-1 space-x-1 bg-blue-900/20 rounded-xl">
          <Tab
            key={tabs[0].id}
            className={({ selected }) =>
              classNames('tab-title', selected ? 'tab-title-selected' : 'tab-title-not-selected')
            }
          >
            {tabs[0].title}
          </Tab>

          <Tab
            key={tabs[1].id}
            className={({ selected }) =>
              classNames('tab-title', selected ? 'tab-title-selected' : 'tab-title-not-selected')
            }
          >
            {tabs[1].title}
          </Tab>
        </Tab.List>
        <Tab.Panels className="mt-2">
          <Tab.Panel
            key={tabs[0].id}
            className={classNames('tab-content')}
          >
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="rsslink">
              RSS URL
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="rsslink"
              type="text"
              placeholder={rssLinkToAdd}
              value={rssLinkToAdd}
              onChange={(e) => {setRssLinkToAdd(e.target.value)}}>
                
            </input>
            <br /><br />
            <button onClick={addRss} className="btn btn-blue">
              Add
            </button>
          </Tab.Panel>
          <Tab.Panel
            key={tabs[1].id}
            className={classNames('tab-content')}
          >
            <ul>
              {urls.map((url, index) => 
                (
                  <li key={index} className="m-1 p-1">
                    <button className='btn btn-red mr-2' onClick={() => rmRss(index)}>Remove</button>
                    <span className="text-gray-700 text-md font-bold mb-2">
                      {url}
                    </span>
                  </li>
                ))}
            </ul>
          </Tab.Panel>
        </Tab.Panels>
      </Tab.Group>
    </div>
  )
}
