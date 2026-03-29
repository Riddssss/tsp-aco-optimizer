from src.ant_system import ant_system
from src.max_min_as import max_min_as

as_res = ant_system()
mmas_res = max_min_as()

print("=== Ant System ===")
print("Tour:", as_res[0])
print("Length:", as_res[1])
print("Time:", as_res[2])

print("\n=== Max-Min AS ===")
print("Tour:", mmas_res[0])
print("Length:", mmas_res[1])
print("Time:", mmas_res[2])