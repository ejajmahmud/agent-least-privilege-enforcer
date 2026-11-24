"""Core Least Privilege Enforcer implementation."""
from typing import Dict, Any, Set, List

class AgentRole:
    RESEARCHER = "researcher"
    CODER = "coder"
    ADMIN = "admin"

class SecurityPolicy:
    def __init__(self, allowed_tools: Set[str], allowed_actions: Set[str]):
        self.allowed_tools = allowed_tools
        self.allowed_actions = allowed_actions

class LeastPrivilegeEnforcer:
    def __init__(self):
        self.role_policies: Dict[str, SecurityPolicy] = {
            AgentRole.RESEARCHER: SecurityPolicy(
                allowed_tools={"search_web", "read_file", "summarize"},
                allowed_actions={"read", "query"}
            ),
            AgentRole.CODER: SecurityPolicy(
                allowed_tools={"read_file", "write_file", "run_tests"},
                allowed_actions={"read", "write", "execute"}
            ),
            AgentRole.ADMIN: SecurityPolicy(
                allowed_tools={"*"},
                allowed_actions={"*"}
            )
        }

    def check_permission(self, role: str, tool_name: str, action: str) -> bool:
        policy = self.role_policies.get(role)
        if not policy:
            return False

        tool_ok = ("*" in policy.allowed_tools) or (tool_name in policy.allowed_tools)
        action_ok = ("*" in policy.allowed_actions) or (action in policy.allowed_actions)
        return tool_ok and action_ok
