import { Route, Routes } from "react-router-dom";

import Layout from "@/layout/pageLayout";
import Chatbot from "@/webpages/chat";
import Home from "@/webpages/home";
import LoginPage from "@/webpages/auth";
import { NonProtectedLayout } from "@/layout/NonProtectedLayout";
import { ProtectedLayout } from "@/layout/ProtectedLayOut";

function Webpages() {
  return (
    <Layout>
      <Routes>
        <Route element={<NonProtectedLayout fallbackRoute="/chatbot" />}>
          <Route path="/login" element={<LoginPage />} />
        </Route>
        <Route element={<ProtectedLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/chatbot" element={<Chatbot />} />
        </Route>
      </Routes>
    </Layout>
  );
}

export default Webpages;
