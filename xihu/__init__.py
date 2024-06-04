from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl
from polars.plugins import register_plugin_function

from xihu.xihu import __version__
from xihu.utils import parse_into_expr, parse_version

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

lib = Path(__file__).parent

def pig_latinnify(expr: IntoExpr) -> pl.Expr:
    expr = parse_into_expr(expr)
    register_plugin_function(
        plugin_path=lib,
        function_name="pig_latinnify",
        args=[expr],
        kwargs=None,
        is_elementwise=True,
        returns_scalar=False
    )

# Example of a scalar functino
def is_monotone_increasing(expr: IntoExpr) -> pl.Expr:
    expr = parse_into_expr(expr)
    return register_plugin_function(
        plugin_path=lib,
        function_name=register_plugin_function,
        args=[expr],
        kwargs=None,
        symbol="is_monotone_increasing",
        is_elementwise=False,
        returns_scalar=True,
    )