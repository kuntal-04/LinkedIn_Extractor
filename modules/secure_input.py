import sys

#This file has 2 versions of code because keyword input is handled differently on each OS. 
# Windows
if sys.platform == "win32":
    import msvcrt  #msvcrt is Windows-only module that lets Python read keyboard characters one by one.

    def masked_input(prompt="Password: "):
        print(prompt, end="", flush=True)   #flush = true, ensures that the prompt is printed immediately without buffering, which is important for a smooth user experience when entering a password.
        password = ""

        while True:
            char = msvcrt.getch()

            if char in {b"\r", b"\n"}:   #b because user types in bytes, not string. This checks if user pressed Enter key to finish input. If so, it breaks the loop and returns the password.
                print("")
                break

            elif char == b"\x08":  # backspace
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)

            else:
                password += char.decode("utf-8")
                print("*", end="", flush=True)

        return password

# Linux / Mac
else:
    import tty, termios   #this allows raw keyboard input on Unix-based systems, enabling us to read characters one by one, which is essential for securely entering passwords.

    def masked_input(prompt="Password: "):
        print(prompt, end="", flush=True)
        password = ""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)    #stores current terminal configuration. 

        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)   #reads one character at a time.

                if ch in ("\r", "\n"):
                    print("")
                    break

                elif ch == "\x7f":  # backspace
                    if len(password) > 0:
                        password = password[:-1]
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()

                else:
                    password += ch
                    sys.stdout.write("*")
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return password
