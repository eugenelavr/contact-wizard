from models.note import Note, NoteBook

class NoteService:
    def __init__(self, note_book):
        self.note_book = note_book

    def add_note(self, text):
        note = Note(text)
        self.note_book.add_note(note)

    def search_notes(self, query):
        return self.note_book.search_notes(query)

    def edit_note(self, old_text, new_note):
        self.note_book.edit_note(old_text, new_note)

    def delete_note(self, text):
        self.note_book.delete_note(text)

    def show_notes(self):
        return self.note_book.show_notes()
