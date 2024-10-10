import React from 'react'
import { Box, Button, IconButton, InputAdornment, Link, Switch, TextField, Typography } from '@mui/material'
import { useState } from 'react'
import { Visibility } from '@mui/icons-material';
import { VisibilityOff } from '@mui/icons-material';

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
                    <Link href='/register' variant='subtitle2' fontWeight='bold' underline='hover' sx={{ ml: 0.5 }}>
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
                    slotProps={{
                        inputLabel: { shrink: true }
                    }}
                />
                <Link variant='body1' underline='hover' color='textPrimary' sx={{ mb: 1 }}>
                    Forgot password?
                </Link>
                <TextField
                    fullWidth
                    name="password"
                    label="Password"
                    defaultValue="@demo1234"
                    type={showPassword ? "text" : "password"}
                    sx={{ mb: 3 }}
                    slotProps={{
                        inputLabel: { shrink: true },
                        input: {
                            endAdornment:
                                <InputAdornment position='end'>
                                    <IconButton
                                        onClick={() => setShowPassword(!showPassword)}
                                    >
                                        {showPassword ? <Visibility /> : <VisibilityOff />}
                                    </IconButton>
                                </InputAdornment>
                        }
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
                    Sign in
                </Button>
            </Box>
        </>
    )
}

export default SignInForm