from models.Note import Note, NoteBook

class NoteService:
    def __init__(self, note_book):
        self.note_book = note_book

    def add_note(self, name, text):
        note = Note(name, text)
        self.note_book.add_note(note)

    def search_notes(self, name):
        return self.note_book.search_notes(name)

    def edit_note(self, note_name, new_note):
        self.note_book.edit_note(note_name, new_note)

    def delete_note(self, note_name):
        self.note_book.delete_note(note_name)

    def show_notes(self):
        return self.note_book.show_notes()
