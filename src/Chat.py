from datetime import datetime
from typing import List

from src.ChatMessage import ChatMessage


START_CHAT_MESSAGES_TO_PRINT = 5
END_CHAT_MESSAGES_TO_PRINT = 5


class Chat:
    def __init__(self, chat: str):
        self.chat_messages: List[ChatMessage] = []

        for line in chat.split('\n'):
            try:
                datetime_string, line = line.split(' - ', maxsplit=1)
                chat_time = datetime.strptime(datetime_string, '%m/%d/%y, %H:%M')
            except ValueError:
                self.chat_messages[-1].content += '\n' + line
                continue

            try:
                chat_author, chat_content = line.split(': ', maxsplit=1)
            except ValueError:
                chat_author = None
                chat_content = line
            self.chat_messages.append(ChatMessage(chat_author, chat_time, chat_content))

    def __str__(self):
        chat_summary = f'This chat has {len(self.chat_messages):,} messages:\n\n'
        number_of_middle_chat_messages = len(self.chat_messages) - (START_CHAT_MESSAGES_TO_PRINT + END_CHAT_MESSAGES_TO_PRINT)

        if number_of_middle_chat_messages > 0:
            start_messages = ''.join(map(str, self.chat_messages[:START_CHAT_MESSAGES_TO_PRINT]))
            end_messages = ''.join(map(str, self.chat_messages[-END_CHAT_MESSAGES_TO_PRINT:]))

            middle_messages_summary = f'| ... {number_of_middle_chat_messages:,} more chat messages ... |'
            middle_summery_dots_line = f"+{'-' * (len(middle_messages_summary) - 2)}+"
            middle_summary = f'\n{middle_summery_dots_line}\n{middle_messages_summary}\n{middle_summery_dots_line}\n\n'

            return f'{chat_summary}{start_messages}{middle_summary}{end_messages}'

        else:
            all_messages = ''.join(map(str, self.chat_messages))
            return f'{chat_summary}{all_messages}'
