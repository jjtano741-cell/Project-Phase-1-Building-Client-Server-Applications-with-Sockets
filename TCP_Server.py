
import socket  # Step 1: Load the socket module

# Step 2: Set the server's IP and port
HOST = ''  # Empty string means "listen on all interfaces"
PORT = 12000
BUFFER_SIZE = 1024

# Step 3: Create a TCP socket
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 4: Bind the socket and start listening
tcp_server.bind((HOST, PORT))
tcp_server.listen(5)  # Allow up to 5 waiting connections

print("[TCP Server] Ready to answer...")

try:
    while True:
        # Step 5: Accept a new connection
        conn, addr = tcp_server.accept()

        # Step 6: Receive the question from the client
        question = conn.recv(BUFFER_SIZE).decode().strip()

        # Step 7: Decide how to respond
        if question.lower() == "are you bruce wayne?":
            reply = "Yes, I am Batman."
        else:
            reply = "No, I'm just a server."

        # Step 8: Send the reply back to the client
        conn.send(reply.encode())

        # Step 9: Close the connection
        conn.close()

        # Step 10: Print what happened
        print(f"Answered {addr}: {question} → {reply}")

except KeyboardInterrupt:
    print("\n[TCP Server] Shutting down.")

finally:
    # Step 11: Close the server socket
    tcp_server.close()
    
    