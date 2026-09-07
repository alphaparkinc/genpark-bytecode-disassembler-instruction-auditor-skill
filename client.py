"""
Bytecode Disassembler Instruction Auditor Skill Client
Pure Python Standard Library implementation of bytecode introspection (using dis module).
Analyzes compiled code objects, audits opcode safety, measures cyclomatic branch complexity,
and verifies absence of dangerous low-level instructions before execution.
"""

import dis
import types
from typing import List, Dict, Any, Tuple, Set


class BytecodeAuditor:
    DANGEROUS_NAMES = {"eval", "exec", "compile", "__import__", "globals", "locals"}

    def __init__(self):
        pass

    def audit_code_object(self, code_obj: types.CodeType) -> Dict[str, Any]:
        instructions = list(dis.get_instructions(code_obj))
        opnames = [i.opname for i in instructions]
        loaded_names = {i.argval for i in instructions if i.opname in ["LOAD_NAME", "LOAD_GLOBAL"]}

        # Check for dangerous global calls
        flagged_names = list(loaded_names.intersection(self.DANGEROUS_NAMES))

        # Count branch jump instructions (cyclomatic complexity proxy)
        jumps = [i for i in instructions if "JUMP" in i.opname]

        return {
            "total_instructions": len(instructions),
            "distinct_opcodes": len(set(opnames)),
            "jump_count": len(jumps),
            "loaded_names": list(loaded_names),
            "flagged_dangerous_names": flagged_names,
            "is_safe": len(flagged_names) == 0
        }

    def audit_source_code(self, source_code: str) -> Dict[str, Any]:
        code_obj = compile(source_code, filename="<audit>", mode="exec")
        return self.audit_code_object(code_obj)
