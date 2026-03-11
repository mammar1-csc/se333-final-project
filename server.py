from fastmcp import FastMCP
import xml.etree.ElementTree as ET

mcp = FastMCP("SE333 Testing Agent")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool
def parse_jacoco(path: str):
    """Parse JaCoCo XML coverage report"""
    tree = ET.parse(path)
    root = tree.getroot()

    coverage = {}

    for counter in root.findall("counter"):
        type = counter.attrib["type"]
        covered = int(counter.attrib["covered"])
        missed = int(counter.attrib["missed"])
        total = covered + missed

        percent = (covered / total) * 100 if total > 0 else 0
        coverage[type] = round(percent, 2)

    return coverage


@mcp.tool
def suggest_tests(coverage: dict):
    """Suggest where tests should be added"""
    if coverage.get("LINE", 0) < 80:
        return "Add more tests to increase line coverage."
    if coverage.get("BRANCH", 0) < 80:
        return "Add edge-case tests for branches."
    return "Coverage looks good."


if __name__ == "__main__":
    mcp.run(transport="sse")
