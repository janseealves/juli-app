import SignIn from "./pages/auth/SignIn";
import Register from "./pages/register/Register";
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
