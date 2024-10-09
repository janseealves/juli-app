import { Box } from '@mui/material'
import React from 'react'

const Logo = ({ width, height }) => {
    width: String
    height: String
    return (
        <Box
            component="img"
            src={"/juli-logo.png"}
            sx={{
                width: { width },
                height: { height },
            }}
        />
    )
}

export default Logo