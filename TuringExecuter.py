import TuringMachine

initial_state = "init"
accepting_states = ["final"]
transition_rules = {
    ("init", "0"): ("init", "1", "R"),
    ("init", "1"): ("init", "0", "R"),
    ("init", " "): ("final", " ", "N"), # 'N' for No movement (halt)
}

# Create and run the machine
input_string = "010011001"
tm = TuringMachine.TuringMachine(
    tape_string=input_string,
    blank_symbol=" ",
    initial_state=initial_state,
    final_states=accepting_states,
    transition_function=transition_rules
)

print(f"Input on Tape: {tm.get_tape_string()}")
tm.run()
print(f"Result: {tm.get_tape_string()}")
# Output: Input on Tape: 010011001; Result: 101100110