from collections import defaultdict
from models import Note

class NoteBook:
    __counter = 0

    def __init__(self):
        self.notes = {} #defaultdict(list)

    def add_note(self, note):
        self.notes[NoteBook.__counter].append(note)
        NoteBook.__counter += 1

    def search_notes(self, query):
        return [note for note in self.notes if query.lower() in note.text.lower() or
                query.lower() in note.title.lower() or query.lower() in note.tags]

    def edit_note(self, id, new_note):
        if new_note:
            self.notes[id] = new_note
        # for note in self.notes:
        #     if note.text == old_text:
        #         note.text = new_note.text
        #         break

    def delete_note(self, id):
        print(f"Note {self.notes.pop(id).title}(ID {id}) was deleted")

    def show_notes(self):
        if self.notes:
            result = "All notes:\n"
            for id, note in self.notes.items():
                result += f"ID {id} {note}\n"
            print(result.strip())
        else:
            print("No notes found")