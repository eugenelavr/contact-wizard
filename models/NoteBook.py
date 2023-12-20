class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes(self, query):
        # Placeholder for search note. I assume crud to file logic. Rewrite below (just to test)
        return [note for note in self.notes if query.lower() in note.text.lower()]

    def edit_note(self, old_text, new_note):
        # Placeholder for edit note. I assume crud to file logic. Rewrite below (just to test)
        for note in self.notes:
            if note.text == old_text:
                note.text = new_note.text
                break

    def delete_note(self, text):
        # Placeholder for del note. I assume crud to file logic. Rewrite below (just to test)
        self.notes = [note for note in self.notes if note.text != text]

    def show_notes(self):
        if self.notes:
            result = "All notes:\n"
            for note in self.notes:
                result += f"{note}\n"
            return result.strip()
        else:
            return "No notes found."