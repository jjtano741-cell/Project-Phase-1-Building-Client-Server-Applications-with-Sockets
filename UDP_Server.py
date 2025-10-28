import socket

# Step 1: Set up server details
HOST = ''  # Listen on all available interfaces
PORT = 12000
BUFFER_SIZE = 1024

# Step 2: Create and bind the UDP socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((HOST, PORT))

print(f"[UDP Server] Ready to answer identity questions on port {PORT}...")

try:
    while True:
        # Step 3: Wait for a message from the client
        data, client_addr = udp_server.recvfrom(BUFFER_SIZE)
        question = data.decode().strip()

        # Step 4: Respond based on the question
        if question.lower() == "are you bruce wayne?":
            reply = "Yes, I am Batman."
        else:
            reply = "No, I'm just a server."

        # Step 5: Send the reply back to the client
        udp_server.sendto(reply.encode(), client_addr)

        # Step 6: Log the interaction
        print(f"Answered {client_addr}: {question} → {reply}")

except KeyboardInterrupt:
    print("\n[UDP Server] Shutting down.")
finally:
    # Step 7: Close the socket
    udp_server.close()
    
    
    