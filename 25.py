import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

# Define your prompt
prompt = "Once upon a time,"

# Generate text based on the prompt
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=50
)

# Print the generated text
print(response['choices'][0]['text'].strip())

