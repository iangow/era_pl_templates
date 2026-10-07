"""Project defaults for using great_tables output with Typst.

Import this module before creating Polars ``.style`` / ``great_tables.GT``
objects. It replaces Great Tables' browser-oriented default font stack with
the book's body font, avoiding Typst font warnings and matching the PDF text.
"""

from __future__ import annotations

import dataclasses

import great_tables as gt
import great_tables._gt_data as _gt_data


DEFAULT_TABLE_FONT = "Libertinus Serif"
DEFAULT_TABLE_FONT_SIZE = "10pt"
DEFAULT_HEADER_RULE_COLOR = "#000000"
DEFAULT_HEADER_RULE_WIDTH = "1px"
DEFAULT_BODY_RULE_STYLE = "none"
DEFAULT_DATA_ROW_PADDING = "3px"
DEFAULT_COLUMN_LABEL_PADDING = "3px"


def configure_gt_typst(
    font: str = DEFAULT_TABLE_FONT,
    font_size: str = DEFAULT_TABLE_FONT_SIZE,
    header_rule_color: str = DEFAULT_HEADER_RULE_COLOR,
    header_rule_width: str = DEFAULT_HEADER_RULE_WIDTH,
    body_rule_style: str = DEFAULT_BODY_RULE_STYLE,
    data_row_padding: str = DEFAULT_DATA_ROW_PADDING,
    column_label_padding: str = DEFAULT_COLUMN_LABEL_PADDING,
) -> None:
    """Set Typst-friendly defaults for new ``great_tables.GT`` objects."""
    current_init = gt.GT.__init__
    original_init = getattr(gt.GT, "_era_original_init", current_init)

    def _gt_init_patched(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        table_font = _gt_data.OptionsInfo(
            False, "table", "values", [font]
        )
        table_font_size = _gt_data.OptionsInfo(
            True, "table", "px", font_size
        )
        header_rule_color_opt = _gt_data.OptionsInfo(
            True, "column_labels", "value", header_rule_color
        )
        header_rule_width_opt = _gt_data.OptionsInfo(
            True, "column_labels", "px", header_rule_width
        )
        body_rule_style_opt = _gt_data.OptionsInfo(
            True, "table_body", "value", body_rule_style
        )
        data_row_padding_opt = _gt_data.OptionsInfo(
            True, "data_row", "px", data_row_padding
        )
        column_label_padding_opt = _gt_data.OptionsInfo(
            True, "column_labels", "px", column_label_padding
        )
        options = dataclasses.replace(
            self._options,
            table_font_names=table_font,
            table_font_size=table_font_size,
            table_border_top_color=header_rule_color_opt,
            table_border_top_width=header_rule_width_opt,
            table_border_bottom_color=header_rule_color_opt,
            table_border_bottom_width=header_rule_width_opt,
            column_labels_border_bottom_color=header_rule_color_opt,
            column_labels_border_bottom_width=header_rule_width_opt,
            table_body_border_top_color=header_rule_color_opt,
            table_body_border_top_width=header_rule_width_opt,
            table_body_hlines_style=body_rule_style_opt,
            data_row_padding=data_row_padding_opt,
            data_row_padding_horizontal=data_row_padding_opt,
            column_labels_padding=column_label_padding_opt,
            column_labels_padding_horizontal=column_label_padding_opt,
        )
        object.__setattr__(self, "_options", options)

    gt.GT._era_original_init = original_init
    gt.GT.__init__ = _gt_init_patched


configure_gt_typst()
