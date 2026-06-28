from app.agent.state import AgentState


def main():
    state = AgentState(
        query="Create GitHub repository"
    )

    print("Agent State:")
    print(state.model_dump())


if __name__ == "__main__":
    main()