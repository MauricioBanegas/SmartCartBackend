from datetime import datetime
from typing import List, Optional

class BitacoraEntry:
    def __init__(self, id: int, user_id: int, action: str, timestamp: Optional[datetime] = None):
        self.id = id
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp or datetime.now()

class BitacoraService:
    def __init__(self):
        self.entries: List[BitacoraEntry] = []

    def add_entry(self, user_id: int, action: str) -> BitacoraEntry:
        new_id = len(self.entries) + 1
        entry = BitacoraEntry(id=new_id, user_id=user_id, action=action)
        self.entries.append(entry)
        return entry

    def get_entries(self) -> List[BitacoraEntry]:
        return self.entries

    def get_entries_by_user(self, user_id: int) -> List[BitacoraEntry]:
        return [entry for entry in self.entries if entry.user_id == user_id]

    def delete_entry(self, entry_id: int) -> bool:
        for i, entry in enumerate(self.entries):
            if entry.id == entry_id:
                del self.entries[i]
                return True
        return False