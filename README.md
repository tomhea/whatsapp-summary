# Whatsapp Time Period Summery

This project tries to use LLM on your whatsapp chats and to produce summaries of your life in a specific time-frame. Imagine that you could answer "What did I do in June 2021", or on "What did I do on my 20th-birthday week".

The function that we are after is:

```python
def get_whatsapp_summary(chat_path: Path, from_date: datetime, to_date: datetime) -> str:
    ...
```
