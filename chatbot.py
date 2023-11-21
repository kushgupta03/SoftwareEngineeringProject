import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):
    response = openai.completions.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Mental Model Reccomendation System Chatbot</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(share=True,debug = True)



# import os
# import openai
# import gradio as gr
# # openai.api_key = "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"
# # openai.api_key = "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"
# openai.api_key = "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"

# start_sequence = "\nUser:"
# restart_sequence = "\nMMRS: "

# prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nUser: Hello, who are you?\nMMRS: I am an AI chatbot. How can I help you today?\nUser: "

# def openai_create(prompt):

#     response = openai.completions.create(
#     model="gpt-3.5-turbo",
#     # messages=[
#     # {
#     #   "role": "user",
#     #   "content": ""
#     # }
#     # ],
#     prompt=prompt,
#     temperature=0.9,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0.6,
#     stop=[" User:", " MMRS:"]
#     )

#     return response.choices[0].text



# def chatgpt_clone(input, history):
#     history = history or []
#     s = list(sum(history, ()))
#     s.append(input)
#     inp = ' '.join(s)
#     output = openai_create(inp)
#     history.append((input, output))
#     return history, history


# block = gr.Blocks()


# with block:
#     gr.Markdown("""<h1><center>Mental Model Reccomendation Chatbot</center></h1>
#     """)
#     chatbot = gr.Chatbot()
#     message = gr.Textbox(placeholder=prompt)
#     state = gr.State()
#     submit = gr.Button("SEND")
#     submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

# block.launch(share = True,debug = True)



# import os
# import gradio as gr
# import openai

# openai.api_key = "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"
# start_sequence = "\nMMRS:"
# restart_sequence = "\nUser:"
# prompt = "The following is a conversation with a helping assistant which helps its users make their lives better by implementing the power of mental models in their daily lives. Give them examples, diagrams, and present yourself in an easy to understand manner!"


# def openai_create(prompt):
#     response = openai.completions.create(
#     model="gpt-3.5-turbo",
#     prompt=prompt,
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop = ["user:","MMRS:"]
#     )

#     return response.choices[0].text

# def chatgpt_clone(input, history):
#     history = history or []
#     s = list(sum(history,()))
#     s.append(input)
#     inp = " ".join(s)
#     output = openai_create(inp)
#     history.append((input,output))
#     return history, history

# block = gr.Blocks()

# with block:
#     gr.Markdown("""<h1><center>Mental Model Recommendation System Chatbot</center></h1>""")
#     chatbot = gr.Chatbot()
#     message = gr.Textbox(placeholder=prompt)
#     state = gr.State()
#     submit = gr.Button("SEND")
#     submit.click(chatgpt_clone, inputs = [message,state], outputs = [chatbot,state])

# block.launch(share=True,debug = True)