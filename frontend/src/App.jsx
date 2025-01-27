import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import Login from './pages/Login'
import SignUp from './pages/SignUp'
import UserHome from './pages/UserHome'
import PrivateRoute from './components/PrivateRoute'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Login />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<SignUp />} />

        <Route element={<PrivateRoute />}>
          <Route path='/user-home' element={<UserHome />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
