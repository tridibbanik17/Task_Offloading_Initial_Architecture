from task_offloading.value_types import NodeRecord, Decision, Migration
from task_offloading.offloadable_node import OffloadableNode


class OffloadManager:
    def __init__(self) -> None:
        self._registry: dict[str, NodeRecord] = {}
        self._cpu_threshold: float = 0.0
        self._mem_threshold: float = 0.0
        self._latency_threshold: float = 0.0
        self._active_migrations: dict[str, Migration] = {}

    def register_node(self, record: NodeRecord) -> None:
        pass

    def deregister_node(self, node_id: str) -> None:
        pass

    def evaluate(self) -> Decision:
        pass

    def spawn_target(self, location: str) -> OffloadableNode:
        pass

    def initiate_migration(self, node_id: str, target_location: str) -> Migration:
        pass

    def monitor_progress(self, migration: Migration) -> None:
        pass

    def confirm_completion(self, migration: Migration) -> None:
        pass

    def rollback(self, migration: Migration) -> None:
        pass

    def handle_manual_request(self, request, response):
        pass
