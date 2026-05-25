class EventBus:
    """
    Mediator komunikacji między komponentami.
    Zdarzenia które MUSZĄ być obsługiwane:
    - "transaction_added"    -> data: Transaction
    - "transaction_updated"  -> data: Transaction
    - "transaction_deleted"  -> data: int (id)
    - "category_changed"     -> data: None
    - "goal_updated"         -> data: SavingGoal
    - "theme_changed"        -> data: str ("dark"|"light")
    - "data_refreshed"       -> data: None
    """
    _subscribers: dict = {}

    @classmethod
    def subscribe(cls, event: str, callback: callable):
        if event not in cls._subscribers:
            cls._subscribers[event] = []
        if callback not in cls._subscribers[event]:
            cls._subscribers[event].append(callback)

    @classmethod
    def unsubscribe(cls, event: str, callback: callable):
        if event in cls._subscribers and callback in cls._subscribers[event]:
            cls._subscribers[event].remove(callback)

    @classmethod
    def publish(cls, event: str, data=None):
        for callback in cls._subscribers.get(event, []):
            try:
                callback(data)
            except Exception as e:
                print(f"[EventBus] Błąd handlera eventu '{event}': {e}")
