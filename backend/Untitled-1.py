# backend/server.py
# Simulation d'un mini backend de gestion de tâches
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

tasks = [{"id": 1, "title": "Apprendre Git branches", "completed": False}]

class TaskServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/tasks":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(tasks).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("localhost", 5000), TaskServer)
    print("[SERVER] Démarrage sur http://localhost:5000")
    server.serve_forever()