class Note:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __str__(self):
        return f"Note '{self.name}': {self.text}"

class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        found_note = [n for n in self.notes if n.name == note.name]

        if found_note:
            found_note[0].text = note.text
        
        self.notes.append(note)

    def search_notes(self, name):
        # Placeholder for search note. I assume crud to file logic. Rewrite below (just to test)
        return [note for note in self.notes if name.lower() == note.name.lower()]

    def edit_note(self, note_name, new_note):
        # Placeholder for edit note. I assume crud to file logic. Rewrite below (just to test)
        found_note = [note for note in self.notes if note.name == note_name]

        if found_note:
            found_note[0].text = new_note.text

    def delete_note(self, note_name):
        # Placeholder for del note. I assume crud to file logic. Rewrite below (just to test)
        self.notes = [note for note in self.notes if note.name != note_name]

    def show_notes(self):
        if self.notes:
            result = "All notes:\n"
            for note in self.notes:
                result += f"{note}\n"
            return result.strip()
        else:
            return "No notes found."