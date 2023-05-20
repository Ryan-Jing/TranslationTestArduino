import { useState, useEffect } from 'react'
import React from 'react'
import { BsMic } from "react-icons/bs";

function App() {
  const [recording, setRecording] = useState(false);
  const [audioData, setAudioData] = useState([]);
    const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);

  let chunks = [];

  useEffect(() => {
    const handleDataAvailable = (event) => {
      chunks.push(event.data);
    };

    const handleStop = () => {
      const blob = new Blob(chunks, { type: 'audio/webm' });
      const audioUrl = URL.createObjectURL(blob);
      console.log('Recorded audio:', audioUrl);
      setAudioData(chunks);
    };

    navigator.mediaDevices.getUserMedia({ audio: true })
      .then((stream) => {
        const newMediaRecorder = new MediaRecorder(stream);
        newMediaRecorder.addEventListener('dataavailable', handleDataAvailable);
        newMediaRecorder.addEventListener('stop', handleStop);
        setMediaRecorder(newMediaRecorder)
      })
      .catch((error) => {
        console.error('Error accessing microphone:', error);
      });

    return () => {
      if (mediaRecorder && mediaRecorder.state === 'recording') {
        console.log("mediaRecorder.stream", mediaRecorder.stream)
        mediaRecorder.stop();
      }
    };
  }, []);

  const startRecording = () => {
    chunks = [];
    console.log("starting recording")
    if (!mediaRecorder) return;
    console.log("media ")
    mediaRecorder.start();
    setRecording(true);
  };

  const stopRecording = () => {
    console.log("stopping recording")
    if (!mediaRecorder) return;
    console.log("media")
    console.log("mediaRecorder.stream", mediaRecorder.stream)
    mediaRecorder.stop();
    setRecording(false);
  };

  const handleClick = () => {
    if (recording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="flex flex-col">
        <button onClick={handleClick} className="focus:outline-none">
          <BsMic size={50}/>
        </button>
      </div>
    </div>
  )
}

export default App
