class text_utils:
    def remove_punctuation(text):
        return text.strip(",?.!")

    def count_words(text):
        no_punc = text.strip(",?.!")
        return len(no_punc.split(" "))

    def count_characters(text):
        no_space = text.strip(" ")
        return len(no_space)

    def reverse_text(text):
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

        return reversed_text


