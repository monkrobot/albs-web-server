import enum


__all__ = ['BuildTaskStatus', 'TestTaskStatus']


class BuildTaskStatus(enum.IntEnum):

    IDLE = 0
    EXCLUDED = 1
    STARTED = 2
    COMPLETED = 3
    FAILED = 4


class TestTaskStatus(enum.IntEnum):
    CREATED = 1
    STARTED = 2
    COMPLETED = 3
    FAILED = 4
