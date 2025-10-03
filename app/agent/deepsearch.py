from typing import List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.prompt.deepsearch import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app.tool import Terminate, ToolCollection
from app.tool.crawl4ai import Crawl4aiTool
from app.tool.web_search import WebSearch


class DeepSearchAgent(ToolCallAgent):
    """A specialized agent for deep web search and content analysis.

    This agent combines web search capabilities with web crawling to perform
    comprehensive research and analysis on any topic. It can:
    - Search the web for relevant information
    - Crawl and extract content from web pages
    - Analyze and synthesize information from multiple sources
    - Provide comprehensive research reports
    """

    name: str = "deepsearch"
    description: str = "A specialized agent for deep web search and content analysis with comprehensive research capabilities"

    system_prompt: str = SYSTEM_PROMPT
    next_step_prompt: str = NEXT_STEP_PROMPT

    # Configure tools for deep search functionality
    available_tools: ToolCollection = ToolCollection(
        WebSearch(),
        Crawl4aiTool(),
        Terminate()
    )

    special_tool_names: List[str] = Field(default_factory=lambda: [Terminate().name])

    # Configure agent parameters for research tasks
    max_steps: int = 15
    max_observe: Optional[int] = 15000  # Allow more content for research

    async def run(self, request: Optional[str] = None) -> str:
        """
        Run the deep search agent with enhanced research capabilities.

        Args:
            request: The research query or topic to investigate

        Returns:
            A comprehensive research report with findings and analysis
        """
        if not request:
            return "No research query provided. Please provide a topic to research."

        # Add research context to the initial request
        research_context = f"""
Research Request: {request}

Please conduct a comprehensive deep search investigation on this topic. Use the following approach:
1. Start with broad web searches to identify key sources and information
2. Crawl relevant web pages to extract detailed content
3. Analyze and synthesize information from multiple sources
4. Provide a comprehensive research report with findings

Begin your investigation now.
"""

        # Run the agent with the enhanced research context
        return await super().run(research_context)
