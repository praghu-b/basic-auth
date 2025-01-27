import { Navigate, Outlet, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useEffect, useState } from 'react'

const PrivateRoute = () => {

  const navigate = useNavigate()
  const [isAuthenticated, setIsAuthenticated] = useState(null)

  useEffect(() => {
    const validateToken = async () => {
      try {
        const response = await axios.post('users/token/validate/')
        setIsAuthenticated(true)
      } catch (error) {
        console.error(error.response.data.message)
        if (error.status == 401) {
          try {
            const response = await axios.post('users/token/refresh/')
            setIsAuthenticated(true)
          } catch (error) {
            console.error(error.response.data.error)
            setIsAuthenticated(false)
          }
        } else {
          console.error(error.response.data.message)
          setIsAuthenticated(false)
        }
      }
    }

    validateToken()
  }, [])

  if (isAuthenticated === null) {
    return null;
  }

  return isAuthenticated ? <Outlet /> : navigate('/login')
}

export default PrivateRoute
