import json
import os
from contextlib import asynccontextmanager
from typing import Any

from dotenv import load_dotenv
from google import genai
from google.genai import types

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()


MODEL = "gemini-3.5-flash"


class CustomerSupportAgent:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env file"
            )

        self.gemini = genai.Client(
            api_key=api_key
        )

    @asynccontextmanager
    async def connect_mcp(self):

        server_params = StdioServerParameters(
            command="uv",
            args=[
                "run",
                "mcp_support.py",
            ],
        )

        async with stdio_client(
            server_params
        ) as streams:

            yield streams

    def convert_mcp_tools_to_gemini(self, mcp_tools):

        declarations = []

        for tool in mcp_tools:

            declaration = {
                "name": tool.name,
                "description": tool.description or "",
                "parameters": tool.inputSchema,
            }

            declarations.append(
                declaration
            )

        return declarations

    async def execute_mcp_tool(
        self,
        session: ClientSession,
        function_call,
    ):

        tool_name = function_call.name

        arguments = function_call.args or {}

        print(f"\n🔧 Tool: {tool_name}")
        print(
            f"📥 Arguments: "
            f"{json.dumps(arguments, indent=2)}"
        )

        result = await session.call_tool(
            tool_name,
            arguments,
        )

        output = []

        for content in result.content:

            if hasattr(content, "text"):
                output.append(content.text)

        tool_output = "\n".join(output)

        print(
            f"📤 Result: {tool_output}"
        )

        return tool_name, tool_output

    async def run_agent_loop(
        self,
        session: ClientSession,
        user_message: str,
    ):

        # -------------------------------------------------
        # 1. Get MCP tools
        # -------------------------------------------------

        tools_response = (
            await session.list_tools()
        )

        gemini_tools = (
            self.convert_mcp_tools_to_gemini(
                tools_response.tools
            )
        )

        print("\n🛠️ Available MCP tools:")

        for tool in tools_response.tools:
            print(
                f"   • {tool.name}"
            )

        # -------------------------------------------------
        # 2. System instruction
        # -------------------------------------------------

        system_instruction = """
You are an autonomous Customer Support Agent.

You have access to customer support MCP tools.

Your responsibilities:

1. Understand the user's request.
2. Search for relevant tickets when necessary.
3. Retrieve complete ticket details before making an update.
4. Never guess a ticket ID.
5. Use MCP tools when database information is required.
6. You may perform multiple tool calls.
7. After receiving a tool result, decide whether another tool is required.
8. Continue until the user's request is completely handled.
9. Give a concise final answer.

For updates:
- First locate the correct ticket.
- Retrieve the ticket details.
- Confirm that it matches the user's request.
- Then update it.
"""

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=user_message
                    )
                ],
            )
        ]

        # -------------------------------------------------
        # 3. Autonomous agent loop
        # -------------------------------------------------

        while True:

            response = (
                self.gemini.models.generate_content(
                    model=MODEL,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        tools=[
                            types.Tool(
                                function_declarations=gemini_tools
                            )
                        ],
                        temperature=0.2,
                    ),
                )
            )

            # -------------------------------------------------
            # No tool requested
            # -------------------------------------------------

            if not response.function_calls:

                print("\n🤖 Agent:")

                print(
                    response.text
                )

                return response.text

            # -------------------------------------------------
            # Add Gemini response to history
            # -------------------------------------------------

            contents.append(
                response.candidates[0].content
            )

            # -------------------------------------------------
            # Execute requested MCP tools
            # -------------------------------------------------

            tool_parts = []

            for function_call in (
                response.function_calls
            ):

                (
                    tool_name,
                    tool_result,
                ) = await self.execute_mcp_tool(
                    session,
                    function_call,
                )

                tool_parts.append(
                    types.Part.from_function_response(
                        name=tool_name,
                        response={
                            "result": tool_result
                        },
                    )
                )

            contents.append(
                types.Content(
                    role="tool",
                    parts=tool_parts,
                )
            )