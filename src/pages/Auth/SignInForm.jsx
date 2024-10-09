import React from 'react'
import { Box, Button, InputAdornment, Link, SvgIcon, Switch, TextField, Typography } from '@mui/material'
import { useState } from 'react'

const SignInForm = () => {

    const [showPassword, setShowPassword] = useState(false);

    return (
        <>
            <Box
                gap={1.5}
                display="flex"
                flexDirection="column"
                alignItems="center"
                sx={{ mb: 5 }}
            >
                <Typography variant='h5' fontWeight='bold'>Sign in</Typography>
                <Typography variant='body2' color='textSecondary'>
                    Don't have an account?
                    <Link variant='subtitle2' fontWeight='bold' underline='hover' sx={{ ml: 0.5 }}>
                        Get started
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
                    name="email"
                    label="Email address"
                    defaultValue="juli_demo@gmail.com"
                    sx={{ mb: 3 }}
                />
                <Link variant='body1' underline='hover' color='textPrimary' sx={{mb: 1}}>
                    Forgot password?
                </Link>
                <TextField
                    fullWidth
                    name="password"
                    label="Password"
                    defaultValue="@demo1234"
                    type={showPassword ? "text" : "password"}
                />
                <Typography variant='body2' color='textSecondary' sx={{ mb: 3 }}>
                    Show password?
                    <Switch 
                        onChange={() => setShowPassword(!showPassword)}
                    />
                </Typography>
               

                <Button
                    fullWidth
                    size="large"
                    type="submit"
                    color="primary"
                    variant="contained"
                // onClick=
                >
                    Sign in
                </Button>
            </Box>
        </>
    )
}

export default SignInForm