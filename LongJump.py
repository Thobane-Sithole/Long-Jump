def get_competitors():
    competitors = []
    print("Please enter the names of competitors. (Press enter when done.)")
    i = 1
    while True:
        name = input(f"Competitor no. {i}: ").strip()
        if not name:
            break
        competitors.append(name)
        i += 1
    return competitors

def get_jumps(name):
    jumps = []
    print(f"\nCompetitor {name}:")
    for i in range(1, 4):
        while True:
            jump = input(f"Attempt {i}: ").lower()
            if jump == "foul" or (jump.replace(".", "").isdigit() and float(jump) > 0):
                jumps.append(jump)
                break
            else:
                print("Invalid input. Please enter a positive number or 'Foul'.")
    return jumps

def best_jump(jumps):
    valid_jumps = [float(j) for j in jumps if j != "foul"]
    return max(valid_jumps) if valid_jumps else "No jump"

def print_results(results):
    print("\nCompetitor\tLongest Distance")
    for name, distance in results.items():
        print(f"{name}\t\t{distance}")

def find_winner(results):
    valid_results = {name: dist for name, dist in results.items() if dist != "No jump"}
    if valid_results:
        winner = max(valid_results, key=valid_results.get)
        return winner, valid_results[winner]
    return None, None

def main():
    print("***** Long Jump Information System *****")
    
    competitors = get_competitors()
    
    results = {}
    print("\nPlease enter the distances for each competitor.")
    for competitor in competitors:
        jumps = get_jumps(competitor)
        results[competitor] = best_jump(jumps)
    
    print_results(results)
    
    winner, winning_distance = find_winner(results)
    if winner:
        print(f"\nThe winner is {winner} with a jump of {winning_distance}.")
    else:
        print("\nNo valid jumps were recorded.")

if __name__ == "__main__":
    main()