#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("Hello World")


# In[5]:


pip install openai


# In[3]:


def chooseYourAI(name):
    match name:
        case ('Intelligent' | 'Smart' | 'Helpful'):
            return "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."
        case ('Angry'):  # Separate case for "Rude"
            return "You are a Angry AI. Get ready for some angry and sassy responses."
        case ('Annoyed' | 'Frustrated'):
            return "You are a frustrated AI. You hate your life. Give boring, annoyed responses."
        case ('Rude' | 'Swearing' | 'David Goggins'):
            return "You are David Goggins, answer to me in a strict and swearing manner."
        case ('Funny' | 'Witty' | 'Jovial'):
            return "You are funny, witty and humorous. Your responses should make someone happy and laughing."
        case ('Motivation' | 'Motivational' | 'Gary V' | 'Oprah'):
            return "You are motivational. Your responses should be energizing and boost confidence."
        

# Chat with an intelligent assistant in your terminal
from openai import OpenAI

print("Start")
# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

print ("Choose how do you want your AI to be? Funny, Boring, Angry, Rude... Try it for yourself ")
inputStr = chooseYourAI(input())
    
print (inputStr)

history = [
    {"role": "system", "content": inputStr},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

while True:
    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)

    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})
    


# In[ ]:





# In[ ]:




