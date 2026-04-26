import os

class VibeEngine:
    """
    RAG (Retrieval-Augmented Generation) Engine.
    Retrieves personal taste context from local Google Maps metadata.
    """
    def __init__(self, data_path="data/my_places.txt"):
        self.data_path = data_path

    def get_personal_context(self):
        """Loads personal taste data or returns a baseline profile."""
        if os.path.exists(self.data_path):
            with open(self.data_path, "r", encoding="utf-8") as f:
                return f.read()
        return "User prefers industrial-chic aesthetics, quiet environments, and minimalist interiors."