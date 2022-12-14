# name: Villas, Justin Lawrence DL.
#lab: 3.4
#purpose: OOP
# -------------------------------------------------------------------------
class ComboLock:

    # ------------------------------------------------------------------
    # purpose: initilize the variables that will be used
    # parameter: secret 1,2,3 are the ints for the combonation of the lock
    # return:    none
    def __init__(self, secret1, secret2, secret3):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3
        self.reveal_Open_Combo = [secret1, secret2, secret3]
        self.guessed_Combo = []

    # ------------------------------------------------------------------
    # purpose: reset the value of the guessed combo to empty set [].
    #parameter: none
    # return:    none

    def reset(self):
        self.guessed_Combo = []

    # -----------------------------------------------------------------
    # purpose:  create string repr of class
    #parameter: none
    # return:    comboEntered: the 3 ints that make up the combonation

    def __repr__(self):
        comboEntered = 'ComboLock({}, {}, {})'.format(
            self.secret1, self.secret2, self.secret3)
        return comboEntered

    # -----------------------------------------------------------------
    # purpose:   turn to the left
    # parameter: ticks: number of turn/s  to the left
    # return:    self.guessed_Combo.append(user_left_insert) - insert user_left_insert value to guessed_Combo list.

    def turn_left(self, ticks):
        user_left_insert = ticks % 40
        return self.guessed_Combo.append(user_left_insert)

    # -----------------------------------------------------------------
    # purpose: turn to the right
    # parameters: ticks: number of turn/s  to the right
    # return : self.guessed_Combo.append(user_right_inser) - insert user_right_inser to guessed_Combo list.
    def turn_right(self, ticks):
        user_right_insert = ticks % 40
        return self.guessed_Combo.append(user_right_insert)

    # -----------------------------------------------------------------
    # purpose: checks if the lock is open by comparing reveal_Open_Combo,
    #         list with guessed combo list
    #parameters: none
    # return:  True (self.reveal_Open_Combo == self.guessed_Combo)

    def open(self):
        print("guess", self.guessed_Combo)
        print("correct_combination", self.reveal_Open_Combo)
        return (self.reveal_Open_Combo == self.guessed_Combo)
