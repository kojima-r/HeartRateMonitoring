import socket

HOST = "0.0.0.0"
PORT = 5008
BUFFER_SIZE = 4096

def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f"UDP server is listening on {HOST}:{PORT}")

        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(f"Received {len(data)} bytes from {addr}: {data!r}")

            local_ip = sock.getsockname()[0]
            sock.sendto("172.21.46.188".encode("utf-8"), addr)

if __name__ == "__main__":
    main()
