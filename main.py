import asyncio

from mcp import ClientSession

from agent import CustomerSupportAgent


async def main():

    print("=" * 65)
    print("        🎧 CUSTOMER SUPPORT AI AGENT")
    print("=" * 65)

    print()
    print("The agent can:")
    print("  🔎 Search tickets")
    print("  📄 Retrieve ticket details")
    print("  ✏️ Update tickets")
    print("  ➕ Create tickets")
    print("  🔄 Perform multi-step tasks")
    print()
    print("Type 'exit' to quit.")
    print("=" * 65)

    agent = CustomerSupportAgent()

    async with agent.connect_mcp() as (
        read_stream,
        write_stream,
    ):

        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            await session.initialize()

            print("\n✅ MCP server connected")

            while True:

                try:

                    user_input = input(
                        "\n👤 You: "
                    ).strip()

                except (
                    KeyboardInterrupt,
                    EOFError,
                ):

                    print("\n\nGoodbye!")
                    break

                if not user_input:
                    continue

                if user_input.lower() in {
                    "exit",
                    "quit",
                }:

                    print("\n👋 Goodbye!")
                    break

                try:

                    await agent.run_agent_loop(
                        session,
                        user_input,
                    )

                except Exception as e:

                    print(
                        f"\n❌ Error: {e}"
                    )


if __name__ == "__main__":
    asyncio.run(main())