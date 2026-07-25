from engine import start_optimizer


def main() -> None:
    """
    Start the GreenOps optimizer.
    """

    # Show startup message
    print("🚀 GreenOps Optimizer Started", flush=True)

    # Start optimizer
    start_optimizer()


if __name__ == "__main__":
    main()