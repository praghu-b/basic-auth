import React, { useState } from 'react'

const Login = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')

    const onSubmit = async () => {
        return
    }

    return (
        <section className='flex justify-center items-center min-h-screen bg-linear-to-r from-violet-400 to-blue-400'>
            <div className="bg-white rounded-lg shadow-xl p-6">
                <h2 className='text-3xl text-violet-400 font-bold'>Login</h2>
            </div>
        </section>
    )
}

export default Login