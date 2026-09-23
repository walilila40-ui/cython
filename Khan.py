import RTTR

if hasattr(RTTR, "menu"):
    RTTR.menu()
else:
    print("ERROR: RTTR.menu() not found")
    print("Available:", [x for x in dir(RTTR) if not x.startswith("_")])
