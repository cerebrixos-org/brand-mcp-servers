# HyperLake MCP tools

The HyperLake MCP server exposes these tools as of `@cerebrixos/hyperlake` 0.2.9 (146 tools). Newer releases may add tools; your MCP client always shows the current list.

Tool names are prefixed with `hyperlake_`. Each tool runs with the permissions of the signed-in HyperLake user.

## Hosted connector

The hosted connector at `https://mcp.hyperlake.cloud/hyperlake-mcp` exposes only these tools:

- Read: `hyperlake_whoami`, `hyperlake_list_clusters`, `hyperlake_get_cluster_status`, `hyperlake_list_catalogs`, `hyperlake_list_apps`, `hyperlake_catalog_expected_fields`, `hyperlake_list_catalog_grants`, `hyperlake_get_catalog_grant`, `hyperlake_list_agents`, `hyperlake_get_agent`, `hyperlake_get_agent_manifest`, `hyperlake_list_agent_capability_providers`, `hyperlake_list_agent_resources`, `hyperlake_get_agent_resource`.
- Write (require confirmation): `hyperlake_create_catalog`, `hyperlake_update_catalog`, `hyperlake_create_catalog_grant`, `hyperlake_update_catalog_grant`, `hyperlake_revoke_catalog_grant`.

Every tool carries a title and read-only, destructive, idempotent and open-world hints.

## SQL and data exploration

| Tool | Description |
| --- | --- |
| `hyperlake_list_catalogs` | List catalogs for a cluster id. |
| `hyperlake_get_cluster_token` | Get a short-lived JWT and connection details for a cluster. |
| `hyperlake_run_query` | Execute a SQL query against a cluster. |
| `hyperlake_list_schemas` | List schemas in a catalog on a cluster. |
| `hyperlake_list_tables` | List tables in a schema on a cluster. |
| `hyperlake_finops` | Estimate query risk or inspect read-only warehouse usage metadata. |

## Dashboards

| Tool | Description |
| --- | --- |
| `hyperlake_dashboard_start` | Start a persisted dashboard draft for an iterative MCP workflow. |
| `hyperlake_dashboard_get` | Read a persisted dashboard draft. |
| `hyperlake_dashboard_list_drafts` | List dashboard drafts created by either MCP or the CLI. |
| `hyperlake_dashboard_list_published` | List canonical published dashboards created by either MCP or the CLI. |
| `hyperlake_dashboard_get_published` | Read a canonical published dashboard created by either MCP or the CLI. |
| `hyperlake_dashboard_run_published` | Deprecated compatibility alias for dashboard_run with dashboard_ref. |
| `hyperlake_dashboard_stop_published` | Stop a locally running published MCP dashboard. |
| `hyperlake_dashboard_set_metadata` | Update persisted dashboard metadata during the iterative draft workflow. |
| `hyperlake_dashboard_add_sql` | Add a SQL dataset and panel to a dashboard draft. |
| `hyperlake_dashboard_remove_dataset` | Remove a dataset and its panels from a dashboard draft. |
| `hyperlake_dashboard_set_runtime` | Set dashboard runtime mode, refresh interval, and drill-down behavior. |
| `hyperlake_dashboard_cancel` | Cancel and delete a dashboard draft. |
| `hyperlake_dashboard_preview` | Preview a dashboard draft and return validation warnings without publishing. |
| `hyperlake_dashboard_validate` | Validate a dashboard draft before publish. |
| `hyperlake_dashboard_publish` | Publish a validated dashboard as the canonical manifest shared with the CLI. |
| `hyperlake_dashboard_export` | Export a dashboard draft to MCP-managed local JSON and HTML files. |
| `hyperlake_dashboard_run` | Run a dashboard with the same runtime as `hyperlake dashboard run`. |
| `hyperlake_dashboard_stop` | Stop a locally running MCP dashboard. |

## Monitors

| Tool | Description |
| --- | --- |
| `hyperlake_begin_monitor_draft` | Begin an in-memory guided monitor draft. |
| `hyperlake_get_monitor_draft_options` | Get the next guided monitor-draft options: clusters until selected, then only catalogs compatible with the selected kind. |
| `hyperlake_update_monitor_draft` | Update a guided monitor draft. |
| `hyperlake_preview_monitor_draft` | Validate and preview a monitor draft before creation, including the completion data stored by the server. |
| `hyperlake_create_monitor_from_draft` | Create a reviewed monitor draft as inactive. |
| `hyperlake_create_monitor` | Create a durable governed monitor. |
| `hyperlake_list_monitors` | List durable monitor definitions. |
| `hyperlake_get_monitor` | Get one monitor definition. |
| `hyperlake_update_monitor` | Update and version a monitor definition. |
| `hyperlake_delete_monitor` | Delete a monitor that has no run history. |
| `hyperlake_run_monitor` | Claim and run a monitor from this machine. |
| `hyperlake_list_monitor_runs` | List auditable monitor run history. |
| `hyperlake_get_monitor_run` | Get a monitor run, assertions, and sanitized evidence. |
| `hyperlake_cancel_monitor_run` | Cancel a non-terminal monitor run. |

## Semantic data lake

| Tool | Description |
| --- | --- |
| `hyperlake_semantic_model` | Manage the existing Modal-backed semantic generation runs, drafts, and approvals. |
| `hyperlake_semantic_datalake_health` | Check whether the Semantic Data Lake service is healthy. |
| `hyperlake_semantic_datalake_llm_status` | Show the Semantic Data Lake LLM configuration and whether it is ready for semantic matching. |
| `hyperlake_semantic_datalake_session_info` | Get the registered Semantic Data Lake session for an email address. |
| `hyperlake_semantic_datalake_dimensions` | List authorized semantic dimensions for the current registration. |
| `hyperlake_semantic_datalake_metrics` | List authorized semantic metrics for the current registration. |
| `hyperlake_semantic_datalake_filters` | Look up permitted values for an authorized semantic dimension. |
| `hyperlake_semantic_datalake_match` | Create a semantic draft from a natural-language question. |
| `hyperlake_semantic_datalake_build` | Build and validate semantic JSON from reviewed selections returned by semantic_datalake_match. |
| `hyperlake_semantic_datalake_execute` | Execute reviewed semantic SQL for a registered session. |
| `hyperlake_semantic_datalake_graph` | Get the semantic model graph for a registered session. |

## Observability and diagnostics

| Tool | Description |
| --- | --- |
| `hyperlake_diagnose_cluster` | Run a read-only, non-persistent diagnosis for an authorized cluster target. |
| `hyperlake_observability_query` | Execute a read-only SQL query against Loki logs or Prometheus metrics for an authorized cluster. |
| `hyperlake_observability_samples` | Return five ready-to-run read-only SQL samples: three for Loki logs and two for Prometheus metrics. |

## Agents and A2A

| Tool | Description |
| --- | --- |
| `hyperlake_a2a_discover_agent` | Discover and validate an A2A 1.0 Agent Card directly from this machine. |
| `hyperlake_a2a_send_message` | Send a text message directly to a discovered A2A agent. |
| `hyperlake_a2a_get_task` | Get a remote A2A task directly from its agent endpoint. |
| `hyperlake_a2a_list_tasks` | List remote A2A tasks, optionally scoped to a context. |
| `hyperlake_a2a_cancel_task` | Request cancellation of a remote A2A task. |
| `hyperlake_list_agents` | List Agent projects available to the authenticated user. |
| `hyperlake_get_agent` | Get an Agent's details, including its metadata, manifest summary, and Copilot settings when available. |
| `hyperlake_get_agent_manifest` | Get the active or draft capability manifest, local execution bindings, and resource scopes for an Agent. |
| `hyperlake_list_agent_capability_providers` | List Hyperlake-owned capability providers and their supported actions before attaching one to an Agent. |
| `hyperlake_create_agent` | Create a private draft Agent. |
| `hyperlake_clone_agent` | Clone an accessible Agent into a new private draft with an independent manifest. |
| `hyperlake_update_agent_manifest_settings` | Update draft purpose, domain context, interaction modes, or default execution route without replacing capabilities or resources. |
| `hyperlake_attach_agent_capability` | Attach a Hyperlake or customer capability to a draft Agent. |
| `hyperlake_detach_agent_capability` | Detach a capability from a draft Agent. |
| `hyperlake_bind_agent_resource` | Bind a described non-secret target, catalog, repository, knowledge base, workflow, dashboard, or storage selector to an Agent capability. |
| `hyperlake_list_agent_resources` | List the resources available through an Agent. |
| `hyperlake_get_agent_resource` | Describe one Agent resource by immutable binding id, including its existing provider, allowed actions, selector, and routing metadata. |
| `hyperlake_unbind_agent_resource` | Remove a resource binding from a draft Agent. |
| `hyperlake_bind_agent_connection` | Bind an opaque credential, OAuth, target identity, or local reference to a draft Agent. |
| `hyperlake_unbind_agent_connection` | Remove an opaque connection reference from a draft Agent. |
| `hyperlake_authorize_agent_capability` | Check whether an active Agent grants a provider action and optional resource to this direct or external invocation. |
| `hyperlake_authorize_agent_resource` | Resolve and authorize one Agent resource as an API-addressable destination. |
| `hyperlake_list_agent_execution_events` | List sanitized Agent execution lifecycle evidence. |
| `hyperlake_record_agent_execution_event` | Record sanitized lifecycle evidence for a direct or external Agent tool run. |
| `hyperlake_compile_agent_context` | Compile a deterministic, sanitized task context from the Agent purpose, capability guidance, resources, and connection metadata. |
| `hyperlake_list_agent_evaluations` | List task-routing evaluations and the latest sanitized result for an Agent manifest. |
| `hyperlake_add_agent_evaluation` | Add a deterministic task-routing evaluation. |
| `hyperlake_remove_agent_evaluation` | Remove an Agent evaluation from the draft manifest after explicit confirmation. |
| `hyperlake_run_agent_evaluations` | Run one or all enabled task-routing evaluations against the current manifest digest. |
| `hyperlake_validate_agent_manifest` | Validate an Agent manifest without activating it. |
| `hyperlake_submit_agent` | Submit a validated Agent manifest for approval. |
| `hyperlake_activate_agent` | Activate a validated private Agent. |
| `hyperlake_run_agent_query` | Execute SQL locally through an existing target resource attached to an active Agent. |
| `hyperlake_chat_with_agent` | Chat with an Agent using the Hyperlake conversation API. |

## Catalogs, credentials and secret stores

| Tool | Description |
| --- | --- |
| `hyperlake_list_creds` | List reusable vault credentials available to the current user. |
| `hyperlake_create_cred` | Create a named vault credential. |
| `hyperlake_update_cred` | Update a vault, Kubernetes Secret, or ExternalSecret credential. |
| `hyperlake_get_secret_store` | Get the external secret store configuration for a cluster (AWS Parameter Store, GCP Secret Manager, etc.). |
| `hyperlake_create_secret_store` | Wire an external secret store (AWS Parameter Store or GCP Secret Manager) to a cluster. |
| `hyperlake_delete_secret_store` | Remove the external secret store configuration from a cluster. |
| `hyperlake_catalog_expected_fields` | Discover the required and optional fields for creating a catalog with a given adapter. |
| `hyperlake_create_catalog` | Create a new catalog on a cluster. |
| `hyperlake_list_secret_store_providers` | List external secret-store providers supported by a cluster. |
| `hyperlake_create_k8s_credential` | Create a Kubernetes Secret credential (sync_type=cluster) or an ExternalSecret mapping (sync_type=external). |
| `hyperlake_list_catalog_grants` | List governed catalog access grants. |
| `hyperlake_get_catalog_grant` | Get one governed catalog access grant by grant UUID. |
| `hyperlake_update_catalog_grant` | Partially update a governed catalog access grant. |
| `hyperlake_create_catalog_grant` | Grant a user access to a catalog. |
| `hyperlake_revoke_catalog_grant` | Revoke a catalog access grant. |

## Apps, collaborators and Kubernetes actions

| Tool | Description |
| --- | --- |
| `hyperlake_list_apps` | List one page of installed normal Helm apps for a cluster. |
| `hyperlake_list_k8s_actions` | List governed Kubernetes actions available to the current user. |
| `hyperlake_list_k8s_action_executions` | List one page of Kubernetes-action executions installed on a cluster. |
| `hyperlake_uninstall_k8s_action` | Queue the Kubernetes uninstall for an action execution. |
| `hyperlake_preview_k8s_action` | Preview a governed Kubernetes action without executing it. |
| `hyperlake_run_k8s_action` | Execute a previously previewed/approved governed Kubernetes action. |
| `hyperlake_list_cluster_namespaces` | List Kubernetes namespaces available on one cluster. |
| `hyperlake_list_app_definitions` | List available app definitions. |
| `hyperlake_list_app_versions` | List available versions for an app definition. |
| `hyperlake_get_app_fields` | Get the configurable fields and their expected values for an app definition. |
| `hyperlake_preview_app_deployment` | Preview a governed app deployment without changing the cluster. |
| `hyperlake_deploy_app` | Deploy a governed app to a cluster. |
| `hyperlake_uninstall_app` | Queue the Kubernetes uninstall for a deployed app. |
| `hyperlake_list_app_collaborators` | List collaborators for a deployed app on a cluster. |
| `hyperlake_add_app_collaborator` | Grant a team member access to a deployed app on a cluster. |
| `hyperlake_request_app_access` | Request access to a deployed app on a cluster that you do not own. |
| `hyperlake_approve_app_collaborator` | Approve a pending app-access request on a cluster. |
| `hyperlake_remove_app_collaborator` | Remove a collaborator's access to a deployed app on a cluster. |

## Governed services

| Tool | Description |
| --- | --- |
| `hyperlake_execute_service` | Execute an allowlisted service through Hyperlake-managed trusted access. |
| `hyperlake_list_services` | List server-allowlisted services, actions, risk levels, and approval requirements. |
| `hyperlake_describe_service` | Describe one server-allowlisted service by its service ID. |
| `hyperlake_manage_service_run` | Approve, reject, cancel, or request the allowlisted rollback for a user-scoped service run. |
| `hyperlake_list_service_runs` | List one page of governed service runs visible to the current user. |
| `hyperlake_get_service_run` | Get the current status of a user-scoped service run. |
| `hyperlake_get_service_run_summary` | Get reporting summary artifact metadata for a completed service run. |
| `hyperlake_get_service_run_findings` | Get normalized findings artifact metadata for a service run. |

## Projects

| Tool | Description |
| --- | --- |
| `hyperlake_get_project_context` | Get the authorized infrastructure context for one Hyperlake project. |
| `hyperlake_get_project_graph` | Get the authorized resource and relationship graph for one Hyperlake project. |
| `hyperlake_get_project_health` | Get a summarized health view and warning or critical signals for resources in one authorized Hyperlake project. |
| `hyperlake_get_project_context_history` | Get sanitized, paginated change history for resources in one authorized Hyperlake project. |

## Clusters and networking

| Tool | Description |
| --- | --- |
| `hyperlake_connection_guide` | Explain how to connect Hyperlake privately over stdio or localhost Streamable HTTP. |
| `hyperlake_whoami` | Return the current Hyperlake identity and cluster count. |
| `hyperlake_list_clusters` | List the Hyperlake clusters available to the current user. |
| `hyperlake_check_aws_cluster_prerequisites` | Check this laptop for the AWS CLI and an authenticated AWS caller identity. |
| `hyperlake_get_cluster_creation_assets` | Return the local cluster-creator skill and approved AWS CloudFormation template paths bundled by the npm installation. |
| `hyperlake_get_current_public_ipv4` | Get the current public IPv4 address only when the user explicitly asks. |
| `hyperlake_create_cluster` | Use this tool when the user asks to create a Hyperlake cluster. |
| `hyperlake_list_customer_managed_cluster_drafts` | List incomplete customer-managed AWS cluster drafts. |
| `hyperlake_get_customer_managed_cluster_draft` | Get safe customer-managed cluster setup status. |
| `hyperlake_submit_customer_managed_cluster_setup` | Submit or correct customer-managed AWS setup. |
| `hyperlake_get_cluster_status` | Fetch status for one cluster, including provisioning/sync state returned by the control plane. |
| `hyperlake_update_cluster_configuration` | Submit a generic partial cluster configuration update for an existing AWS or GCP cluster. |
| `hyperlake_get_cluster_configuration` | Fetch the current normalized cluster configuration, API-defined editable fields, constraints, and live machine options. |
| `hyperlake_get_ip_restrictions` | Get the administrator and ingress IPv4 CIDR allowlists for one cluster. |
| `hyperlake_update_ip_restrictions` | Update one or both cluster IPv4 CIDR allowlists. |
