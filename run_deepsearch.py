#!/usr/bin/env python3
"""
DeepSearch Agent Runner

A simple script to run the DeepSearch agent for comprehensive web research.
"""

import asyncio
import sys
from typing import Optional

from app.agent.deepsearch import DeepSearchAgent
from app.logger import logger


async def main():
    """Main function to run the DeepSearch agent."""
    if len(sys.argv) < 2:
        print("Usage: python run_deepsearch.py <research_query>")
        print("Example: python run_deepsearch.py 'artificial intelligence trends 2024'")
        sys.exit(1)

    # Get the research query from command line arguments
    research_query = " ".join(sys.argv[1:])

    logger.info(f"🔍 Starting DeepSearch research on: {research_query}")

    try:
        # Create and run the DeepSearch agent
        agent = DeepSearchAgent()
        result = await agent.run(research_query)

        print("\n" + "="*80)
        print("DEEPSEARCH RESEARCH REPORT")
        print("="*80)
        print(result)
        print("="*80)

    except Exception as e:
        logger.error(f"❌ DeepSearch failed: {e}")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
