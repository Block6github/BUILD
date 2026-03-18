# Antigravity Physics Engine - Version 1.1
def apply_gravity(object_weight, antigravity_enabled=False):
    if antigravity_enabled:
        print("Antigravity Active! Object is weightless.")
        return 0
    
    gravity_constant = 9.8
    force = object_weight * gravity_constant
    print(f"Applying downward force: {force} Newtons")
    return force

# Now testing with Antigravity ON
apply_gravity(83, antigravity_enabled=True)