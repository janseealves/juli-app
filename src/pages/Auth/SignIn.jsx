import Header from './Header'
import Body from './Body'
import SignInForm from './SignInForm'
import CenteredBox from '../../components/CenteredBox'
import React from 'react'

const SignIn = () => {
    return (
        <>
            <Header />
            <CenteredBox>
                <Body>
                    <SignInForm />
                </Body>
            </CenteredBox>
        </>
    )
}

export default SignIn