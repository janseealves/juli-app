import { Box } from '@mui/material'
import React from 'react'
import { useNavigate } from 'react-router-dom'

const Logo = ({ width, height }) => {
    width: String
    height: String

    const navigate = useNavigate();

    const goToHome = () => {
        navigate('/sign-in')
    }

    return (
        <Box
            component="img"
            src={"assets/juli-logo.png"}
            sx={{
                width: { width },
                height: { height },
            }}
            onClick={goToHome}
        />
    )
}

export default Logo