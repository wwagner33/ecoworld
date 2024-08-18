from Simulator import Simulator
from SimulatorThings.map_editor import MapMaker

def main():
    game_simulator = Simulator("./ecoworld/simulation00.json")
    # map_editor = MapMaker()
    try:
        # map_editor.run()
        game_simulator.run()
    except KeyboardInterrupt:
        print("Game interrupted by user.")
    # except Exception as err:
    #     print(err)
    # finally:
    #     game_simulator.shutdown()
        
if __name__ == "__main__":
    main()
