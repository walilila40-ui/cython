import sys
import importlib

def main():
    version = f"{sys.version_info.major}.{sys.version_info.minor}"

    if version == "3.11":
        module_name = "TRRT11"
    elif version == "3.13":
        module_name = "RTTR"
    else:
        print(f"Unsupported Python version: {version}")
        print("Supported: Python 3.11 / 3.13")
        return

    try:
        mod = importlib.import_module(module_name)

        if hasattr(mod, "main"):
            mod.main()
        elif hasattr(mod, "menu"):
            mod.menu()
        else:
            print(f"{module_name}.so loaded, but no main/menu function found.")
            print("Available:", [x for x in dir(mod) if not x.startswith("_")])

    except Exception as e:
        print(f"Failed to load {module_name}.so")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
