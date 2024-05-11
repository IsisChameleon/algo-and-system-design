#
# 1. Identify all possible states and when to transition from one ot the others
# 1. Create an abstract class that has all the actions possible in all the states
# 2. Create children classes for each separate state and implement the actions. Some of the actions are impossible for some states therefore you should produce
#    the right error message etc...
# 3. Create the final "object that has states" class, in our case the ATM. In the init, initialize each state class and initialize
#    the current state to one of them.


from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Literal

class CardDetails(BaseModel):
    card_number: str
    pin: str

class Transaction(BaseModel):
    amount: float
    transaction_type: Literal['withdraw', 'deposit'] 


class ATMState(ABC):
    @abstractmethod
    def insert_card(self, card_details: CardDetails):
        pass

    @abstractmethod
    def eject_card(self):
        pass

    @abstractmethod
    def enter_pin(self, pin: str):
        pass

    @abstractmethod
    def request_transaction(self, transaction: Transaction):
        pass

class NoCardState(ATMState):
    def __init__(self, atm_machine):
        self.atm_machine = atm_machine

    def insert_card(self, card_details: CardDetails):
        print("Card inserted")
        self.atm_machine.card_details = card_details
        self.atm_machine.set_state(self.atm_machine.has_card_state)

    def eject_card(self):
        print("No card in the machine")

    def enter_pin(self, pin: str):
        print("Insert card first")

    def request_transaction(self, transaction: Transaction):
        print("Insert card first")

class HasCardState(ATMState):
    def __init__(self, atm_machine):
        self.atm_machine = atm_machine

    def insert_card(self, card_details: CardDetails):
        print("Card is already inserted")

    def eject_card(self):
        print("Card ejected")
        self.atm_machine.set_state(self.atm_machine.no_card_state)

    def enter_pin(self, pin: str):
        if pin == self.atm_machine.card_details.pin:
            print("PIN correct, transaction can be processed")
            self.atm_machine.set_state(self.atm_machine.authorized_state)
        else:
            print("Incorrect PIN")
            self.eject_card()

    def request_transaction(self, transaction: Transaction):
        print("Enter PIN first")

class AuthorizedState(ATMState):
    def __init__(self, atm_machine):
        self.atm_machine = atm_machine

    def insert_card(self, card_details: CardDetails):
        print("Transaction in process. Eject current card first.")

    def eject_card(self):
        print("Card ejected. Session ended.")
        self.atm_machine.set_state(self.atm_machine.no_card_state)

    def enter_pin(self, pin: str):
        print("PIN already entered")

    def request_transaction(self, transaction: Transaction):
        print(f"Transaction processed: {transaction.transaction_type} of ${transaction.amount}")
        self.eject_card()

class ATM:
    def __init__(self):
        self.no_card_state = NoCardState(self)
        self.has_card_state = HasCardState(self)
        self.authorized_state = AuthorizedState(self)
        self.current_state = self.no_card_state
        self.card_details: CardDetails = None

    def set_state(self, state: ATMState):
        self.current_state = state

    def insert_card(self, card_details: CardDetails):
        self.current_state.insert_card(card_details)

    def eject_card(self):
        self.current_state.eject_card()

    def enter_pin(self, pin: str):
        self.current_state.enter_pin(pin)

    def request_transaction(self, transaction: Transaction):
        self.current_state.request_transaction(transaction)
