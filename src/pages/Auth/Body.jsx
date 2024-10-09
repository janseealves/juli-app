import { Paper } from '@mui/material'
import React from 'react'

const Body = ({ children }) => {
    return (
        <Paper
            elevation={3}
            
            sx={{
                px: 5,
                py: 5,
                borderRadius: 3,
                width: "25%"
            }}
        >
            {children}
        </Paper>
    )
}

export default Body