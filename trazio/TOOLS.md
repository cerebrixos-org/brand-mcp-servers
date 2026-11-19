# Trazio tools

All tools run with the permissions of the signed-in person and only inside the pipeline they were given. All are read-only except `request_video_export`.

| Tool | What it does |
| --- | --- |
| `whoami` | Shows the tenant, pipeline, region and subject for this connection. |
| `semantic_query` | Runs a natural-language investigation across recent events, video vectors and recorded evidence. |
| `investigate` | Guided investigation across video, logs, rules and telemetry, with synchronized evidence. |
| `search_events` | Natural-language log and event search, with source, severity and time filters. |
| `search_correlations` | Searches detections and evidence edges by terms, relationship or rule. |
| `get_event_neighbors` | Finds graph nodes, edges and detections connected to one event. |
| `get_evidence_graph` | Returns bounded graph neighbors for an event, node or edge. |
| `explain_relationship` | Explains the method, evidence, confidence and limits of one relationship. |
| `find_identity_conflicts` | Finds records where a source identity was reused with a different payload. |
| `trace_run` | Traces a robot run through events and evidence. |
| `list_incidents` | Lists incidents and their state. |
| `get_incident` | Gets one incident with its evidence and audit history. |
| `get_operations_overview` | Counts of entities and incidents for the pipeline. |
| `get_operations_snapshot` | One bounded snapshot of entities, observations, incidents and sampled health. |
| `list_operational_registry` | Lists sites, fleets, devices, cameras and organizations. |
| `get_operational_asset` | Gets one registry record. |
| `open_video` | Creates a short-lived viewer link for an indexed video. |
| `get_video_timeline` | Synchronized rules, logs, diagnostics and telemetry for a video time range. |
| `request_video_export` | Creates a bounded annotated video clip. Needs exports enabled by an admin. |
| `get_video_export` | Reads the status of a video export. |
