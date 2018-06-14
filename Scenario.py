
from Tester import Tester
from Spannerpi import Spannerpi
from Ifttt import Ifttt
import time
import json
BINARY_FROM = "SPANNER"
DEVICE_ID = "250020001047343438323536"
ACCESS_TOKEN = "4be83e75f9856a4f4c573bd17d45b2529b0ba052"
tester = Tester('250020001047343438323536')
spannerpi = Spannerpi()
ifttt = Ifttt()
# D5 -> green led
# D1 -> blue led
# D3 -> button

# Basic Functionality
def B1_validate_button_press():
    # button press
    tester.digitalWrite("OUTPUT", "D3", "LOW")
    tester.setPinMode("D1", "INPUT")

    # check blue led state
    result = tester.digitalRead("D1")

    if (tester.assert_spanner(result) == 1):
        return 0
    else:
        return 1

# Network Tests
def N1_validate_wifi_connect():
    result = spannerpi.connect()

    time.sleep(4)

    # check green led state
    tester.setPinMode("D5", "INPUT")
    value = tester.digitalRead("D5")

    if (tester.assert_spanner(value) == 0):
        return 0
    else:
        return 1

# Network Tests
def N3_validate_wifi_reconnect():
    result = spannerpi.disconnect()

    result = spannerpi.connect()

    time.sleep(60)

    # check green led blinking state
    for i in range(0, 20):
        time.sleep(0.2)
        value = tester.digitalRead("D5")
        if tester.assert_spanner(value) == 0:
            return 0
    return 1

# Network Tests
def N2_validate_wifi_disconnect():
    result = spannerpi.disconnect()

    time.sleep(4)

    # check green led blinking state
    for i in range(0, 10):
        value = tester.digitalRead("D5")

        time.sleep(0.3)

        if tester.assert_spanner(value) == 1:
            return 0
        else:
            return 1

# Cloud Functionality
def C1_validate_ifttt_buttonOn():
    ifttt.buttonOn()

    time.sleep(2)

    # check blue led state
    value = tester.digitalRead("D1")
    if (tester.assert_spanner(value) == 1):
        return 0
    else:
        return 1

# Cloud Functionality
def C2_validate_ifttt_buttonOff():
    ifttt.buttonOff()

    time.sleep(2)

    # check blue led state
    value = tester.digitalRead("D1")
    if (tester.assert_spanner(value) == 0):
        return 0
    else:
        return 1

if __name__ == "__main__":

    EXEC_TEST_CASE(C1_validate_ifttt_buttonOn())



    time.sleep(2)
    print("Welcome nick!")
    EXEC_TEST_CASE(C2_validate_ifttt_buttonOff())
