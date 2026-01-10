#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""msrv_public_engine.py

Public-demo engine for MSR-V White Engine.

This is **NOT** the proprietary MSR-V core.
It provides a stable, deterministic interface and can replay
precomputed benchmark traces (route/state/Zs/theta) shipped in this repo.

Why:
- protects IP
- still demonstrates governance outputs + traceability
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import json
import os
import difflib


@dataclass
class MSRVResult:
    text: str
    lang: str
    route: str
    state4: str
    zs: Optional[float] = None
    theta: Optional[float] = None
    shape: Optional[str] = None
    need: Optional[float] = None
    notes: Optional[str] = None


class MSRVPublicEngine:
    def __init__(self, samples_path: str = None):
        if samples_path is None:
            samples_path = os.path.join(os.path.dirname(__file__), "public_samples")
        self.samples_path = samples_path
        self.samples: List[Dict[str, Any]] = []

        if os.path.exists(samples_path):
            with open(samples_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
            self.samples = self._normalize_samples(raw)

    def _normalize_samples(self, raw: Any) -> List[Dict[str, Any]]:
        """
        Normalize loaded samples into a flat list[dict].
        """
        flat: List[Dict[str, Any]] = []

        def walk(x: Any) -> None:
            if isinstance(x, dict):
                flat.append(x)
                return
            if isinstance(x, list):
                for y in x:
                    walk(y)
                return

        walk(raw)

        cleaned: List[Dict[str, Any]] = []
        for s in flat:
            if "text" not in s:
                continue
            if "lang" not in s:
                s["lang"] = "EN"
            cleaned.append(s)

        return cleaned

    def inspect(self, text: str, lang: str = "EN") -> Dict[str, Any]:
        """Return a deterministic 'governance trace' for the given text.

        Strategy:
        1) exact match in shipped samples
        2) fuzzy nearest neighbor among shipped samples
        3) fallback heuristic that is intentionally conservative
        """
        text_norm = (text or "").strip()
        if not text_norm:
            return self._pack(
                text, lang,
                route="BYPASS", state4="Harmony", zs=0.95,
                theta=0.0, shape="POINT", need=0.0,
                notes="Empty input -> BYPASS"
            )

        # exact match
        for s in self.samples:
            if s.get("lang", "").upper() == lang.upper() and (s.get("text", "").strip() == text_norm):
                return self._from_sample(s, match="exact")

        # fuzzy match (same language first)
        candidates = [s for s in self.samples if s.get("lang", "").upper() == lang.upper()]
        if not candidates:
            candidates = self.samples

        best: Optional[Dict[str, Any]] = None
        best_score = 0.0
        for s in candidates:
            t = (s.get("text", "") or "").strip()
            if not t:
                continue
            score = difflib.SequenceMatcher(a=text_norm, b=t).ratio()
            if score > best_score:
                best_score = score
                best = s

        if best is not None and best_score >= 0.72:
            out = self._from_sample(best, match=f"fuzzy:{best_score:.2f}")
            out["meta"]["nearest_text"] = best.get("text", "")
            return out

        # conservative fallback
        lower = text_norm.lower()
        has_numbers = any(ch.isdigit() for ch in text_norm)
        risky_claim = any(k in lower for k in ["100%", "guarantee", "cure", "always", "never", "perfect"])
        negation = any(k in lower for k in ["not", "never", "no "]) or any(k in text_norm for k in ["아니다", "않", "못", "없"])

        need = 0.55 + (0.15 if has_numbers else 0.0) + (0.15 if risky_claim else 0.0) + (0.10 if negation else 0.0)
        need = min(1.0, need)
        route = "FULL" if need >= 0.70 else "LITE"
        state4 = "Divergence" if negation else "Alignment" if risky_claim else "Harmony"
        zs = 0.55 if route == "FULL" else 0.72
        theta = 0.35 if risky_claim else 0.18
        shape = "TRIANGLE" if (has_numbers or risky_claim) else "LINE"

        return self._pack(
            text=text_norm, lang=lang, route=route, state4=state4, zs=zs, theta=theta, shape=shape, need=need,
            notes="Public fallback heuristic (conservative). For real evaluation, run the proprietary engine privately."
        )

    def _from_sample(self, s: Dict[str, Any], match: str) -> Dict[str, Any]:
        return self._pack(
            text=s.get("text", ""),
            lang=s.get("lang", "EN"),
            route=s.get("route") or "LITE",
            state4=s.get("state4") or "Harmony",
            zs=s.get("zs"),
            theta=s.get("theta"),
            shape=s.get("shape"),
            need=s.get("need"),
            notes=(s.get("notes") or "") + (f" | match={match}" if match else "")
        )

    def _pack(
        self, text: str, lang: str, route: str, state4: str,
        zs: Optional[float], theta: Optional[float], shape: Optional[str],
        need: Optional[float], notes: str
    ) -> Dict[str, Any]:
        return {
            "input": {"text": text, "lang": lang},
            "output": {
                "route": route,
                "state4": state4,
                "Zs": zs,
                "theta": theta,
                "shape": shape,
                "need": need,
            },
            "meta": {
                "engine": "MSRV-Public-Demo",
                "proprietary_core": False,
                "notes": notes,
            }
        }
