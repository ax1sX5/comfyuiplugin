# 加载节点模块
from . import ExecCommandNode

# 加载接口路由模块
from . import exec

# 关键修复：将子模块中的节点映射导出到包的顶层
NODE_CLASS_MAPPINGS = ExecCommandNode.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = ExecCommandNode.NODE_DISPLAY_NAME_MAPPINGS

# 导出所有（可选，此为 Python 规范，对 ComfyUI 加载无直接影响）
__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
