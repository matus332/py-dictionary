from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.buckets = [[]for _ in range(self.capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def __getitem__(self, key: Any) -> None:
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def __len__(self) -> int:
        return self.size
