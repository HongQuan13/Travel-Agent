import React from "react";

import { Navbar } from "@/layouts/Navbar";

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-grow h-[calc(100vh-64px)] items-center justify-center">
        {children}
      </main>
    </div>
  );
};

export default Layout;
