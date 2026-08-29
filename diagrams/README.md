# Diagrams - Task Offloading Framework

## Files

| File | Format | Description |
|------|--------|-------------|
| `1_architecture.dot` | Graphviz DOT | Component architecture and relationships |
| `2_migration_sequence.puml` | PlantUML | Migration sequence diagram (hot standby) |
| `3_migration_statemachine.dot` | Graphviz DOT | Node-level state machine with rollback path |
| `4_timing_hot_standby.puml` | PlantUML | Timing diagram showing zero-gap transfer |
| `4_timing_hot_standby.dot` | Graphviz DOT | Alternative timing diagram in Graphviz |

## How to Render

### Graphviz (.dot files)

Install Graphviz: https://graphviz.org/download/

```bash
# Render to PNG
dot -Tpng 1_architecture.dot -o 1_architecture.png
dot -Tpng 3_migration_statemachine.dot -o 3_migration_statemachine.png
dot -Tpng 4_timing_hot_standby.dot -o 4_timing_hot_standby.png

# Render to PDF
dot -Tpdf 1_architecture.dot -o 1_architecture.pdf
dot -Tpdf 3_migration_statemachine.dot -o 3_migration_statemachine.pdf

# Render to SVG (good for reports)
dot -Tsvg 1_architecture.dot -o 1_architecture.svg
```

### PlantUML (.puml files)

Option 1 - Online: https://www.plantuml.com/plantuml/uml/
Option 2 - CLI: Download plantuml.jar from https://plantuml.com/download

```bash
java -jar plantuml.jar 2_migration_sequence.puml
java -jar plantuml.jar 4_timing_hot_standby.puml
```

Option 3 - VS Code extension: "PlantUML" by jebbs (Alt+D to preview)

## Diagram Descriptions

### 1. Architecture
Shows the framework components:
- Offload Manager (regular Node): Registry, Decision Engine, Migration Controller
- OffloadableNode (extends LifecycleNode): Lifecycle Manager, State Manager, Offload Agent
- Physical Twin environment with Sensor Nodes
- Digital Twin environment with target node instances
- ROS2 interfaces: Topics, Services, Actions connecting them

### 2. Migration Sequence
Shows the step-by-step interaction between Offload Manager, Source Node, Target Node, 
and Sensor Node during a hot-standby migration. Key: source stays Active until target
is confirmed Active (zero-gap).

### 3. Migration State Machine
Shows every state an OffloadableNode goes through during migration, for both source 
and target sides. Includes the rollback path: any failure → Offload Manager re-activates 
the source node.

### 4. Timing Diagram (Hot Standby)
Shows the temporal overlap: at time t3, both source and target are Active simultaneously.
Source is only deactivated after target is confirmed. This eliminates the danger gap
where no node is processing safety-critical data.
