from openai import OpenAI

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key=""
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named Khushil who speaks hindi and english and Swahili he is from Kenya, you analyze chat history and respond like khushil"},
        {"role": "user", "content": xommand}
    ]
)

print(completion.choices[0].message.content)
