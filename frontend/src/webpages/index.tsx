import { Route, Routes } from "react-router-dom";

import Layout from "@/components/layout";
import Chatbot from "@/webpages/chat";
import Home from "@/webpages/home";

function Webpages() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/chatbot" element={<Chatbot />} />
      </Routes>
    </Layout>
  );
}

export default Webpages;
