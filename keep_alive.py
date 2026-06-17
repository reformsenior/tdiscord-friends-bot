"""Web server mínimo para o UptimeRobot pingar e manter o bot ativo."""

import os
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
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"🌐 Servidor web ativo na porta {port} (UptimeRobot)")
