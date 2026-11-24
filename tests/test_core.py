"""Tests for LeastPrivilegeEnforcer."""
import unittest
from agent_least_privilege_enforcer.core import LeastPrivilegeEnforcer, AgentRole

class TestLeastPrivilegeEnforcer(unittest.TestCase):
    def setUp(self):
        self.enforcer = LeastPrivilegeEnforcer()

    def test_researcher_privileges(self):
        self.assertTrue(self.enforcer.check_permission(AgentRole.RESEARCHER, "read_file", "read"))
        self.assertFalse(self.enforcer.check_permission(AgentRole.RESEARCHER, "write_file", "write"))

    def test_admin_privileges(self):
        self.assertTrue(self.enforcer.check_permission(AgentRole.ADMIN, "drop_table", "delete"))
