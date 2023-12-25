from models.Note import Note
from models.NoteBook import NoteBook

class NoteService:
    def __init__(self, note_book):
        self.note_book = note_book

    def add_note(self, title, text, tags):
        try:
            note = Note(title, text, tags)
            self.note_book.add_note(note)
        except:
            return False
        return True

    def search_notes(self, query):
        return self.note_book.search_notes(query)

    def edit_note(self, id, new_note):
        self.note_book.edit_note(id, new_note)

    def delete_note(self, id):
        self.note_book.delete_note(id)

    def show_notes(self):
        self.note_book.show_notes()
