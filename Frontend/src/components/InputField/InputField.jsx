function InputField({
  label,
  type = "text",
  value,
  onChange,
  placeholder,
  name,
}) {
  return (
    <div className="flex flex-col gap-2">
      <label className="font-semibold text-gray-700">
        {label}
      </label>

      <input
        className="border border-gray-300 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        name={name}
      />
    </div>
  );
}

export default InputField;