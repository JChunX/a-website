# Playing Chess with GPT - Part 1. The GPT Gambit

2023/09/20

*Find this project on [Github](https://github.com/JChunX/llm-whisperer/blob/main)*

---

Let's see if we can get GPT to play chess.

At it's core, chess is about  understanding game dynamics, identifying threats and opportunities, and planning ahead. While the internet has endowed GPT with a trove of chess knowledge, can it use its knowledge to actually play well?

## An Agent is Born

Starting from scratch, we create an `agent` and an `environment`. The agent is ChatGPT, and the environment is a chess simulator. We setup simple wrapper classes `OpenAILLM` and `ChessEnv` to interface with `openai` and `python-chess` respectively.

Prior work (source: `r/AnarchyChess`) has shown that GPT is not particularly great at keeping track of piece or even making legal moves. So we prompt it with the availble moves using the engine.

The gruntwork is done in prompt engineering:

```python
player = OpenAILLM(model_name='gpt-4', temperature=1.2, 
                    system_prompt="You are a intelligent agent\
                        whose goal is to win a chess game. \
                        at each step, you are given\
                        a chess board and availble moves. \
                        you must choose a move that will lead to a win.")

player_closing_prompt = "You must make only one move by calling the chess API: \
                        'chess_move(yourmove). \
                         Respond in a concise dictionary' \
                         Example response: \
                         { move: chess_move(e2e4), \
                           reason: 'helps control the center, opens up the bishop, \
                            and allows the queen to move out.', \
                           risks: 'potentially weakens the king side.'}"

env = ChessEnvironment()
board_vector, player_color, legal_moves, img = env.observe()
player_color = "white" if player_color == 1 else "black"
    
while True:
    board_vector, _, legal_moves, img = env.observe()
    board_str = board_vector_to_string(np.array(board_vector))
    legal_moves = [str(move.uci()) for move in legal_moves]
    legal_moves = ", ".join(legal_moves)
    observation_prompt = f"You are playing as {player_color}. \
                           The board is: {board_str}. \
                           Legal moves are: {legal_moves}. \
                           Think step-by-step about your next move."
    observation_prompt += player_closing_prompt

    response = player.generate_responses(observation_prompt)

    print(f"response ({player_color}): {response}")
    move_str = response.split("chess_move(")[1].split(")")[0]
    reward, done = env.step(chess.Move.from_uci(move_str))
    print(f"you played {move_str}. reward: {reward}. done: {done}")
    print(env.board)

    if done:
        print("game over")
        break
```

We set it loose on a game with Stockfish, and the result is... not great.

<img src="/static/images/gpt-gambit.gif" alt="gpt-gambit" width="400"/>

*holy hell*

Thanks to its natural knowledge of chess, GPT is able to make a few moves that resembled an opening. However, it quickly falls apart, blundering a bishop, two knights, and a queen before getting checkmated.

## The GPT Gambit

Let's take a closer look at a move by GPT (Black, lowercase)

```
input: 

r . b q k . n r
p p p p . p p p
. . n . . . . .
. . b . N . . .
. . . . P . . .
. . N . . . . .
P P P P . P P P
R . B Q K B . R

response (black): { "move": "chess_move(c5f2)", 
                    "reason": "Potential check to opponent's king, 
                               increases control of center, pressures both
                               rooks due to the jeopardized position of king.", 
                    "risks": "Bishop becomes a target and faces potential counter 
                              attack, opening where detachment from other 
                              pieces could lead to being captured." }
                              
you played c5f2+.
engine plays e1f2.

result:

r . b q k . n r
p p p p . p p p
. . n . . . . .
. . . . N . . .
. . . . P . . .
. . N . . . . .
P P P P . K P P
R . B Q . B . R
```

Even though GPT knew `c5f2` would put the king in check and understood that the bishop would become vulnerable, it still made the move. Despite the immense language capabilities of GPT, it still lacks the ability to plan and precisely reason about the game!

So what can we do about this?

## The Plan

The plan, is to make GPT plan. 

To improve GPT's ability to play chess, We should prompt the agent to explicitly reason about future trajectories and their outcomes. Just as human players think carefully before making a move, there should be built-in mechanisms for GPT to do the same.