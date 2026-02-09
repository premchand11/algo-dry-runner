import json
from pathlib import Path

def generate_mock_ir():
    """
    TEMPORARY MVP:
    Emits a hardcoded IR snapshot.
    This proves the pipeline, not execution.
    """

    ir = {
        "meta": {
            "language": "cpp",
            "version": "0.1",
            "entry_function": "main"
        },
        "timeline": [
            {
                "step": 1,
                "line": 4,
                "event": "write",
                "stack": [
                    {
                        "frame_id": "f1",
                        "function": "main",
                        "locals": {
                            "sum": {"type": "int", "value": 0}
                        }
                    }
                ],
                "heap": {
                    "arr_1": {
                        "kind": "array",
                        "datatype": "int",
                        "values": [1, 2, 3],
                        "meta": {"size": 3}
                    }
                },
                "references": {
                    "sum": {"ref": "arr_1", "index": 0}
                },
                "globals": {},
                "stdout": [],
                "annotations": []
            }
        ]
    }

    return ir


if __name__ == "__main__":
    output = generate_mock_ir()
    out_path = Path("ir_output.json")
    out_path.write_text(json.dumps(output, indent=2))
    print("IR written to ir_output.json")
