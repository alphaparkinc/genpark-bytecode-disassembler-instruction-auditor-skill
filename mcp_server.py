"""
MCP Server for Bytecode Disassembler Instruction Auditor Skill
"""

import json
import sys
from client import BytecodeAuditor

auditor = BytecodeAuditor()

def handle_call(name: str, args: dict) -> dict:
    if name == "audit_bytecode":
        src = args.get("source_code", "")
        try:
            return auditor.audit_source_code(src)
        except Exception as e:
            return {"error": str(e)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
