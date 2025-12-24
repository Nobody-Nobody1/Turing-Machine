class TuringMachine:
    def __init__(self, tape_string, blank_symbol, initial_state, final_states, transition_function):
        # Tape implemented as a dictionary to handle "infinite" length
        self.tape = dict(enumerate(tape_string))
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        self.final_states = set(final_states)
        # Transition function is a dictionary: (state, symbol) -> (new_state, new_symbol, direction)
        self.transition_function = transition_function

    def step(self):
        char_under_head = self.tape.get(self.head_position, self.blank_symbol)
        if (self.current_state, char_under_head) in self.transition_function:
            new_state, new_symbol, direction = self.transition_function[(self.current_state, char_under_head)]
            self.tape[self.head_position] = new_symbol
            if direction == "R":
                self.head_position += 1
            elif direction == "L":
                self.head_position -= 1
            self.current_state = new_state
            return True  # Step was successful
        return False # No valid transition, halt

    def run(self):
        while self.step():
            if self.current_state in self.final_states:
                return True # Accepted
        return self.current_state in self.final_states # Check if halted in a final state

    def get_tape_string(self):
        # Helper to visualize the used portion of the tape
        min_used = min(self.tape.keys())
        max_used = max(self.tape.keys())
        return "".join(self.tape.get(i, self.blank_symbol) for i in range(min_used, max_used + 1))