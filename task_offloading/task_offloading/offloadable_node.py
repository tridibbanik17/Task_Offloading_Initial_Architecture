from typing import Any

from rclpy.lifecycle import LifecycleNode
from rclpy.lifecycle import LifecycleState
from rclpy.lifecycle import TransitionCallbackReturn

from task_offloading.value_types import StateSnapshot, NodeStatus


class OffloadableNode(LifecycleNode):
    def __init__(self, node_id: str, current_location: str) -> None:
        super().__init__(node_id)
        self.current_location = current_location
        self._internal_state: dict[str, Any] = {}
        self._lifecycle_state: str = "unconfigured"
        self._snapshot_version: int = 0
        self._snapshot: StateSnapshot | None = None

    def report_location(self) -> None:
        pass

    # --- Lifecycle callbacks (ROS2) ---
    def on_configure(self, state: LifecycleState) -> TransitionCallbackReturn:
        pass

    def on_activate(self, state: LifecycleState) -> TransitionCallbackReturn:
        pass

    def on_deactivate(self, state: LifecycleState) -> TransitionCallbackReturn:
        pass

    def on_shutdown(self, state: LifecycleState) -> TransitionCallbackReturn:
        pass

    def on_error(self, state: LifecycleState) -> TransitionCallbackReturn:
        pass

    # --- State transfer ---
    def serialize_state(self) -> bytes:
        pass

    def deserialize_state(self, data: bytes) -> None:
        pass

    def get_snapshot(self) -> StateSnapshot:
        pass

    def restore_snapshot(self, snapshot: StateSnapshot) -> None:
        pass

    # --- Offload agent ---
    def register_with_manager(self) -> None:
        pass

    def handle_offload_request(self, request, response):
        pass

    def send_heartbeat(self) -> None:
        pass

    def report_status(self) -> NodeStatus:
        pass
