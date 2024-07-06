from Simulator import Simulator

def main():
    game_simulator = Simulator("simulation00.json")
    try:
        game_simulator.run()
    except KeyboardInterrupt:
        print("Game interrupted by user.")
    # except Exception as err:
    #     print(err)
    # finally:
    #     game_simulator.shutdown()
        
if __name__ == "__main__":
    main()
