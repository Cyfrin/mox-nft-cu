import base64

from src import mood_nft


def deploy_mood_nft():
    happy_svg_uri = ""
    sad_svg_uri = ""
    with open("./images/dynamic/happy.svg", "r") as f:
        happy_svg = f.read()
        happy_svg_uri = svg_to_base64_uri(happy_svg)
    with open("./images/dynamic/sad.svg", "r") as f:
        sad_svg = f.read()
        sad_svg_uri = svg_to_base64_uri(sad_svg)

    mood_nft_contract = mood_nft.deploy(happy_svg_uri, sad_svg_uri)
    print(f"Deployed mood NFT to {mood_nft_contract.address}")
    mood_nft_contract.mint_nft()
    print(mood_nft_contract.tokenURI(0))
    return mood_nft_contract


def moccasin_main():
    return deploy_mood_nft()


def svg_to_base64_uri(svg_content: str) -> str:
    """
    Convert SVG content to a base64-encoded data URI.

    Args:
        svg_content (str): The SVG content as a string

    Returns:
        str: Base64-encoded data URI for the SVG
    """
    svg_bytes = svg_content.encode("utf-8")
    base64_svg = base64.b64encode(svg_bytes).decode("utf-8")
    return f"data:image/svg+xml;base64,{base64_svg}"


# HAPPY_SVG_URI= "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgIGhlaWdodD0iNDAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgZmlsbD0ieWVsbG93IiByPSI3OCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPGcgY2xhc3M9ImV5ZXMiPgogICAgPGNpcmNsZSBjeD0iNjEiIGN5PSI4MiIgcj0iMTIiLz4KICAgIDxjaXJjbGUgY3g9IjEyNyIgY3k9IjgyIiByPSIxMiIvPgogIDwvZz4KICA8cGF0aCBkPSJtMTM2LjgxIDExNi41M2MuNjkgMjYuMTctNjQuMTEgNDItODEuNTItLjczIiBzdHlsZT0iZmlsbDpub25lOyBzdHJva2U6IGJsYWNrOyBzdHJva2Utd2lkdGg6IDM7Ii8+Cjwvc3ZnPg=="
# SAD_SVG_URI = "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgaGVpZ2h0PSI0MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiBmaWxsPSJ5ZWxsb3ciIHI9Ijc4IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMiLz4KICA8ZyBjbGFzcz0iZXllcyI+CiAgICA8Y2lyY2xlIGN4PSI3MCIgY3k9IjgyIiByPSIxMiIvPgogICAgPGNpcmNsZSBjeD0iMTI3IiBjeT0iODIiIHI9IjEyIi8+CiAgPC9nPgogIDxwYXRoIGQ9Ik01NSAxNDBjMTcuNDEtNDIuNzMgODIuMjEtMjYuOSA4MS41Mi0uNzMiIHN0eWxlPSJmaWxsOm5vbmU7IHN0cm9rZTogYmxhY2s7IHN0cm9rZS13aWR0aDogMzsiLz4KPC9zdmc+"
