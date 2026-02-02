#!/usr/bin/env python3
# MuteAvery was here ~:>

# Imports
import base64
from re import error


# banner for the tool
def banner():
    CYAN = "\033[0;36m"
    END = "\033[0m"
    banner = f"""{CYAN}
     ██╗██╗    ██╗████████╗    ███████╗██╗   ██╗██████╗  ██████╗ ███████╗ ██████╗ ███╗   ██╗
     ██║██║    ██║╚══██╔══╝    ██╔════╝██║   ██║██╔══██╗██╔════╝ ██╔════╝██╔═══██╗████╗  ██║
     ██║██║ █╗ ██║   ██║       ███████╗██║   ██║██████╔╝██║  ███╗█████╗  ██║   ██║██╔██╗ ██║
██   ██║██║███╗██║   ██║       ╚════██║██║   ██║██╔══██╗██║   ██║██╔══╝  ██║   ██║██║╚██╗██║
╚█████╔╝╚███╔███╔╝   ██║       ███████║╚██████╔╝██║  ██║╚██████╔╝███████╗╚██████╔╝██║ ╚████║
 ╚════╝  ╚══╝╚══╝    ╚═╝       ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
    {END} 
    """
    print(banner)


# help menu for tool
def help_menu():
    YELLOW = "\033[1;33m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    END = "\033[0m"

    menu = f""" 
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  					                  JWT SURGEON                       					                             ║
║ {YELLOW}Section 1 the main menu{END}                                                                     								     ║
║         			                    													     ║	
║  The main menu is a simple cli menu,															     ║
║  First select your option (enter the number in front of the option).  						                                     ║
║  Once you have selected your option you will be greeted with that options needed information (i,e the encoded jwt token).                                  ║
║  If you are worried about having to rerun jwt surgeon to then edit the decoded jwt values,                                                                 ║
║  JWT surgeon will allow you to select the jwt build option straight after decoding your encoded JWT token (or you can decode another jwt token).           ║
║																	                     ║	 
║ {PURPLE}Section 2 JWT decoding{END}                                                                                                                                     ║														
║                                  			                          									     ║
║  JWT Surgeon allows you to decode a given base6 encoded jwt token.											     ║
║  All you need to do is supply the full jwt token when prompted (be sure to submit it as one line).							     ║
║  After which you will be shown the original jwt heaer and payload encoded and underneath that the decoded data. 					     ║
║																			     ║
║  {CYAN}Section 3 JWT building/editing{END}                     													     ║
║															     				     ║
║  JWT surgeon allows you to edit and build new JWT tokens.												     ║	
║  As with the Decoding feature all you are required to do is submit the needed JWT data (header,payload and signature if needed).			     ║	
║  JWT surgeon will then craft your new token!														     ║
║   						       													     ║
║						                                                                                                             ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    
    """
    print(menu)


# Decode JWT data and show user
def jwt_decoding(jwt):
    try:
        # Spliting the JWT into its core parts
        jwt_split = jwt.split(".")
        jwt_header = jwt_split[0]
        jwt_payload = jwt_split[1]

        # printing the core parts of the jwt
        print("=" * 50)
        print(f"Original Base64 Header: {jwt_header}")
        print(f"Original Base64 Payload: {jwt_payload}")
        print("=" * 50)

        # Converting the jwt to a readable format
        jwt_header_info = base64.b64decode(jwt_header + "==")
        jwt_header_info_str_convert = str(jwt_header_info, "utf-8")
        jwt_payload_info = base64.b64decode(jwt_payload + "==")
        jwt_payload_info_str_convert = str(jwt_payload_info, "utf-8")

        # printing the converted jwt data
        print("=" * 50)
        print(f"Original Header Info: {jwt_header_info_str_convert}")
        print(f"Original Payload Info: {jwt_payload_info_str_convert}")
        print("=" * 50)
    except IndexError as e:
        print(f"\nError JWT is too small! Please resubmit your JWT: {e}")
    except ValueError as e:
        print(f"\nError ValueError: {e}")
    except Exception as e:
        print(f"\nError Unknown: {e}")


# base64 encode the jwt token
def base64url_encode(data: str) -> str:
    try:
        return (
            base64.urlsafe_b64encode(data.encode("utf-8"))
            .replace(b"=", b"")
            .decode("utf-8")
        )
    except Exception as e:
        print(f"Error encoding JWT: {e}")


# take users header, payload, and signature
def Build_jwt(header: str, payload: str, signature: str | None = None) -> str:
    try:
        # base64 encode the header and payload
        header_b64 = base64url_encode(header)
        payload_b64 = base64url_encode(payload)

        # apply the signature if it has one
        if signature:
            jwt = f"{header_b64}.{payload_b64}.{signature}"
        else:
            jwt = f"{header_b64}.{payload_b64}."

        # print the jwt token
        print("=" * 50)
        print("Here is your new jwt token")
        print(jwt)
        print("=" * 50)
    except Exception as e:
        print(f"Error Unknown {e}")


# Main
def main():
    try:
        banner()
        # main menu for option selection
        print("Main Menu!")
        while True:
            # Menu options
            print("\n1. Decode JWT token")
            print("2. Craft JWT token")
            print("9. help menu")
            print("0. Exit")

            # Take users choice
            try:
                choice = int(input("Select your choice: "))
            except ValueError:
                print("\nInput Error! Please select a number")
                continue

            # match the users choice to the correct functiona
            match choice:
                case 1:
                    jwt = input("Please supply your *Encoded* JWT token here ~> ")
                    jwt_decoding(jwt)

                case 2:
                    header = input("Please enter the JWT header here (json) ~> ")
                    payload = input("Pleae enter the JWT payload (json) ~> ")
                    signature = input(
                        "Please enter the JWT signature (empty if none) ~> "
                    )
                    signature = signature if signature.strip() else None
                    Build_jwt(header, payload, signature)

                case 0:
                    print("Goodbye!")
                    break
                case 9:
                    help_menu()
                    print("\n")
                case _:
                    print("Unknown option Please choose again!")
                    continue

    except KeyboardInterrupt:
        print("\nUser Exited... Goodbye!")


if __name__ == "__main__":
    main()
