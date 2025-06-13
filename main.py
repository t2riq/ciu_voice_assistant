import json
import re
from datetime import datetime
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from api import AssistantFnc

# Load .env
load_dotenv()

# Load responses
with open("responses.json", "r") as f:
    RESPONSES = json.load(f)

def get_local_response(query: str) -> str | None:
    query = query.lower()
    for keyword in sorted(RESPONSES.keys(), key=len, reverse=True):
        if re.search(rf"\b{re.escape(keyword)}\b", query):
            response = RESPONSES[keyword]
            if "{time}" in response:
                return response.format(time=datetime.now().strftime("%H:%M:%S"))
            return response
    return None

class AssistantFnc(llm.FunctionContext):
    @llm.ai_callable(description="Answer based on CIU preset knowledge")
    def query_local(self, query: str) -> str:
        """
        Returns a known campus-related answer if found in local responses.json
        """
        match = get_local_response(query)
        if match:
            return match
        else:
            return "I'm sorry, I don't have that information in my local data."


async def entrypoint(ctx: JobContext):
    chat_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by CIU. Your job is to assist students with information "
            "related to campus services such as restoration, building locations, academic inquiries, etc. "
            "You are designed to help new and returning students navigate the campus and find relevant information. "
            "If a query doesn't match a predefined answer, do your best to generate a helpful response based on your knowledge.")
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        tts=openai.TTS(),
        llm=openai.LLM(),
        chat_ctx=chat_ctx,
        fnc_ctx=AssistantFnc(),
    )

    assistant.start(ctx.room)
    await assistant.say("Hello, I'm CIU Robot Assistant. How can I help you?")
    await assistant.run_forever()

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
