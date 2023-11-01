# %%

from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# %%

llm = Ollama(
    model="zephyr",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

# %%

prompt = PromptTemplate(
    template="Give me 5 interesting facts about {topic}", input_variables=["topic"]
)

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

# %%

chain.run("nudity in movies")
