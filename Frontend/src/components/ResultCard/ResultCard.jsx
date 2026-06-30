import { HeartPulse, CheckCircle, AlertTriangle } from "lucide-react";

function ResultCard({ result }) {

    if (!result) return null;

    const highRisk = result.prediction === 1;

    return (

        <div
            className={`mt-10 rounded-3xl shadow-xl p-8 text-white ${
                highRisk
                    ? "bg-gradient-to-r from-red-500 to-red-700"
                    : "bg-gradient-to-r from-green-500 to-green-700"
            }`}
        >

            <div className="flex items-center gap-3">

                <HeartPulse size={40} />

                <h2 className="text-3xl font-bold">

                    Prediction Result

                </h2>

            </div>

            <div className="mt-8">

                <h1 className="text-5xl font-extrabold">

                    {highRisk ? "HIGH RISK" : "LOW RISK"}

                </h1>

                <p className="mt-4 text-xl">

                    Risk Score

                </p>

                <h2 className="text-6xl font-bold">

                    {(result.probability * 100).toFixed(2)}%

                </h2>

            </div>

            <div className="mt-10">

                <h2 className="text-2xl font-bold mb-5">

                    AI Recommendations

                </h2>

                {
                    highRisk
                    ?
                    <ul className="space-y-3">

                        <li className="flex items-center gap-3">

                            <AlertTriangle />

                            Consult a Cardiologist

                        </li>

                        <li className="flex items-center gap-3">

                            <AlertTriangle />

                            Exercise Daily

                        </li>

                        <li className="flex items-center gap-3">

                            <AlertTriangle />

                            Reduce Cholesterol

                        </li>

                        <li className="flex items-center gap-3">

                            <AlertTriangle />

                            Avoid Smoking

                        </li>

                    </ul>

                    :

                    <ul className="space-y-3">

                        <li className="flex items-center gap-3">

                            <CheckCircle />

                            Maintain Healthy Lifestyle

                        </li>

                        <li className="flex items-center gap-3">

                            <CheckCircle />

                            Annual Heart Check-up

                        </li>

                        <li className="flex items-center gap-3">

                            <CheckCircle />

                            Continue Regular Exercise

                        </li>

                    </ul>

                }

            </div>

        </div>

    );

}

export default ResultCard;