import { HeartPulse } from "lucide-react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="fixed top-0 left-0 w-full bg-white/80 backdrop-blur-md shadow-sm z-50">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-8 py-4">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <HeartPulse className="text-red-500 w-8 h-8" />
          <h1 className="text-2xl font-bold text-blue-600">CardioCare AI</h1>
        </div>

        {/* Navigation */}
        <ul className="hidden md:flex items-center gap-8 text-gray-700 font-medium">
          <li className="hover:text-blue-600 cursor-pointer transition">
            Home
          </li>
          <li>
            <Link to="/prediction" className="hover:text-blue-600 transition">
              Prediction
            </Link>
          </li>

          <li className="hover:text-blue-600 cursor-pointer transition">
            Features
          </li>
          <li className="hover:text-blue-600 cursor-pointer transition">
            About
          </li>
          <li className="hover:text-blue-600 cursor-pointer transition">
            Contact
          </li>
        </ul>

        {/* Button */}
        <button className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg transition">
          Get Started
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
