import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { FaEye, FaEyeSlash } from 'react-icons/fa'

const Login = () => {

    const navigate = useNavigate()
    const baseUrl = import.meta.env.VITE_BASE_URL;
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const [showPassword, setShowPassoword] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await axios.post(`/users/login/`, { email, password }, { withCredentials: true})
            console.log(response);
            
            if(response.status==202) {
                setErrorMessage('')
                navigate('/user-home')
            }
        } catch (error) {
            console.error(error.response?.data?.message || "Something Went Wrong")
            setErrorMessage(error.response.data.message)
        }
    }

    return (
        <section className='flex justify-center items-center min-h-screen bg-linear-to-r from-violet-400 to-blue-400'>
            <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
                <h2 className='text-3xl text-center text-violet-400 font-bold mb-6'>Sign In</h2>
                <form onSubmit={handleSubmit} className='space-y-4'>
                    <div className='text-sm'>
                        <label htmlFor="email" className='block mb-2 font-medium'>Email</label>
                        <input type="email" id='email' value={email} onChange={(e) => setEmail(e.target.value)} className='border border-gray-400 focus:outline-violet-500 rounded-md px-4 py-2 w-full' placeholder='Enter your email' required/>
                    </div>
                    <div className='text-sm'>
                        <label htmlFor="password" className='block mb-2 font-medium'>Password</label>
                        <div className='relative'>
                            <input type={!showPassword ? 'password' : 'text'} value={password} onChange={(e) => setPassword(e.target.value)} id='password' className='border border-gray-400 focus:outline-violet-500 rounded-md px-4 py-2 w-full' placeholder='Enter your password' required/>
                            <a className='absolute inset-y-0 right-3 flex items-center' onClick={() => setShowPassoword(!showPassword)}>{!showPassword ? <FaEye /> : <FaEyeSlash />}</a>
                        </div>
                    </div>
                    <div className='text-center mt-6'>
                        <button type='submit' className='font-medium px-4 py-2 bg-linear-to-r from-blue-400 to-violet-400 text-white rounded-full shadow-lg cursor-pointer'>
                            Sign In
                        </button>
                    </div>
                    <div className='text-center'>
                        <small>Don't have an account? <a onClick={() => navigate('/signup')} className='text-violet-500 cursor-pointer'>Sign Up</a></small>
                        { errorMessage && 
                            <small className='block text-red-500'>{errorMessage}</small>
                        }
                    </div>
                </form>
            </div>
        </section>
    )
}

export default Login