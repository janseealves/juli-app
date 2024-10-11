import Header from './'
import Body from '../../components/CenteredCard'
import SignInForm from './SignInForm'
import React from 'react'

const SignIn = () => {
    return (
        <>
            <Header />
            <Body>
                <SignInForm />
            </Body>
        </>
    )
}

export default SignIn