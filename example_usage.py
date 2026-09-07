"""
Demonstration of Bytecode Disassembler Instruction Auditor Skill
"""

from client import BytecodeAuditor

def main():
    print("=== Auditing Python Bytecode Instructions ===")
    auditor = BytecodeAuditor()

    safe_code = """
def calculate_sum(numbers):
    total = 0
    for x in numbers:
        if x > 0:
            total += x
    return total
"""

    unsafe_code = """
def malicious_runner(cmd):
    return eval(cmd)
"""

    print("Auditing Safe Function Bytecode:")
    safe_res = auditor.audit_source_code(safe_code)
    print(f"  Total Instructions: {safe_res['total_instructions']}, Jumps: {safe_res['jump_count']}")
    print(f"  Is Safe: {safe_res['is_safe']}, Flagged: {safe_res['flagged_dangerous_names']}")
    assert safe_res["is_safe"] is True

    print("\nAuditing Unsafe Function Bytecode:")
    unsafe_res = auditor.audit_source_code(unsafe_code)
    print(f"  Total Instructions: {unsafe_res['total_instructions']}")
    print(f"  Is Safe: {unsafe_res['is_safe']}, Flagged: {unsafe_res['flagged_dangerous_names']}")
    assert unsafe_res["is_safe"] is False
    assert "eval" in unsafe_res["flagged_dangerous_names"]

    print("\nBytecode Disassembler Instruction Auditor Verification PASS!")

if __name__ == "__main__":
    main()
