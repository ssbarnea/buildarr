# Allow execution of buildarr as a module: python3 -m buildarr
from __future__ import annotations

from buildarr.cli.main import main

if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
