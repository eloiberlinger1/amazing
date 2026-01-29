"""
Docstring for config_loader

Manages the config.txt file, parse all the data
and process the checks of the values
"""


def load_config(file_path: str) -> dict[str, str]:
    """
    Load configuration file
    """
    config_data: dict[str, str] = {}
    try:
        with open(file_path, "r") as f:
            for li in f:
                li = li.strip()
                if "=" in li:
                    li = li.split("=", 1)
                    key = li[0]
                    config_data[key] = li[1]
    except Exception:
        print("File not found")

    return config_data


if __name__ == "__main__":
    exit()
