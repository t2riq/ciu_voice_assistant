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

├── main.py # Main logic for assistant, query handling, LiveKit setup
├── api.py # Contains AssistantFnc with callable functions
├── responses.json # Local preset answers to known student questions
├── .env # Environment config with API keys

## 📋 Sample `responses.json` Entry

```json
{
  "library": "The library is located in Building B, near the main entrance.",
  "cafeteria": "The cafeteria is in Building D, next to the main hall.",
  "time": "The current time is {time}."
}
