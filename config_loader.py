"""
Docstring for config_loader

Manages the config.txt file, parse all the data
and process the checks of the values
"""

from typing import Any


def check_values(c: dict[str, Any]) -> dict[str, Any]:
    """
    Check the configuration file values
    (c => config_data)
    """
    if c["HEIGHT"] <= 0:
        raise BaseException("Height value needs to be at least 1")
    elif c["WIDTH"] <= 0:
        raise BaseException("Width value needs to be at least 1")
    elif (
        c["ENTRY"][0] >= c["HEIGHT"]
        or c["ENTRY"][1] >= c["WIDTH"]
        or c["EXIT"][0] >= c["HEIGHT"]
        or c["EXIT"][1] >= c["WIDTH"]
    ):
        raise BaseException(
            f"Entry or exit must be IN the maze dimensions. "
            f"Maze size: {c['HEIGHT']} rows × {c['WIDTH']}"
            " cols (valid: rows 0-"
            f"{c['HEIGHT']-1}, cols 0-{c['WIDTH']-1}). "
            f"ENTRY={c['ENTRY']}, EXIT={c['EXIT']}. "
        )
    elif (
        c["ENTRY"][0] < 0
        or c["ENTRY"][1] < 0
        or c["EXIT"][0] < 0
        or c["EXIT"][1] < 0
    ):
        raise BaseException("Entry / exit must have positive values Really..?")
    elif c["ENTRY"] == c["EXIT"]:
        raise BaseException("Entry and exit can not be same. Are you stupid ?")

    return c


def apply_types(config_data: dict[str, Any]) -> dict[str, Any]:
    """
    Apply the expected type for each input
    """

    # string_exected_keys = ["OUTPUT_FILE"]
    int_exected_keys = ["WIDTH", "HEIGHT", "SEED"]
    tuple_exected_keys = ["ENTRY", "EXIT"]
    bool_exected_keys = ["PERFECT"]

    for c, v in config_data.items():

        if c in int_exected_keys:
            config_data[c] = int(v)

        elif c in tuple_exected_keys:
            v = v.split(",")
            col = int(v[0].strip())
            row = int(v[1].strip())
            config_data[c] = (row, col)

        elif c in bool_exected_keys:
            # Convert string to proper boolean
            config_data[c] = v.strip().lower() in ("true", "1", "yes", "on")

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
                    li_c = li.split("=", 1)
                    key = li_c[0]
                    config_data[key] = li_c[1]
    except Exception:
        print("File not found")

    apply_types(config_data)
    try:
        check_values(config_data)
    except Exception as e:
        print(f"Invalid config file value ! Error: {e}")
        exit()

    return config_data


if __name__ == "__main__":
    exit()
