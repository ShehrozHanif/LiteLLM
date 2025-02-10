from litellm import completion


api_key = "AIzaSyB70sBKLCGLa3Z-nCXkI7-VSnEiuo8E_hQ"


def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-flash",
    api_key=api_key,
    messages=[{ "content": "Hello, how are you?","role": "user"}]
    )
    print(response['choices'][0]['message']['content'])