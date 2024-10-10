import React from 'react'
import Header from '../../components/Header'
import CenteredCard from '../../components/CenteredCard'
import RegisterForm from './RegisterForm'

const Register = () => {
  return (
    <>
        <Header />
        <CenteredCard>
            <RegisterForm />
        </CenteredCard>
        
    </>
  )
}

export default Register