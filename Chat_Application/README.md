# Chat Application (Socket Programming) 💬

A simple multi-client real-time chat application built with Python. This project demonstrates the use of socket programming and multithreading for basic network communication.

---

## 🔧 Features

- Multiple clients can connect to a single server
- Real-time message exchange
- Colored console output using `colorama`
- Nickname system for identifying users
- Server can also broadcast messages
- Graceful exit from chat using `exit` command

---

## 🛠 Technologies Used

- Python `socket` library
- `threading` for concurrent client handling
- `colorama` for colored text in terminal
- Basic terminal-based user interface

---

## 📁 Project Structure

chat_application/
│
├── server.py # Runs the server and handles incoming 
└── client.py # Runs the chat client

---

## 🚀 How to Run

### 1. Clone or download the repository.

### 2. Install requirements:
```bash
pip install colorama
```

## How to Run
1. Run `server.py` in one terminal.
2. Run `client.py` in multiple terminals to simulate multiple users.
3. Type `exit` to leave the chat.
