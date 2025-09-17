from mcp.server.fastmcp import FastMCP
from typing import List
import os

TEXT_FOLDER="docs"


mcp=FastMCP("filesearch")

@mcp.tool()
def search_file(keyword: str, ) -> List[str]:
    matching_files = []
    for file_name in os.listdir(TEXT_FOLDER):
        if file_name.endswith(".txt"):
            file_path = os.path.join(TEXT_FOLDER, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    matching_files.append(file_name)
    return matching_files

if __name__ == "__main__":
    mcp.run(transport="streamable_http")