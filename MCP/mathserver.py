from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

def add(a:int , b:int) -> int:
    """Add two numbers"""
    return a+b

def multiply(a:int , b:int)->int:
    """ Multiply Two numbers."""
    return a*b

"""
the transport = "stdio" arguement tells the server to:

use standard input/output (stdin and stdout) to receive and respond to tool function calls .

"""


if __name__ == "__main__":
    mcp.run(transport="stdio")