import { Route, Routes } from "react-router-dom";
import Chatbot from "./chat";
import Layout from "@/components/layout";
import Home from "./home";

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
