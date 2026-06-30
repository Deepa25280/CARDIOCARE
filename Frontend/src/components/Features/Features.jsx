import { FaHeartbeat, FaRobot, FaChartLine } from "react-icons/fa";

function Features() {
  return (
    <section className="py-20 px-10 bg-gray-100">

      <h2 className="text-4xl font-bold text-center mb-16">
        Why Choose CardioCare AI?
      </h2>

      <div className="grid md:grid-cols-3 gap-8">

        <div className="bg-white rounded-xl shadow-lg p-8 text-center">
          <FaHeartbeat className="text-red-500 text-5xl mx-auto mb-5" />
          <h3 className="text-2xl font-bold mb-3">Heart Prediction</h3>
          <p>Predict heart disease using machine learning.</p>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-8 text-center">
          <FaRobot className="text-blue-500 text-5xl mx-auto mb-5" />
          <h3 className="text-2xl font-bold mb-3">AI Powered</h3>
          <p>Built using advanced machine learning algorithms.</p>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-8 text-center">
          <FaChartLine className="text-green-500 text-5xl mx-auto mb-5" />
          <h3 className="text-2xl font-bold mb-3">Instant Results</h3>
          <p>Get predictions and risk analysis within seconds.</p>
        </div>

      </div>

    </section>
  );
}

export default Features;