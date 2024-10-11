import SignIn from "./pages/Auth/SignIn.jsx";
import Register from "./pages/Auth/Register.jsx";

import { Routes } from "react-router-dom";
import { Route } from "react-router-dom";
import { BrowserRouter } from "react-router-dom";
import { Navigate } from "react-router-dom";

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/sign-in" element={<SignIn />} />

          <Route path="/register" element={<Register />} />

          <Route path="*" element={<Navigate to="/sign-in" />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
