
text = "I Love to eat food"


message = []
reversed_message = []

actual_text = text.split(" ")
for word in actual_text:
    message.append(word)

    count = len(message) - 1

for _ in message:
    reversed_message.append(message[count])
    count -= 1

reversed_text = " ".join(reversed_message)

print(reversed_text)
