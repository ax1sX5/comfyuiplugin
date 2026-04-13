import subprocess

class ExecCommandNode:
    CATEGORY = "Exec"
    
    # 必须加这一行！指定执行哪个函数
    FUNCTION = "execute"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "command": ("STRING", {"default": "ls", "multiline": False}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)

    def execute(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            output = result.stdout + result.stderr
            return (output,)
        except Exception as e:
            return (f"Error: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "ExecCommandNode": ExecCommandNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExecCommandNode": "Exec Command"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
