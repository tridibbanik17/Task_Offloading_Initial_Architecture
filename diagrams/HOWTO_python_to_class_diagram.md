# Python to Class Diagram (PNG)

## 1. Install

```powershell
py -m pip install pylint
```

## 2. Python -> .puml (run from project root)

```powershell
py -m pylint.pyreverse.main -o puml -p task_offloading -d diagrams task_offloading\task_offloading
```

## 3. Add relationships by hand

Edit `classes_task_offloading.puml` and add the arrows before `@enduml`:

```plantuml
' Inheritance (parent <|-- child)
Node <|-- LifecycleNode

' Association with multiplicity + label
OffloadManager "1" --> "0..*" OffloadableNode : _managed_nodes

' Dependency (type used only in a method signature)
OffloadManager ..> Decision : returns
```

## 4. .puml -> .png (run from diagrams/)

```powershell
java -jar plantuml.jar -tpng classes_task_offloading.puml
```

## Note

`pyreverse` only captures class boxes and inheritance. Associations, multiplicities,
labels, and external classes (`Node` / `LifecycleNode`) are added by hand, so re-running
step 2 overwrites the curated `classes_task_offloading.puml`.
