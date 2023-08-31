

strings_for_input = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ".", ",", "?",
                     "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", "_", "''", "$", "@", " "]

morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
               "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
               "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-",
               "--..--", "..--..", ".----.", "-.-.--", "-..-.", "-.--.", "-.--.-", ".-...", "---...",
               "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-", ".-..-.", "...-..-", ".--.-",
               "/"]


def encode(decoded_message):
    encoded_message = ""
    for char in decoded_message:
        if char in strings_for_input:
            position = strings_for_input.index(char)  # here .index gives the index starts counting from 0
            morse_output = morse_codes[position]
            encoded_message += morse_output + " "
    return encoded_message  # here return should be outside the for loop since return ends the function


def decode(encoded_message):
    decoded_message = ""
    for char in encoded_message.split(" "):  # Split a string into a list where each word is a list item
        if char in morse_codes:
            position = morse_codes.index(char)
            reverse_morse_code = strings_for_input[position]
            decoded_message += reverse_morse_code
    return decoded_message
