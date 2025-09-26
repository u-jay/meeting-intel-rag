import { useState } from "react";
import axios from "axios";
function App() {
  const [file, setFile] = useState(null);
  const handleFile = (e) => setFile(e.target.files[0]);
  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post("http://localhost:8000/upload/", formData);
    alert("File upload started!");
  };
  return (
    <div>
      <h1>Meeting Insights RAG Demo</h1>
      <input type="file" onChange={handleFile} />
      <button onClick={handleSubmit}>Upload</button>
    </div>
  );
}
export default App;
