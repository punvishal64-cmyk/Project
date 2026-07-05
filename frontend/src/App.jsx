import { useRef, useState } from "react";
import api from "./services/api";
import Header from "./components/Header";
import ResultCard from "./components/ResultCard";

function App() {
  const [recording, setRecording] = useState(false);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [seconds, setSeconds] = useState(0);
  const timerRef = useRef(null);

  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });

    const mediaRecorder = new MediaRecorder(stream);

    mediaRecorderRef.current = mediaRecorder;
    audioChunksRef.current = [];

    mediaRecorder.ondataavailable = (event) => {
      audioChunksRef.current.push(event.data);
    };

    mediaRecorder.onstop = async () => {
      setSeconds(0);
      const audioBlob = new Blob(audioChunksRef.current, {
        type: "audio/webm",
      });

      const formData = new FormData();

      formData.append("file", audioBlob, "recording.webm");

      try {
        setLoading(true);
        const response = await api.post("/voice/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        setResult(response.data);
        setLoading(false);
      } catch (error) {
        setLoading(false);
        console.error(error);
      }
    };

    mediaRecorder.start();
    setRecording(true);

    timerRef.current = setInterval(() => {
      setSeconds((prev) => prev + 1);
    }, 1000);
  };

  const stopRecording = () => {
    clearInterval(timerRef.current);
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  return (
    <div className="min-h-screen bg-slate-100">
      <div className="max-w-md mx-auto p-5">
        <Header />

        <p className="text-center text-gray-500 mb-6">
          Track your day using AI
        </p>

        {!recording ? (
          <button
            onClick={startRecording}
            className="w-full rounded-2xl bg-blue-600 py-4 text-xl font-bold text-white shadow-lg active:scale-95 transition"
          >
            🎤 Start Recording
          </button>
        ) : (
          <button
            onClick={stopRecording}
            className="w-full rounded-2xl bg-red-600 py-4 text-xl font-bold text-white shadow-lg active:scale-95 transition"
          >
            ⏹ Stop Recording
          </button>
        )}

        {recording && (
          <p className="text-center mt-4 text-red-600 font-semibold">
            🔴 Recording... {seconds}s
          </p>
        )}

        {loading && (
          <div className="mt-6 rounded-xl bg-white p-4 shadow text-center">
            <div className="animate-pulse text-lg">
              ⏳ Processing your recording...
            </div>
          </div>
        )}
        <ResultCard result={result} />
      </div>
    </div>
  );
}

export default App;
