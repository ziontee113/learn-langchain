# %%

from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# %%

llm = Ollama(
    model="zephyr", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# %%

llm(
    "create functions for a calculator in python. PLEASE make sure the function keyword is lowercased. DO NOT write any explanation"
)
