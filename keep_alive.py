"""Web server mínimo para o UptimeRobot pingar e manter o bot ativo."""

from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot online!")

    def log_message(self, format, *args) -> None:
        pass


def keep_alive() -> None:
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print("🌐 Servidor web ativo na porta 8080 (UptimeRobot)")
