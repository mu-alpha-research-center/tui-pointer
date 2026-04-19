"""
Rich-based terminal animator for two-pointer steps.
"""

import time
from typing import Any

from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.panel import Panel
from rich import box

# Palette — cycles if there are more than len(COLORS) pointers
COLORS = ["bold cyan", "bold red", "bold green", "bold magenta", "bold yellow"]


def _pointer_color(name: str, names: list[str]) -> str:
    return COLORS[names.index(name) % len(COLORS)]


def _render(step, step_num: int, total: int) -> Panel:
    arr = step.arr
    pointers = step.pointers          # {name: index}
    pointer_names = list(pointers.keys())

    # Each slot must fit: the value, the pointer name, and the [ ] brackets.
    # slot_width = inner width; total slot on screen = slot_width + 2 (for "[ ]").
    val_width = max((len(str(v)) for v in arr), default=1)
    name_width = max((len(n) for n in pointer_names), default=0)
    slot_width = max(val_width, name_width - 2)  # -2 because brackets add 2
    slot_width = max(slot_width, 1)
    slot = slot_width + 2  # total chars per cell including brackets

    # ── label row: pointer names above their cell ────────────────────────────
    label_texts = []
    for name in pointer_names:
        color = _pointer_color(name, pointer_names)
        t = Text()
        for i in range(len(arr)):
            cell = name.center(slot) if pointers[name] == i else " " * slot
            t.append(cell, style=color)
        label_texts.append(t)

    # ── array row ────────────────────────────────────────────────────────────
    array_text = Text()
    for i, val in enumerate(arr):
        cell = str(val).center(slot_width)
        active = [n for n in pointer_names if pointers[n] == i]
        if active:
            color = _pointer_color(active[0], pointer_names)
            array_text.append(f"[{cell}]", style=f"{color} reverse")
        else:
            array_text.append(f"[{cell}]")

    # ── arrow row: ↑ under the active cell ───────────────────────────────────
    arrow_texts = []
    for name in pointer_names:
        color = _pointer_color(name, pointer_names)
        t = Text()
        for i in range(len(arr)):
            if pointers[name] == i:
                t.append("↑".center(slot), style=color)
            else:
                t.append(" " * slot)
        arrow_texts.append(t)

    lines: list[Any] = [*label_texts, array_text, *arrow_texts]

    if step.message:
        lines.append(Text(""))
        lines.append(Text(step.message, style="italic dim"))

    body = Text("\n").join(lines)
    return Panel(body, title=f"Step {step_num} / {total}", box=box.ROUNDED, padding=(1, 2))


def animate(steps, delay: float = 0.5) -> None:
    if not steps:
        return

    console = Console()
    total = len(steps)

    with Live(console=console, refresh_per_second=20, screen=False) as live:
        for i, step in enumerate(steps, 1):
            live.update(_render(step, i, total))
            time.sleep(delay)
