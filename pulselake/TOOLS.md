# Pulselake MCP tools

The Pulselake MCP server exposes the tools below. Every tool runs with the permissions of the signed-in Pulselake user, in that user's tenant only. Your MCP client always shows the current list.

Hints: **R** read-only, **W** writes data, **D** destructive. All tools act inside the user's Pulselake account.

## Projects and surveys

| Tool | Hint | Description |
| --- | --- | --- |
| `pulselake_list_projects` | R | List one page of Experience Ops projects visible to the signed-in user. |
| `pulselake_survey_expected_fields` | R | Discover survey creation fields and the enabled project type IDs. Requires creation permission. |
| `pulselake_create_survey` | W | Queue AI survey creation. Returns a job. |
| `pulselake_get_survey_job` | R | Read or wait for a survey creation job. Jobs expire after 24 hours. |
| `pulselake_list_surveys` | R | List accessible survey projects, newest first. |
| `pulselake_get_survey` | R | Read survey metadata and sections. |
| `pulselake_list_survey_links` | R | List shareable survey links. |
| `pulselake_list_survey_submissions` | R | List completed, non-test submissions. |
| `pulselake_get_survey_submission` | R | Read one submission and its raw answers. |
| `pulselake_list_survey_submitters` | R | List respondents with qualifying submissions, including names and emails. Anonymous identities are null. |

## Agent Copilots

| Tool | Hint | Description |
| --- | --- | --- |
| `pulselake_list_agents` | R | List one page of accessible Agent projects. |
| `pulselake_get_agent` | R | Get an Agent's details and Copilot settings. |
| `pulselake_chat_with_agent` | W | Chat with an Agent. Supply `chat_name` when starting a new chat, and reuse `conversation_id` for follow-ups. |
| `pulselake_list_agent_chat_files` | R | List file metadata associated with a conversation. |
| `pulselake_upload_agent_chat_file` | W | Upload one file the user selected, up to 512 MB, to an existing conversation. Local server only. |
| `pulselake_update_agent_chat_projects` | D | Add, remove or replace a conversation's project scope. Only on an explicit request. |

Agent authoring, administration and A2A are not available through this server.
