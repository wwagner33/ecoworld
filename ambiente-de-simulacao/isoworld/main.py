from Simulator import Simulator

def main():
    game_simulator = Simulator()
    try:
        game_simulator.run()
    except KeyboardInterrupt:
        print("Game interrupted by user.")
    finally:
        game_simulator.shutdown()
        
if __name__ == "__main__":
    main()
