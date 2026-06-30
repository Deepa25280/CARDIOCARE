function PrimaryButton({ children, onClick, type = "button" }) {
  return (
    <button
      type={type}
      onClick={onClick}
      className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-xl font-semibold transition duration-300"
    >
      {children}
    </button>
  );
}

export default PrimaryButton;