from customer import Customer
from soda_machine import SodaMachine
import user_interface


class Simulation:
    def __init__(self):
        self.customer = Customer()
        self.soda_machine = SodaMachine()
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                self.soda_machine.begin_transaction(self.customer)
            elif user_option == 2:
                self.customer.check_coins_in_wallet()
            elif user_option == 3:
                self.customer.check_backpack()
            else:
                will_proceed = False
