import { Box, Button, Link, TextField, Typography } from '@mui/material'
import React from 'react'

const RegisterForm = () => {

    return (
        <>
            <Box
                gap={1.5}
                display="flex"
                flexDirection="column"
                alignItems="center"
                sx={{ mb: 3 }}
            >
                <Typography variant='h5' fontWeight='bold'>Get started</Typography>
                <Typography variant='body2' color='textSecondary'>
                    Already have an account?
                    <Link href='/sign-in' variant='subtitle2' fontWeight='bold' underline='hover' sx={{ ml: 0.5 }}>
                        Sign in
                    </Link>
                </Typography>
            </Box>
            <Box
                display="flex"
                flexDirection="column"
                alignItems="flex-end"
            >
                <TextField
                    fullWidth
                    required
                    name="email"
                    label="Email address"
                    defaultValue="juli_demo@gmail.com"
                    sx={{ mb: 3 }}
                    slotProps={{
                        inputLabel: { shrink: true },
                    }}
                />
                <TextField
                    fullWidth
                    required
                    name="password"
                    label="Password"
                    type="password"
                    defaultValue="@demo1234"
                    sx={{ mb: 3 }}
                    slotProps={{
                        inputLabel: { shrink: true },
                    }}
                />
                <TextField
                    fullWidth
                    required
                    name="reTypePassword"
                    label="Re-Type Password"
                    type="password"
                    defaultValue="@demo1234"
                    sx={{ mb: 3 }}
                    slotProps={{
                        inputLabel: { shrink: true },
                    }}
                />
                <Button
                    fullWidth
                    size="large"
                    type="submit"
                    color="primary"
                    variant="contained"
                // onClick=
                >
                    Register
                </Button>
            </Box>
        </>
    )
}

export default RegisterForm