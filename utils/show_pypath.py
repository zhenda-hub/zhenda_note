import sys
import pprint
from pathlib import Path
import pdb


if __name__ == '__main__':
    pprint.pprint(sys.path)

    PJ_DIR = Path(__file__).resolve().parent.parent
    sys.path.append(str(PJ_DIR))

    pprint.pprint(sys.path)
    # pdb.set_trace()
