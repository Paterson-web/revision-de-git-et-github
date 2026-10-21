# frontend/client.py
import urllib.request
import json

def fetch_tasks():
    try:
        url = "http://localhost:5000/tasks"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))
        print("[CLIENT] Tâches récupérées du serveur :")
        for task in data:
            print(f"- {task['title']} (Complété: {task['completed']})")
    except Exception as e:
        print(f"[CLIENT] Erreur de connexion au serveur : {e}")

if __name__ == "__main__":
    fetch_tasks()