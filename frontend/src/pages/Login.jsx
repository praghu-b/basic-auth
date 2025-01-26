import React, { useState } from 'react'

const Login = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')

    const onSubmit = async () => {
        // const response = await axios.post('')
        return
    }

    return (
        <section className='flex justify-center items-center min-h-screen bg-linear-to-r from-violet-400 to-blue-400'>
            <div className="bg-white p-6">
                <form action={onSubmit} className='p-6'>
                    <div className='p-6'>
                        <label htmlFor="email" className=''>Email</label>
                        <input type="text" placeholder='Enter your email'/>
                    </div>
                    <div>
                        <label htmlFor="email"></label>
                        <input type="text" />
                    </div>
                    <div>
                        <label htmlFor="name"></label>
                        <input type="text" />
                    </div>
                </form>
            </div>
        </section>
    )
}

export default Login