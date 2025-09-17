from mcp.server.fastmcp import FastMCP

mcp=FastMCP("calculator")


@mcp.tool()
def add(a:float, b:float)-> float:
    """Add Two numbers"""
    return a+b

@mcp.tool()
def subtract(a:float, b:float)-> float:
    """Subtract Two numbers"""
    return a-b 

@mcp.tool()
def multiply(a:float, b:float)-> float:
    """Multiply Two numbers"""
    return a*b  

@mcp.tool()
def divide(a:float, b:float)-> float:
    """Divide Two numbers"""
    if b==0:
        return "Error: Division by zero"
    return a/b

@mcp.tool()
def power(a:float, b:float)-> float:
    """Power of a number"""
    return a**b

@mcp.tool()
def sqrt(a:float)-> float:
    """Square root of a number"""
    if a<0:
        return "Error: Square root of negative number"
    return a**0.5

@mcp.tool()
def factorial(a:int)-> int:
    """Factorial of a number"""
    if a<0:
        return "Error: Factorial of negative number"
    if a==0 or a==1:
        return 1
    result=1
    for i in range(2,a+1):
        result*=i
    return result

@mcp.tool()
def log(a:float, base:float=10)-> float:
    """Logarithm of a number"""
    import math
    if a<=0:
        return "Error: Logarithm of non-positive number"
    if base<=1:
        return "Error: Logarithm base must be greater than 1"
    return math.log(a, base)

@mcp.tool()
def sin(a:float)-> float:
    """Sine of an angle in degrees"""
    import math
    return math.sin(math.radians(a))

@mcp.tool()
def cos(a:float)-> float:
    """Cosine of an angle in degrees"""
    import math
    return math.cos(math.radians(a))

@mcp.tool()
def tan(a:float)-> float:
    """Tangent of an angle in degrees"""
    import math
    return math.tan(math.radians(a))


if __name__=="__main__":
    mcp.run(transport="stdio")