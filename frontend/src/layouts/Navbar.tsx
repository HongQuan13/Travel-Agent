import { Link, useNavigate } from "react-router-dom";
import { Menu } from "lucide-react";
import { Fragment, useState } from "react";

import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Separator } from "@/components/ui/separator";
import { useAuthContext, logout } from "@/features/auth";

const navItems = [
  { name: "Home", href: "/" },
  { name: "Conversation", href: "/conversation" },
  { name: "Chatbot", href: "/chatbot" },
];

export function Navbar() {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);
  const { isAuthenticated, setIsAuthenticated } = useAuthContext();

  const handleLogout = async () => {
    try {
      await logout();
      setIsAuthenticated(false);
      navigate("/login");
    } catch (error) {
      console.log("logout error", error);
    }
  };

  return (
    <nav className="bg-background border-b h-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex-shrink-0 flex items-center">
              <span className="text-2xl font-bold text-primary">Logo</span>
            </Link>
          </div>
          <div className="hidden sm:flex-1 sm:flex sm:items-center sm:justify-center">
            <div className="flex space-x-8">
              {navItems.map((item) => (
                <Button key={item.name} asChild variant="ghost">
                  <Link to={item.href}>{item.name}</Link>
                </Button>
              ))}
              {isAuthenticated ? (
                <Button variant="ghost" onClick={handleLogout}>
                  Logout
                </Button>
              ) : (
                <Button asChild variant="ghost">
                  <Link to="/login">Login</Link>
                </Button>
              )}
            </div>
          </div>
          <div className="flex items-center sm:hidden">
            <Sheet open={isOpen} onOpenChange={setIsOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="icon">
                  <Menu className="h-5 w-5" />
                  <span className="sr-only">Open main menu</span>
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-[240px] sm:w-[540px]">
                <nav className="flex flex-col gap-4">
                  {navItems.map((item, index) => (
                    <Fragment key={item.name}>
                      <Button
                        asChild
                        variant="ghost"
                        className="justify-start"
                        onClick={() => setIsOpen(false)}
                      >
                        <Link to={item.href}>{item.name}</Link>
                      </Button>
                      {index < navItems.length - 1 && <Separator />}
                    </Fragment>
                  ))}
                </nav>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </div>
    </nav>
  );
}
