from time import sleep

from genesis.core.simulation import Simulation


def main():
    simulation = Simulation()

    simulation.set_speed(1)

    simulation.start()
    try:
        sleep(5)
    finally:
        simulation.stop()

    print(simulation)


if __name__ == "__main__":
    main()
