from core.brain import Brain


def main():
    nous = Brain()

    nous.think("Go to the kitchen")

    nous.remember("owner", "Sotsai")

    print(nous.recall("owner"))

    nous.act()

    print(nous.status())


if __name__ == "__main__":
    main()
