#!/usr/bin/env python3
# MuteAvery was here ~:>

# Imports
import base64


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


# Decode JWT data and show user
def jwt_decoding(jwt):
    # Spliting the JWT into its core parts
    jwt_split = jwt.split(".")
    jwt_header = jwt_split[0]
    jwt_payload = jwt_split[1]

    # printing the core parts of the jwt
    print("=" * 30)
    print(f"Original Base64 Header: {jwt_header}")
    print(f"Original Base64 Payload: {jwt_payload}")

    # Converting the jwt to a readable format
    jwt_header_info = base64.b64decode(jwt_header + "==")
    jwt_header_info_str_convert = str(jwt_header_info, "utf-8")
    jwt_payload_info = base64.b64decode(jwt_payload + "==")
    jwt_payload_info_str_convert = str(jwt_payload_info, "utf-8")

    # printing the converted jwt data
    print("=" * 30)
    print(f"Original Header Info: {jwt_header_info_str_convert}")
    print(f"Original Payload Info: {jwt_payload_info_str_convert}")
    print("=" * 30)


# base64 encode the jwt token
def base64url_encode(data: str) -> str:
    return (
        base64.urlsafe_b64encode(data.encode("utf-8"))
        .replace(b"=", b"")
        .decode("utf-8")
    )


# take users header, payload, and signature
def Build_jwt(header: str, payload: str, signature: str | None = None) -> str:
    # base64 encode the header and payload
    header_b64 = base64url_encode(header)
    payload_b64 = base64url_encode(payload)

    # apply the signature if it has one
    if signature:
        jwt = f"{header_b64}.{payload_b64}.{signature}"
    else:
        jwt = f"{header_b64}.{payload_b64}."

    # print the jwt token
    print("=" * 30)
    print("Here is your new jwt token")
    print(jwt)
    print("=" * 30)


def main():
    try:
        banner()
        # main menu for option selection
        print("Main Menu!")
        while True:
            # Menu options
            print("1. Decode JWT token")
            print("2. Craft JWT token")
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
    except KeyboardInterrupt:
        print("\nUser Exited... Goodbye!")


if __name__ == "__main__":
    main()
