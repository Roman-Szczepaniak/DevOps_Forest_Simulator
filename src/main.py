from fireGenerator import FireGenerator
from consoleMapLogger import ConsoleMapLogger
from mapGenerator import MapGenerator


def main():
    mapGenerator = MapGenerator(width=10, height=10, percentage_of_trees=80)
    mapGenerator.generate()

    logger = ConsoleMapLogger()
    # logger = HtmlLogger()
    print("Carte initiale :")
    logger.log(mapGenerator)

    sim = FireGenerator(mapGenerator)
    sim.start_fire()
    sim.spread()

    print("\nCarte après feu :")
    logger.log(mapGenerator)

if __name__ == "__main__":
    main()
