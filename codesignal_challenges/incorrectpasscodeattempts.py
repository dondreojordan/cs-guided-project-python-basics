"""
One Very Important User (VIU) has a Very Confidential Document (VCD) stored on his Dropbox account. 
He doesn't let anyone see the VCD, especially his roommates who often have access to his devices.

Opening the Dropbox mobile app on the VIU's tablet requires a four-digit passcode. 
To ensure the confidentiality of the stored information, the device is locked out of Dropbox after 10 
consecutive failed passcode attempts. We need to implement a function that, 
given an array of attempts made throughout the day and the correct passcode, 
checks to see if the device should be locked, i.e. 10 or more consecutive failed passcode attempts were made.

Example

For
passcode = "1111" and

attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
the output should be
incorrectPasscodeAttempts(passcode, attempts) = true.

The first attempt is correct, so the user must have successfully logged in. 
However, the next 10 consecutive attempts are incorrect, so the device should be locked. 
Thus, the output should be true.

For
passcode = "1234" and

attempts = ["9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "1234",
            "9999", "9999"]
the output should be
incorrectPasscodeAttempts(passcode, attempts) = false.

There are only 9 consecutive incorrect attempts, so there's no need to lock the device.
"""
############################################### My First Attempt  #########################################################
# def incorrectPasscodeAttempts(passcode, attempts):
#     # :passcode: four digit integer
#     # :attempts: length of number of tries to input the passcode correctly (max 10 attempts)

#     # Create conditional that is there are counts each object consecutively to 10 (attempts)
#     # If the attempt isn't the passcode, keep a count, and print LOCK IT UP
#         # otherwise, reset count, print dont lock it up

#     # :return: boolean, True if device needs to be locked after 10 failed attempts
#     #                   False if device was successfuly logged within 10 attempts
#     return pass

# def incorrectPasscodeAttempts(passcode, attempts):
#     num_attempts = len(attempts)
#     correct = []
#     for attempt in num_attempts:
#         if passcode isin attempts and the attempts[index of range(attempt, attempt+10) of attempts]:
#             answer.append(print("Phone Stays Unlocked!"))
#         else:
#             correct.append(print("LOCK IT UP!"))
#     return correct

##########################################################################################################################
def incorrectPasscodeAttempts(passcode, attempts):
    
    incorrect = 0
    for attempt in attempts:
        if attempt != passcode:
            incorrect += 1
        elif attempt == passcode:
            incorrect = 0
        if incorrect >= 10:
            return print(f"{True} Cellphone LOCKED!")

    return print(f"{False} Cellphone Unlocked...")


if __name__ == "__main__":
    passcode = "1234" 
    attempts = ["9999", "9999",
                "9999", "9999",
                "9999", "9999",
                "9999", "9999",
                "9999", "9999",
                "9999", "9999"]

    print(incorrectPasscodeAttempts(passcode, attempts))
