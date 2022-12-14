from Combo_Lock import ComboLock


def test_correct_combo_lock1():
    lock = ComboLock(3, 11, 3)
    assert str(lock) == 'ComboLock(3, 11, 3)'
    assert not lock.open()

    print("All possible format of a correct combination")
    print("\nlock should open - correct combination")
    lock.reset()
    lock.turn_right(3)
    lock.turn_left(11)
    lock.turn_right(3)
    assert lock.open()

    print("\nlock should open - rotate more that one rotation but still get the same combination")
    lock.reset()
    lock.turn_right(43)
    lock.turn_left(51)
    lock.turn_right(83)
    assert lock.open()

    print("\nlock should open - basic with reset in the middle")
    lock.reset()
    lock.turn_right(35)
    lock.turn_left(7)
    lock.reset()
    lock.turn_right(3)
    lock.turn_left(11)
    lock.turn_right(3)
    assert lock.open()


def test_wrong_combo_lock1():
    lock = ComboLock(3, 11, 3)
    assert str(lock) == 'ComboLock(3, 11, 3)'  # __repr__
    assert not lock.open()

    print("\nAll possible format of wrong combination.")
    print("lock should not open - wrong combination")
    lock.reset()
    lock.turn_right(12)
    lock.turn_left(11)
    lock.turn_right(3)
    assert not lock.open()

    print("lock should not open - rotate more that one rotation but did not get the same combination")
    lock.reset()
    lock.turn_right(103)
    lock.turn_left(400)
    lock.turn_right(73)
    assert not lock.open()


def test():
    # test_combo_lock1()
    test_correct_combo_lock1()
    test_wrong_combo_lock1()
    print('passed all test cases...')


test()  # test my ComboLock class
