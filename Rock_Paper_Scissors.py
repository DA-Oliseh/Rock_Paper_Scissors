import random
choices=["rock","paper","scissors"]
player_score=0
computer_score=0
rounds=0
print("=" * 40)
print("🎮 ROCK,PAPER,SCISSORS")
print(("=" * 40))
print("Rules: Rock beats Scissors,Scissors beats Paper,Paper beats Rock")
while True:
    print(f"\n📊 Score: You {player_score} - {computer_score} Computer")
    print(f"📝 round: {rounds +1}")
    #Player's turn
    player=input("\nChoose :Rock,Paper or Scissors(or quit to exit):").lower()
    if player=="quit":
        break
    if player not in choices:
        print("❌ Invalid choice! Please choose Rock,Paper or Scissors")
        continue
    computer=random.choice(choices)
    print(f"🤖 Computer choice: {computer}")
    #Dtermine winner
    if player==computer:
        print("🤝 It's a tie")
        rounds +=1
    elif (player=="rock" and computer=="scissors" or player=="Scissors" and computer=="Paper" or player=="Paper" and computer=="Rock"):
        print("🎉 You win!")
        player_score +=1
        rounds +=1
    else:
        print("💻 Computer wins")
        computer_score += 1
        rounds += 1
    print("\n" + "=" * 40)
    print("🏆 Game Over!")
    print("=" * 40)
    print(f"Final Scores: You {player_score} - {computer_score} Computer")
    print("Total rounds: {rounds}")
    if player_score > computer_score:
        print("🎊Congratulations! You are the champion!")
    elif computer_score > player_score:
        print("💪 Compueter wins!Keep up champ!")
    else:
        print("🤝 The margins were thin!It's an overall tie!")




