import re, sys
from . import launch_selenium as ls

safetyDomains = ['mc-anpi.com']
urlPattern = "(?:https?:\/\/(?:[\w\d]+\.)*){0}\S+"

def parseMessageBody(body: str) -> str | None:
    for url in safetyDomains:
        rstr = urlPattern.format(url)
        m = re.search(rstr, body)
        if m is not None:
            res = m.group(0)
            return res
    return None

def main() -> int:
    inp = sys.argv[1]
    url = parseMessageBody(inp)
    print(url)
   

if __name__ == "__main__":
    sys.exit(main())