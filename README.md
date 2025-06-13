# 🎓 CIU Voice Assistant

A voice-enabled assistant built for Cyprus International University (CIU) to help students with campus-related questions using **LiveKit**, **OpenAI**, and **local response mapping** from a JSON file.

---

## 💡 Purpose

The assistant helps CIU students navigate the campus and access essential information through voice commands. It supports questions about:

- Campus directions (library, cafeteria, student union, etc.)
- Academic inquiries (grades, advisors, schedules)
- Restoration (student ID reissue)
- General info (Wi-Fi, printers, time, working hours)

---

## 🧠 How It Works

- **Voice Input**: Captured via microphone using LiveKit.
- **Speech-to-Text**: Handled by OpenAI Whisper.
- **Query Matching**: Questions are matched against `responses.json` using keyword detection.
- **Voice Output**: Text-to-Speech response is spoken back to the user.

If a query doesn't match local data, OpenAI's LLM can generate a fallback response.

---

## 🛠 Technologies Used

- **LiveKit** – For real-time voice streaming and room connection
- **OpenAI** – STT, TTS, and LLM responses
- **Python + asyncio** – Core asynchronous logic
- **Regex + JSON** – For pattern matching in predefined Q&A

---

## 📁 Project Structure
```
├── main.py # Main logic for assistant, query handling, LiveKit setup
├── api.py # Contains AssistantFnc with callable functions
├── responses.json # Local preset answers to known student questions
├── .env # Environment config with API keys
```
## 📋 Sample `responses.json` Entry

```json
{
  "library": "The library is located in Building B, near the main entrance.",
  "cafeteria": "The cafeteria is in Building D, next to the main hall.",
  "time": "The current time is {time}."
}
```

---

## 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/ciu_voice_assistant.git
cd ciu_voice_assistant
```
2. **Install Dependencies**

pip install -r requirements.txt


3. **Add a .env file**
Create a .env file in the root directory and add your keys:

OPENAI_API_KEY=your_openai_key
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_SECRET=your_livekit_secret
LIVEKIT_URL=wss://your-livekit-url


4. **Run the Assistant**
python main.py

---

## 🗣 Example Questions the Assistant Can Handle

- "Where is the library?"
- "What time is it?"
- "How do I access my grades?"
- "How can I restore my student ID?"
- "Where is the nearest printer?"
- "How do I connect to the university Wi-Fi?"
- "Who is my advisor?"
- "Where is the student union?"

---

## 👤 Author

**Tariq Fahed**  
Capstone Developer | Cyprus International University  
Email: tarialajam@gmail.com 
---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute this software for educational purposes.
