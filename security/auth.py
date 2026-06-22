ROLE_PERMISSIONS = {
    "admin": ["read", "write"],
    "employee": ["read"]
}

def can_access(role, action):
    return action in ROLE_PERMISSIONS.get(role, [])