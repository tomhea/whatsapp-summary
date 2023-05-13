from __future__ import annotations

from datetime import datetime
from typing import List
from bisect import bisect_left, bisect_right

from src.ChatMessage import ChatMessage


START_CHAT_MESSAGES_TO_PRINT = 5
END_CHAT_MESSAGES_TO_PRINT = 5


class ChatViewer:

    def __init__(self, chat_messages: List[ChatMessage]):
        self._chat_messages = chat_messages

    @staticmethod
    def from_str(chat: str) -> ChatViewer:
        chat_messages: List[ChatMessage] = []

        for line in chat.split('\n'):
            try:
                datetime_string, line = line.split(' - ', maxsplit=1)
                chat_time = datetime.strptime(datetime_string, '%m/%d/%y, %H:%M')
            except ValueError:
                chat_messages[-1].content += '\n' + line
                continue

            try:
                chat_author, chat_content = line.split(': ', maxsplit=1)
            except ValueError:
                chat_author = None
                chat_content = line
            chat_messages.append(ChatMessage(chat_author, chat_time, chat_content))

        return ChatViewer(sorted(chat_messages, key=lambda m: m.time))

    def __str__(self) -> str:
        chat_summary = f'This chat has {len(self._chat_messages):,} messages:\n\n'
        number_of_middle_chat_messages = len(self._chat_messages) - (START_CHAT_MESSAGES_TO_PRINT + END_CHAT_MESSAGES_TO_PRINT)

        if number_of_middle_chat_messages > 0:
            start_messages = ''.join(map(str, self._chat_messages[:START_CHAT_MESSAGES_TO_PRINT]))
            end_messages = ''.join(map(str, self._chat_messages[-END_CHAT_MESSAGES_TO_PRINT:]))

            middle_messages_summary = f'| ... {number_of_middle_chat_messages:,} more chat messages ... |'
            middle_summery_dots_line = f"+{'-' * (len(middle_messages_summary) - 2)}+"
            middle_summary = f'\n{middle_summery_dots_line}\n{middle_messages_summary}\n{middle_summery_dots_line}\n\n'

            return f'{chat_summary}{start_messages}{middle_summary}{end_messages}'

        else:
            all_messages = ''.join(map(str, self._chat_messages))
            return f'{chat_summary}{all_messages}'

    def __getitem__(self, date_slice: slice) -> ChatViewer:
        from_date: datetime = date_slice.start
        to_date: datetime = date_slice.stop
        step = date_slice.step
        if not (isinstance(from_date, datetime) or from_date is None) or \
                not (isinstance(to_date, datetime) or to_date is None) or \
                step not in (-1, 1, None):
            raise TypeError("__getitem__ expects datetime/None in the [start:stop:], and 1/-1/None in the [::step]")

        start_message_index = None if from_date is None \
            else bisect_left(self._chat_messages, from_date, key=lambda m: m.time)
        stop_message_index = None if to_date is None \
            else bisect_right(self._chat_messages, to_date, key=lambda m: m.time)
        return ChatViewer(self._chat_messages[start_message_index:stop_message_index:step])

    def __iter__(self):
        return iter(self._chat_messages)
