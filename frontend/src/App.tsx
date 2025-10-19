import { RecoilRoot } from 'recoil'
import CreateUserForm from './components/CreateUserForm'
import LoginForm from './components/LoginForm'
import TokenDisplay from './components/TokenDisplay'
import MePanel from './components/MePanel'
import './App.css'
import ToastContainer from './components/ToastContainer'
import Sidebar from './components/Sidebar'
import RightSidebar from './components/RightSidebar'
import React from 'react'

function App() {
  return (
    <RecoilRoot>
      <nav className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-center items-center">
          <h1 className="text-center text-2xl font-bold">Auth Dashboard</h1>
        </div>
      </nav>
      <div className="max-w-7xl mx-auto px-4 mt-6 flex gap-6">
        <Sidebar />
        <main className="flex-1">
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 justify-items-center">
            <div className="tile p-4 w-full"><TokenDisplay /></div>
            <div className="tile p-4 w-full"><CreateUserForm /></div>
            <div className="tile p-4 w-full"><LoginForm /></div>
            <div className="tile p-4 w-full md:col-span-2 xl:col-span-3"><MePanel /></div>
          </div>
        </main>
        <RightSidebar />
      </div>
      <ToastContainer />
    </RecoilRoot>
  )
}

export default App


