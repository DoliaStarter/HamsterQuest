"""
Module responsible for game session information and session scheduling.

Works as background application, doesn't send any templates to user.
Responsibilities:
    1. Start game sessions in case if there are enough users, otherwise rechedule them.
    2. Handle logic of joining the session.
    3. Handle logic of filtering available sessions based on user preferences. 
"""