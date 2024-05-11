from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl

from xihu.xihu import __version__
from xihu.utils import parse_into_expr, register_plugin, parse_version

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

lib = Path(__file__).parent

def pig_latinnify(expr: IntoExpr) -> pl.Expr:
    expr = parse_into_expr(expr)
    return register_plugin(
        args=[expr],
        symbol="pig_latinnify",
        is_elementwise=True,
        lib=lib,
    )