import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



os.environ["OPENAI_API_KEY"] = "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"


prefix = """
i have taken photos of answers written by student, after which i take the text out of the photos by ai. The AI is imperfect,
which means that the answer it takes out has a lot of spelling mistakes and sometimes even misses words. What i want you to do is to convert
the messy answers taken out by the ai, and try to reconstruct what the student might have written, please do not add any more information 
than what might be given in the messy answer. This is very important as you do not need to construct more information than what the student
has written as if he had written a bad answer, and you add more information from the messy output of the answer that the ai provides than 
the answer would look better than what the student had originally written, so keep that in my mind. Also please first convert all the new line
symbols to new line spaces before reconstructing the answer

Messy Answer: {input}

Reconstructed Answer:"""


prompt = PromptTemplate(input_variables=["input"],template=prefix)

llm = ChatOpenAI(temperature=0)
llm_chain= LLMChain(llm=llm,prompt=prompt)



def parse(query):
    response = llm_chain(query)
    return response['text']
