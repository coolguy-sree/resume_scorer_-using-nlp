import google.generativeai as palm

def test_chat():
    palm.configure(api_key='AIzaSyAPhwQpJ9sKjazLxrSH01cHRorhed1O_j0')
    response = palm.chat.completions.create(
        model="models/chat-bison-001",
        messages=[{"content": "Hello, how are you?"}]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    test_chat()
