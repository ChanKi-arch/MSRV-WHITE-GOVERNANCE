#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI demo for MSR-V Public Demo Engine."""

import argparse, json
from engine import MSRVPublicEngine

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="EN", choices=["EN","KO"])
    ap.add_argument("--text", default=None, help="Input text to inspect")
    ap.add_argument("--interactive", action="store_true", help="Interactive loop")
    args = ap.parse_args()

    eng = MSRVPublicEngine()

    if args.interactive or not args.text:
        print("MSR-V Public Demo (type 'exit' to quit)")
        while True:
            t = input("> ").strip()
            if t.lower() in ("exit","quit","q"):
                break
            out = eng.inspect(t, lang=args.lang)
            print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        out = eng.inspect(args.text, lang=args.lang)
        print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
