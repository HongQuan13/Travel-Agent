import { Route, Routes } from "react-router-dom";

import Layout from "@/layouts/PageLayout";
import Chatbot from "@/webpages/pages/Message";
import Home from "@/webpages/pages/Home";
import Login from "@/webpages/pages/Login";
import Conversation from "@/webpages/pages/ConversationHistory";
import { NonProtectedLayout } from "@/layouts/NonProtectedLayout";
import { ProtectedLayout } from "@/layouts/ProtectedLayOut";

function Webpages() {
  return (
    <Layout>
      <Routes>
        <Route element={<NonProtectedLayout fallbackRoute="/chatbot" />}>
          <Route path="/login" element={<Login />} />
        </Route>
        <Route element={<ProtectedLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/conversation" element={<Conversation />} />
          <Route path="/chat" element={<Chatbot />} />
        </Route>
      </Routes>
    </Layout>
  );
}

export default Webpages;
