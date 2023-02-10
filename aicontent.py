from dotenv import load_dotenv

load_dotenv()

#Set openAI key
def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

#OpenAI key info
KEY_NAME = os.getenv("OPENAI_KEY")
set_openai_key(KEY_NAME)

def openAIQuery(eng,query,temp,tokens,tp,freq,presence,bo):   
    response = openai.Completion.create(
      engine= eng,
      prompt=query,
      temperature=temp,
      max_tokens=tokens,
      top_p=tp,
      best_of=bo,
      frequency_penalty=freq,
      presence_penalty=presence)
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'
    return answer