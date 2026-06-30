function SelectField({
  label,
  value,
  onChange,
  options,
  name,
}) {
  return (
    <div className="flex flex-col gap-2">
      <label className="font-semibold text-gray-700">
        {label}
      </label>

      <select
        className="border border-gray-300 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={value}
        onChange={onChange}
        name={name}
      >
        {options.map((option) => (
          <option
            key={option.value}
            value={option.value}
          >
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}

export default SelectField;