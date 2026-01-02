#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI demo for MSR-V Public Demo Engine."""

import argparse
import json
from engine import MSRVPublicEngine


def main():
    ap = argparse.ArgumentParser(description="MSR-V Public Demo CLI")
    ap.add_argument("--lang", default="EN", choices=["EN", "KO"], help="Language (EN or KO)")
    ap.add_argument("--text", default=None, help="Input text to inspect")
    ap.add_argument("--interactive", action="store_true", help="Interactive loop mode")
    args = ap.parse_args()

    eng = MSRVPublicEngine()

    if args.interactive or not args.text:
        print("=" * 60)
        print("MSR-V Public Demo (type 'exit' to quit)")
        print("=" * 60)
        while True:
            try:
                t = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nBye!")
                break
            if t.lower() in ("exit", "quit", "q"):
                break
            out = eng.inspect(t, lang=args.lang)
            print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        out = eng.inspect(args.text, lang=args.lang)
        print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
