import { Box, Paper } from '@mui/material'
import React from 'react'

const Body = ({ children }) => {
    return (
        <Box
            display="flex"
            alignItems="center"
            justifyContent="center"
            minHeight="80vh"
        >
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
        </Box>
    )
}

export default Body