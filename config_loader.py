"""
Docstring for config_loader

Manages the config.txt file, parse all the data
and process the checks of the values
"""

from typing import Any


def check_values(config_data: dict[str, Any]):
    """
    Check the configuration file values
    """
    c = config_data
    if c["HEIGHT"] <= 0:
        raise (Exception, "Height value needs to be at least 1")
    elif c["WIDTH"] <= 0:
        raise (Exception, "Width value needs to be at least 1")


def apply_types(config_data: dict[str, Any]):
    """
    Apply the expected type for each input
    """

    # string_exected_keys = ["OUTPUT_FILE"]
    int_exected_keys = ["WIDTH", "HEIGHT", "SEED"]
    tuple_exected_keys = ["ENTRY", "EXIT"]
    bool_exected_keys = ["PERFECT"]

    for c, v in config_data.items():

        if c in int_exected_keys:
            v = int(v)

        elif c in tuple_exected_keys:
            v = v.split(",")
            v = (v[0], v[1])

        elif c in bool_exected_keys:
            v = bool(v)

    return config_data


def get_config(file_path: str) -> dict[str, str]:
    """
    Get configuration file
    """
    config_data: dict[str, Any] = {}
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

    try:
        apply_types(config_data)
        check_values(config_data)
    except Exception as e:
        print(f"Invalid config file value ! Error: {e}")
        exit()

    return config_data


if __name__ == "__main__":
    exit()
