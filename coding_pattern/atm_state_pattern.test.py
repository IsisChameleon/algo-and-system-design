import unittest
from atm_state_pattern import ATM, NoCardState, HasCardState, AuthorizedState, CardDetails, Transaction

class TestATMStatePattern(unittest.TestCase):

    def test_NoCardState(self):
        atm = ATM()
        no_card_state = NoCardState(atm)
        with self.assertRaisesRegex(Exception, "No card in the machine"):
            no_card_state.eject_card()
        with self.assertRaisesRegex(Exception, "Insert card first"):
            no_card_state.enter_pin('1234')
        with self.assertRaisesRegex(Exception, "Insert card first"):
            no_card_state.request_transaction(Transaction(amount=100, transaction_type='withdraw'))

    def test_HasCardState(self):
        atm = ATM()
        has_card_state = HasCardState(atm)
        with self.assertRaisesRegex(Exception, "Card is already inserted"):
            has_card_state.insert_card(CardDetails(card_number='123456789', pin='1234'))
        # Assuming the card is inserted and the state is set to HasCardState
        atm.current_state = has_card_state
        atm.card_details = CardDetails(card_number='123456789', pin='1234')
        has_card_state.enter_pin('1234')
        self.assertIsInstance(atm.current_state, AuthorizedState)

    def test_AuthorizedState(self):
        atm = ATM()
        authorized_state = AuthorizedState(atm)
        # Assuming the card is inserted, the pin is entered and the state is set to AuthorizedState
        atm.current_state = authorized_state
        atm.card_details = CardDetails(card_number='123456789', pin='1234')
        with self.assertRaisesRegex(Exception, "PIN already entered"):
            authorized_state.enter_pin('1234')
        authorized_state.request_transaction(Transaction(amount=100, transaction_type='withdraw'))
        self.assertIsInstance(atm.current_state, NoCardState)

    def test_ATM(self):
        atm = ATM()
        self.assertIsInstance(atm.current_state, NoCardState)
        atm.insert_card(CardDetails(card_number='123456789', pin='1234'))
        self.assertIsInstance(atm.current_state, HasCardState)
        atm.enter_pin('1234')
        self.assertIsInstance(atm.current_state, AuthorizedState)
        atm.request_transaction(Transaction(amount=100, transaction_type='withdraw'))
        self.assertIsInstance(atm.current_state, NoCardState)

if __name__ == '__main__':
    unittest.main()
