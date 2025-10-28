
import socket  # Step 1: Load networking tools

# Step 2: Set server details
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12000
BUFFER_SIZE = 1024

# Step 3: Create a TCP socket
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Step 4: Connect to the server
    tcp_client.connect((SERVER_IP, SERVER_PORT))

    # ✅ Step 5: Ask the user for a question
    question = input("Ask the server a question: ")

    # Step 6: Send the question
    tcp_client.send(question.encode())

    # Step 7: Receive the reply
    response = tcp_client.recv(BUFFER_SIZE)

    # Step 8: Show the reply
    print("Server response:", response.decode())

except Exception as e:
    print("Connection error:", e)
finally:
    # Step 9: Close the socket
    tcp_client.close()
    