import { Route, Routes } from "react-router-dom";

import Layout from "@/layouts/pageLayout";
import Chatbot from "@/webpages/chat/conversationDetail";
import Home from "@/webpages/home";
import LoginPage from "@/webpages/auth";
import Conversation from "@/webpages/chat/conversationHistory";
import { NonProtectedLayout } from "@/layouts/nonProtectedLayout";
import { ProtectedLayout } from "@/layouts/protectedLayOut";

function Webpages() {
  return (
    <Layout>
      <Routes>
        <Route element={<NonProtectedLayout fallbackRoute="/chatbot" />}>
          <Route path="/login" element={<LoginPage />} />
        </Route>
        <Route element={<ProtectedLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/conversation" element={<Conversation />} />
          <Route path="/chatbot" element={<Chatbot />} />
        </Route>
      </Routes>
    </Layout>
  );
}

export default Webpages;
