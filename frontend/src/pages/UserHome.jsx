import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const UserHome = () => {

  const navigate = useNavigate()
  const [userInfo, setUserInfo] = useState({})

  useEffect(() => {
    setUserInfo(JSON.parse(localStorage.getItem('userInfo')))
  },[])
  

  const handleLogout = async () => {
    try {
      const response = await axios.post('users/logout/')
      localStorage.clear()
      navigate('/login')
    } catch (error) {
      console.error(error)
    }
  }

  return (
    <section className='flex flex-col items-center justify-center min-h-screen bg-white'>
      <h1 className='font-bold text-3xl text-violet-500 mb-5'>Welcome Back, {userInfo?.name}!</h1>
      <button onClick={handleLogout} className='px-4 py-2 bg-linear-to-r from-violet-400 to-blue-400 text-white text-lg rounded-full font-semibold shadow-xl cursor-pointer'>Logout</button>
    </section>
  )
}

export default UserHome