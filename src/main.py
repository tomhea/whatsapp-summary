from datetime import datetime
from pathlib import Path

from definitions import CHATS_DIR
from src.ChatViewer import ChatViewer

TEST_PATH = CHATS_DIR / 'test_chat.txt'


def get_chat_viewer(chat_path: Path) -> ChatViewer:
    with open(chat_path, 'r', encoding='utf-8') as chat_file:
        chat_str = chat_file.read()

    return ChatViewer.from_str(chat_str)


# def get_whatsapp_summary(chat_path: Path, from_date: datetime, to_date: datetime) -> str:
#     ...


def main() -> None:
    chat_viewer = get_chat_viewer(TEST_PATH)
    for message in chat_viewer[datetime(2019, 1, 1):datetime(2019, 1, 8)]:
        print(message, end='')


if __name__ == '__main__':
    main()
