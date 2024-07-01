import tkinter as tk
from nltk.chat.util import Chat, reflections

# Persiapkan data percakapan
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a bot created by you. You can call me AI.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright", "No worries",]
    ],
    [
        r"aku (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!"]
    ],
]

# Membuat instance chat
chat = Chat(pairs, reflections)

# Fungsi untuk menangani respons chatbot
def get_response():
    user_input = user_entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = chat.respond(user_input)
    chat_log.insert(tk.END, "Bot: " + str(response) + "\n")
    user_entry.delete(0, tk.END)

# Buat jendela utama
root = tk.Tk()
root.title("Chatbot")

# Buat area teks untuk menampilkan percakapan
chat_log = tk.Text(root, bd=1, bg="white", font=("Arial", 12))
chat_log.pack(pady=10, padx=10)

# Buat entri pengguna untuk memasukkan teks
user_entry = tk.Entry(root, bd=1, bg="white", font=("Arial", 12))
user_entry.pack(pady=10, padx=10)
user_entry.bind("<Return>", lambda event: get_response())

# Buat tombol untuk mengirim pesan
send_button = tk.Button(root, text="Send", command=get_response, bd=1, bg="lightgray", font=("Arial", 12))
send_button.pack(pady=10, padx=10)

# Jalankan aplikasi
root.mainloop()
