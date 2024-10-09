import { Box } from '@mui/material'
import React from 'react'

const CenteredBox = ({ children }) => {
    return (
        <Box
            display="flex"
            alignItems="center"
            justifyContent="center"
            minHeight="80vh"
        >
            { children }
        </Box>
    )
}

export default CenteredBox