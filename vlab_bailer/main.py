import requests
import pandas as pd
from time import sleep
import argparse

BOTSERVER_URL = "https://fly-botserver.vlab.digital"


def bailout(user, page, form):
    dat = {
        "event": {"type": "bailout", "value": {"form": form}},
        "user": str(user),
        "page": str(page),
    }

    return dat


def post_bail(dat):
    sleep(1)
    res = requests.post(f"{BOTSERVER_URL}/synthetic", json=dat)
    return res


def main(path: str):
    df = pd.read_csv(
        path, dtype={"user": "string", "page": "string", "shortcode": "string"}
    )

    try:
        bails = [bailout(r.user, r.page, r.shortcode) for _, r in df.iterrows()]
    except AttributeError:
        print('Error: Your csv is not the right format. Please use the headers: user,page,shortcode')
        return

    for i, b in enumerate(bails):
        if i % 20 == 0 and i != 0:
            print(f"Bailed {i} users.")
        try:
            post_bail(b)
        except Exception as e:
            print(e)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, required=True)
    args = parser.parse_args()
    main(args.path)
