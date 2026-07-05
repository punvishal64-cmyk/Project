import { useRef, useState } from "react";
import api from "./services/api";


function App() {
    const [recording, setRecording] = useState(false);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

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
           const audioBlob = new Blob(audioChunksRef.current, {
                type: "audio/webm",
            });

            const formData = new FormData();

            formData.append(
                "file",
                audioBlob,
                "recording.webm"
            );

            try {
                setLoading(true);
                const response = await api.post(
                    "/voice/upload",
                    formData,
                    {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        },
                    }
                );

                setResult(response.data);
                setLoading(false);

            } catch (error) {
                setLoading(false);
                console.error(error);
            }
        };

        mediaRecorder.start();
        setRecording(true);
    };

    const stopRecording = () => {
        mediaRecorderRef.current.stop();
        setRecording(false);
    };

    return (
        <div style={{ padding: "2rem" }}>
            <h1>AI Time Tracker</h1>

            {!recording ? (
                <button onClick={startRecording}>
                    🎤 Start Recording
                </button>
            ) : (
                <button onClick={stopRecording}>
                    ⏹ Stop Recording
                </button>
            )}

            {loading && <p>⏳ Processing...</p>}

            {result && (
                <div>
                    <h2>Transcript</h2>
                    <p>{result.transcript}</p>

                    <h2>Category</h2>
                    <p>{result.analysis.category}</p>

                    <h2>Task</h2>
                    <p>{result.analysis.task}</p>
                </div>
            )}
            
        </div>
    );
}

export default App;