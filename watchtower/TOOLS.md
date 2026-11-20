# Watchtower tools

From the Watchtower tool contract as of November 2026. A workspace exposes 45 tools, or 53 with graph memory. `tools/list` returns only the tools the signed-in person may call. These are the main ones, grouped by what they do. Your MCP client always shows the current list.

## Look up

| Tool | What it does |
| --- | --- |
| `status` | Workspace overview: repositories, clouds, last scan per engine, open issues, change-freeze flag. |
| `capabilities` | Licensed capabilities for this workspace. |
| `list_findings` | Findings from the latest FinOps, security or drift scan, without rescanning. |
| `get_finding` | One finding in full: evidence, monthly cost, fix snippet and rollback. |
| `list_issues` | Open Watchtower issues in the incident repository. |
| `list_reports` | Recorded report runs, newest first, with totals and what changed. |
| `get_report` | One recorded report, including SARIF and OCSF exports. |
| `list_events` | Events Watchtower emitted: sweeps, new findings, alerts, pull requests. |
| `get_scan_job` | Status of a scan or assessment job and its report id. |
| `list_frameworks` | Available compliance frameworks and their automated coverage. |
| `get_compliance_configuration` | The workspace's selected frameworks. |
| `list_assessments` | Compliance assessments, newest first. |
| `get_assessment` | One assessment with every mapped control and evidence gap. |
| `get_assessment_plan` | Preview of what an assessment run will cover. |
| `get_assessment_schedule` | The recurring assessment schedule. |
| `blast_radius` | What depends on a resource, grouped by hop depth. |
| `pr_impact` | What a pull request in an infrastructure repository would touch on the live estate; can also post that as a PR comment. |
| `verify_cloud` | Live, read-only check that a cloud account is reachable. |

Read-only cloud, Kubernetes, Prometheus, log and graph-memory lookups are also listed when the workspace has them.

## Start work

| Tool | What it does |
| --- | --- |
| `start_scan` | Queue a FinOps, security or drift scan. |
| `run_scan` | Run a scan engine now. |
| `start_compliance` | Queue a compliance assessment. |
| `start_assessment_run` | Queue a coordinated assessment of every configured Azure subscription. |
| `generate_report` | Record a report from the latest scans. |
| `refresh_topology` | Re-read dependency edges from cloud inventory. |

Approving fixes, marking findings benign, settings and API keys are not available through OAuth sign-in; they need the Watchtower portal or an API key with the right scope.
