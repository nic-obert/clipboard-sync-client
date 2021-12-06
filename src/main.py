from sys import argv

import clipboard
from server import Server


def main() -> None:
    hostname = argv[1]
    server = Server((hostname, 50019))
    server.connect()

    clipboard.listen(server.update_clipboard, server.disconnect)


if __name__ == "__main__":
    main()

