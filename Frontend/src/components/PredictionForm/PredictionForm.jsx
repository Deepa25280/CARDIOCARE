import { useState } from "react";
import api from "../../services/api";
import ResultCard from "../ResultCard/ResultCard";

function PredictionForm() {
  const [formData, setFormData] = useState({
    age: "",
    sex: "Male",
    cp: "typical angina",
    trestbps: "",
    chol: "",
    fbs: false,
    restecg: "normal",
    thalch: "",
    exang: false,
    oldpeak: "",
    slope: "flat",
    ca: 0,
    thal: "normal",
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  function handleChange(e) {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: value === "true" ? true : value === "false" ? false : value,
    });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      setLoading(true);

      const response = await api.post("/predict", formData);

      setResult(response.data);
    } catch (error) {
      console.log(error);

      alert("Prediction Failed");
    }

    setLoading(false);
  }

  return (
    <div className="max-w-5xl mx-auto bg-white shadow-xl rounded-2xl p-10">
      <h1 className="text-4xl font-bold text-center text-blue-600 mb-10">
        Heart Disease Prediction
      </h1>
      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-5">
        <input
          className="border p-3 rounded-lg"
          placeholder="Age"
          type="number"
          name="age"
          onChange={handleChange}
        />

        <input
          className="border p-3 rounded-lg"
          placeholder="Blood Pressure"
          type="number"
          name="trestbps"
          onChange={handleChange}
        />

        <input
          className="border p-3 rounded-lg"
          placeholder="Cholesterol"
          type="number"
          name="chol"
          onChange={handleChange}
        />

        <input
          className="border p-3 rounded-lg"
          placeholder="Maximum Heart Rate"
          type="number"
          name="thalch"
          onChange={handleChange}
        />

        <input
          className="border p-3 rounded-lg"
          placeholder="Old Peak"
          type="number"
          step="0.1"
          name="oldpeak"
          onChange={handleChange}
        />

        <select
          className="border p-3 rounded-lg"
          name="sex"
          onChange={handleChange}
        >
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="cp"
          onChange={handleChange}
        >
          <option value="typical angina">Typical Angina</option>
          <option value="atypical angina">Atypical Angina</option>
          <option value="non-anginal">Non-Anginal</option>
          <option value="asymptomatic">Asymptomatic</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="fbs"
          onChange={handleChange}
        >
          <option value={false}>False</option>
          <option value={true}>True</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="restecg"
          onChange={handleChange}
        >
          <option value="normal">Normal</option>
          <option value="lv hypertrophy">LV Hypertrophy</option>
          <option value="st-t abnormality">ST-T Abnormality</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="exang"
          onChange={handleChange}
        >
          <option value={false}>No</option>
          <option value={true}>Yes</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="slope"
          onChange={handleChange}
        >
          <option value="upsloping">Upsloping</option>
          <option value="flat">Flat</option>
          <option value="downsloping">Downsloping</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="ca"
          onChange={handleChange}
        >
          <option value={0}>0</option>
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
        </select>

        <select
          className="border p-3 rounded-lg"
          name="thal"
          onChange={handleChange}
        >
          <option value="normal">Normal</option>
          <option value="fixed defect">Fixed Defect</option>
          <option value="reversable defect">Reversible Defect</option>
        </select>

        <button className="col-span-2 bg-blue-600 text-white p-4 rounded-xl hover:bg-blue-700 transition">
          {loading ? "Predicting..." : "❤️ Predict"}
        </button>
      </form>
      <ResultCard result={result} />;
    </div>
  );
}

export default PredictionForm;
