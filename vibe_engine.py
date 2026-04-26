import os

class VibeEngine:
    """
    RAG (Retrieval-Augmented Generation) Engine.
    Parses user's private location history to understand personal 'Vibes'.
    """
    def __init__(self, data_path="data/my_places.txt"):
        self.data_path = data_path
        self.knowledge_base = self._load_data()

    def _load_data(self):
        """Loads and splits the text data into searchable chunks."""
        if not os.path.exists(self.data_path):
            return ["Industrial and moody aesthetics."]
        with open(self.data_path, "r", encoding="utf-8") as f:
            content = f.read()
        return [p.strip() for p in content.split("\n\n") if p.strip()]

    def get_my_vibe(self, query):
        """
        Retrieves the most relevant preference chunk based on the query.
        This simulates a Vector DB similarity search.
        """
        query_words = query.lower().split()
        for chunk in self.knowledge_base:
            if any(word in chunk.lower() for word in query_words):
                return chunk
        return self.knowledge_base[0] # Default to the first profile if no match