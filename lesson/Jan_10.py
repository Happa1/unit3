class Books:
    def __init__(self, my_no_pages, my_weight, my_title, my_author, my_language):
        self.page  = my_no_pages
        self.weight = my_weight
        self.title = my_title
        self.author = my_author
        self.language = my_language

    def get_title(self):
        return self.title

    def get_language(self):
        return self.language

    def get_left_pages(self, current_page):
        left_pages=self.page - current_page
        return left_pages

    def set_translation(self, new_language:str):
        self.language = new_language


agatha_favorite_book = Books(my_no_pages=632, my_weight=500, my_title='harry', my_author='JK', my_language='Belarusian')
manaha_favorite_book = Books(my_no_pages=353, my_weight=300, my_title='management', my_author='PF', my_language='Japanese')
keeler_favorite_book = Books(my_no_pages=210, my_weight=350, my_title='3 body problems', my_author='LC', my_language='English')

print(agatha_favorite_book.get_language())
print(agatha_favorite_book.get_left_pages(current_page=200))

old_language = manaha_favorite_book.get_language()
manaha_favorite_book.set_translation(new_language='English')
print(f'{manaha_favorite_book.get_title()} is translated to {manaha_favorite_book.get_language()}')