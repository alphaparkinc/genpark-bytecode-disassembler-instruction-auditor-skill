# GenPark Bytecode Disassembler Instruction Auditor Skill

Python bytecode inspection and opcode auditor evaluating instruction safety and control-flow jumps.

Find more agent tools at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph LR
    A[Source Code] --> B[compile to Code Object]
    B --> C[dis.get_instructions]
    C --> D[Scan LOAD_NAME & LOAD_GLOBAL]
    C --> E[Count Branch JUMP Opcodes]
    D & E --> F{Audit Pass?}
    F -->|Clean| G[Safe for Execution]
    F -->|Dangerous Token| H[Block Untrusted Bytecode]
```

## Features
- In-memory opcode disassembly with standard library `dis`.
- Detection of dangerous dynamic execution builtins.
- Zero external dependencies.
