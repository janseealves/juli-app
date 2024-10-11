import { AppBar } from '@mui/material'
import React from 'react'
import Logo from '../../components/Logo'

const Header = () => {
    return (
        <AppBar 
            position='sticky'
            color='transparent'
            sx={{
                boxShadow: 'none'
            }}
        >
            <Logo width='100px' height='50px'/>
        </AppBar>
    )
}

export default Header