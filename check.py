import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import ResponseSchema, StructuredOutputParser


os.environ["OPENAI_API_KEY"] = "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"


prefix = """
I have a question, to which i have a model answer which is perfect, and what i want is to to match answers written by students to give marks out
of 3 to them. I am using AI to get out text from answers to a question that students have written, but it's kind of messy.
It certainly has a lot of spelling and spacing errors, some words are missing, hence they are not what the students had written originally 
because they were taken out by AI .So what i want you to do is to keep that in mind and take out the context out 
of the components of the model answer and remember it. Now the first component is of 1.5 marks and its is:-

"The liberalisation of trade and investment was initiated to increase international
competitiveness of industrial production, as well as the flow of foreign investments and
technology into the economy. Prior to these reforms, in order to protect domestic industries, India was following a regime of quantitative restrictions on imports and restrictions of
foreign investments. The trade policy reforms aimed at:"

the second, third and fourth components are of 0.5 marks each and they are:-

2.) "dismantling of quantitative restrictions on imports and exports."
3.) "reduction of tariff rates."
4.)"removal of licensing procedures for imports."



Then i will give you the answers by students which are messed up due to AI, you take out context and match them with the context of the
components of the model answer, how you will do that is by seeing if there are context that match with the context of each component and 
then give marks for individual components. For example, you see how much the context match with those of component 1 and give marks according
to the total marks of component 1 which is 1.5, then you repeat this for all the components. Remember that the marks you give should be 
a multiple of 0.25.After you have done all this add all the scores of each component and give the marks that the student has got.
Please dont worry about the description or the spacing or spelling errors and just match context.

At the end, also give the reason why the score of the student is given like that in an up to the point manner

Student's Answer: {input} 

{response_format}"""

Marks = ResponseSchema(
        name="marks",
        description="The marks given to the student's answer",
    )

Reason = ResponseSchema(
        name="reason",
        description="The reason for the marks assigned to the student",
    )


output_parser = StructuredOutputParser.from_response_schemas(
    [Marks, Reason]
)
response_format = output_parser.get_format_instructions()

prompt = PromptTemplate(input_variables=["input", "model", "response_format", "marks"],template=prefix)

llm = ChatOpenAI(temperature=0)
llm_chain= LLMChain(llm=llm,prompt=prompt)

marks = 3

def check(query):
    response1 = llm_chain.run(input = query, response_format = response_format)
    response2 = output_parser.parse(response1)
    return response2

