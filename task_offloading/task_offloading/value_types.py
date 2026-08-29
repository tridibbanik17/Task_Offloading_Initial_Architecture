from dataclasses import dataclass


@dataclass
class StateSnapshot:
    version: int
    variables: bytes
    buffered_messages: bytes
    subscriptions: list
    timestamp: float

    def to_bytes(self) -> bytes:
        pass

    @classmethod
    def from_bytes(cls, data: bytes) -> "StateSnapshot":
        pass


@dataclass
class NodeRecord:
    node_id: str
    current_location: str
    lifecycle_state: str
    cpu_usage: float
    mem_usage: float
    last_heartbeat: float


@dataclass
class NodeStatus:
    node_id: str
    current_location: str
    lifecycle_state: str
    cpu_usage: float
    mem_usage: float
    migration_eligible: bool


@dataclass
class Decision:
    should_migrate: bool
    node_id: str
    target_location: str
    reason: str


@dataclass
class Migration:
    node_id: str
    source_location: str
    target_location: str
    status: str
    started_at: float
