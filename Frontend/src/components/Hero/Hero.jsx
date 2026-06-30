import { motion } from "framer-motion";

function Hero() {
  return (
    <section className="min-h-screen bg-gradient-to-r from-blue-600 via-cyan-500 to-blue-700 flex items-center">

      <div className="max-w-7xl mx-auto px-8 grid md:grid-cols-2 gap-10 items-center">

        {/* Left */}
        <motion.div
          initial={{ opacity: 0, x: -80 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="text-6xl font-extrabold text-white leading-tight">
            Predict Heart Disease
            <br />
            Before It Happens ❤️
          </h1>

          <p className="mt-6 text-xl text-blue-100 leading-8">
            CardioCare AI combines Machine Learning and Healthcare to estimate
            heart disease risk within seconds.
          </p>

          <div className="mt-10 flex gap-5">
            <button className="bg-white text-blue-600 px-8 py-4 rounded-xl font-semibold hover:scale-105 transition">
              Predict Now
            </button>

            <button className="border border-white text-white px-8 py-4 rounded-xl hover:bg-white hover:text-blue-600 transition">
              Learn More
            </button>
          </div>
        </motion.div>

        {/* Right */}
        <motion.div
          initial={{ opacity: 0, x: 80 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          className="flex justify-center"
        >
          <img
            src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?w=700"
            alt="Healthcare"
            className="rounded-3xl shadow-2xl"
          />
        </motion.div>

      </div>

    </section>
  );
}

export default Hero;