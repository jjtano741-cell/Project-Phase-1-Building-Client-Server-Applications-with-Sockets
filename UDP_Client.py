import socket

# Step 1: Set server details
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12000
BUFFER_SIZE = 1024

# Step 2: Create the UDP socket
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.settimeout(5)

try:
    # ✅ Step 3: Ask the user for a question
    question = input("Ask the server a question: ")

    # Step 4: Send the question to the server
    udp_client.sendto(question.encode(), (SERVER_IP, SERVER_PORT))

    # Step 5: Receive the reply
    response, _ = udp_client.recvfrom(BUFFER_SIZE)

    # Step 6: Show the reply
    print("Server response:", response.decode())

except socket.timeout:
    print("No response received.")
except Exception as e:
    print("Error:", e)
finally:
    # Step 7: Close the socket
    udp_client.close()
    
    
