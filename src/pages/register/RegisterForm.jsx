import { VisibilityOff } from '@mui/icons-material';
import { Visibility } from '@mui/icons-material';
import { Box, Button, IconButton, InputAdornment, Switch, TextField, Typography } from '@mui/material'
import { useState } from 'react';
import React from 'react'

const RegisterForm = () => {

    const [showPassword, setShowPassword] = useState(false);

    return (
        <>
            <Box
                gap={1.5}
                display="flex"
                flexDirection="column"
                alignItems="center"
                sx={{ mb: 3 }}
            >
                <Typography variant='h5' fontWeight='bold' color='primary'>Register new account</Typography>
            </Box>
            <Box 
                display="flex"
                flexDirection="column"
                alignItems="flex-end"
            >
                <TextField 
                    fullWidth
                    required
                    name="fullname"
                    label="Full name"
                    sx={{ mb: 3 }}
                    slotProps={{
                        inputLabel: { shrink: true },
                    }}
                />
                <TextField 
                    fullWidth
                    required
                    name="email"
                    label="Email address"
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
                    type={showPassword ? 'text' : 'password'}
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
                    Register
                </Button>

            </Box>

        </>
    )
}

export default RegisterForm