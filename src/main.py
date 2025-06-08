from src.fireGenerator import FireGenerator
from src.consoleMapLogger import ConsoleMapLogger
from src.mapGenerator import MapGenerator


def main():
    mapGenerator = MapGenerator(width=10, height=10, percentage_of_trees=50)
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
