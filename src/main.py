from pathlib import Path

from definitions import CHATS_DIR

TEST_PATH = CHATS_DIR / 'test_chat.txt'


def get_number_of_lines_in_chat(chat_path: Path):
    with open(chat_path, 'r', encoding='utf-8') as chat_file:
        return len(chat_file.readlines())


def get_first_chat_lines(chat_path: Path, number_of_lines: int):
    with open(chat_path, 'r', encoding='utf-8') as chat_file:
        return ''.join(chat_file.readline() for _ in range(number_of_lines))


# def get_whatsapp_summary(chat_path: Path, from_date: datetime, to_date: datetime) -> str:
#     ...


def main():
    print(f'The test chat has {get_number_of_lines_in_chat(TEST_PATH)} chat-lines.')
    print(f'The first 10 lines are:\n{get_first_chat_lines(TEST_PATH, 10)}')


if __name__ == '__main__':
    main()
