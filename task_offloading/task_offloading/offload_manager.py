from task_offloading.value_types import NodeRecord, Decision, Migration
from task_offloading.offloadable_node import OffloadableNode


class OffloadManager:
    def __init__(self) -> None:
        self._registry: dict[str, NodeRecord] = {}
        self._managed_nodes: dict[str, OffloadableNode] = {}
        self._cpu_threshold: float = 0.0
        self._mem_threshold: float = 0.0
        self._latency_threshold: float = 0.0
        self._active_migrations: dict[str, Migration] = {}

    def spawn_target(self, location: str) -> OffloadableNode:
        # Create a target node at the given location. The Manager owns the
        # returned reference (stored in _managed_nodes) and is responsible for
        # tearing it down later via teardown_node().
        pass

    def register_node(self, record: NodeRecord) -> None:
        pass

    def deregister_node(self, node_id: str) -> None:
        pass

    def teardown_node(self, node_id: str) -> None:
        # Retire a node the Manager created (via spawn_target): remove it from
        # the registry, then free its ROS2 resources by calling the node's
        # built-in destroy_node(). destroy_node() itself is a ROS2 (rclpy)
        # built-in on the node, not defined here.
        pass

    def evaluate(self) -> Decision:
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
