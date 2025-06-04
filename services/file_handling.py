# import os
# import sys

# BOOK_PATH = 'book/book.txt'
# PAGE_SIZE = 1050

# book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    symbols = [',', '.', '!', ':', ';', '?']

    text_slice = text[start:start + size]
    text_split = text_slice.split()

    end_text = text_slice

    for i in range(1, len(text_split)):

        if not text_split[-i].endswith(tuple(symbols)) or text_split[-i+1].endswith(tuple(symbols)):
            continue

        last_word = text_split[-i]
        end_text = text_slice[:text_slice.rfind(last_word) + len(last_word)]
        break

    return (end_text, len(end_text))


book: dict[int, str] = {}
PAGE_SIZE = 1050


def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        text = f.read()

    page, start_index = 1, 0

    while start_index < len(text):
        page_text, actual_len = _get_part_text(text, start_index, PAGE_SIZE)
        book[page] = page_text.lstrip()
        page += 1
        start_index += actual_len


prepare_book('book/book.txt')
# print(book)
