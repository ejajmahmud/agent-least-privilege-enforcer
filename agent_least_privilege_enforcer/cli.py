"""CLI for Least Privilege Enforcer."""
import argparse
from .core import LeastPrivilegeEnforcer, AgentRole

def main():
    parser = argparse.ArgumentParser(description="Agent Least Privilege Enforcer CLI")
    parser.add_argument("--role", default="researcher", help="Agent role (researcher, coder, admin)")
    parser.add_argument("--tool", default="delete_database", help="Tool to check")
    parser.add_argument("--action", default="write", help="Action type (read, write, execute)")
    args = parser.parse_args()

    enforcer = LeastPrivilegeEnforcer()
    ok = enforcer.check_permission(args.role, args.tool, args.action)
    print(f"Role '{args.role}' attempting '{args.tool}' ({args.action}): Allowed={ok}")

if __name__ == "__main__":
    main()
