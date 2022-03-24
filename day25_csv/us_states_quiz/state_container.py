import pandas


class StateContainer:

    def __init__(self):
        self.data = pandas.read_csv('50_states.csv')

    def check_if_state_exists(self, state_name):
        if state_name in self.data.state.to_list():
            return True
        return False

    def get_state_coords(self, state_name):
        state_data = self.data[self.data.state == state_name]
        return int(state_data.x), int(state_data.y)