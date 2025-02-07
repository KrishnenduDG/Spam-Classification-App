import { useState } from "react";

function Input({
  className,
  ...props
}: React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={`w-full max-w-lg p-2 border rounded bg-gray-800 text-white ${className}`}
      {...props}
    />
  );
}

function Button({
  className,
  children,
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={`mt-4 px-6 py-2 bg-blue-500 rounded hover:bg-blue-600 disabled:opacity-50 ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const checkSpam = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const response = await fetch(
        "https://spam-classification-app-backend.onrender.com/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ sentence: text }),
        }
      );
      const data = await response.json();
      setResult(data.result); // Assuming the API response contains { "prediction": "spam" or "ham" }
    } catch (error) {
      setResult("Error fetching result");
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-900 text-white">
      <h1 className="text-2xl font-bold mb-4">Spam Checker</h1>
      <Input
        placeholder="Enter your text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <Button onClick={checkSpam} disabled={loading}>
        {loading ? "Checking..." : "Check"}
      </Button>
      {result && (
        <div className="mt-4 p-3 rounded text-lg bg-gray-700">
          {result === "Spam" ? "🚨 Spam Detected!" : "✅ Ham"}
        </div>
      )}
    </div>
  );
}
