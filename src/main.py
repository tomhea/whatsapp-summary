from pathlib import Path

from definitions import CHATS_DIR
from src.Chat import Chat


TEST_PATH = CHATS_DIR / 'test_chat.txt'


def get_chat(chat_path: Path) -> Chat:
    with open(chat_path, 'r', encoding='utf-8') as chat_file:
        chat_str = chat_file.read()

    return Chat(chat_str)


# def get_whatsapp_summary(chat_path: Path, from_date: datetime, to_date: datetime) -> str:
#     ...


def main():
    print(get_chat(TEST_PATH))


if __name__ == '__main__':
    main()
