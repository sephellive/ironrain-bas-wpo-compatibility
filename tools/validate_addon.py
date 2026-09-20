#!/usr/bin/env python3
"""Small source-tree validator used by CI before packaging the addon."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
GAMEDATA = ROOT / "gamedata"
EXPECTED = {
    "configs/items/settings/mod_parts_zzzz_ir_bas_wpo_compat.ltx",
    "configs/items/weapons/mod_w_ks23_zzzz_ir_bas_wpo_compat.ltx",
    "scripts/zzzzzzzzzzzz_ir_bas_wpo_compat.script",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


actual = {
    path.relative_to(GAMEDATA).as_posix()
    for path in GAMEDATA.rglob("*")
    if path.is_file()
}
if actual != EXPECTED:
    fail(f"unexpected gamedata file set: {sorted(actual)}")

parts = (GAMEDATA / "configs/items/settings/mod_parts_zzzz_ir_bas_wpo_compat.ltx").read_text(
    encoding="utf-8-sig"
)
for token in (
    "![con_parts_list]",
    "wpn_fn57_bas",
    "prt_w_p_spring_4",
    "wpn_karabiner98k_silen98",
):
    if token not in parts:
        fail(f"missing parts patch token: {token}")

ks23 = (GAMEDATA / "configs/items/weapons/mod_w_ks23_zzzz_ir_bas_wpo_compat.ltx").read_text(
    encoding="utf-8-sig"
)
if "![wpn_ks23]" not in ks23 or "single_handed = 0" not in ks23:
    fail("KS-23 classification patch is incomplete")

runtime = (GAMEDATA / "scripts/zzzzzzzzzzzz_ir_bas_wpo_compat.script").read_text(
    encoding="utf-8-sig"
)
for token in (
    "calculate_weapon_shot_heat_impact",
    "execute_advanced_thermodynamics_core",
    "calculate_realistic_gas_rpm",
    "calculate_realistic_spring_rpm",
    "yan_stalker_sakharov",
    "m_data.tm_custom = nil",
):
    if token not in runtime:
        fail(f"missing runtime compatibility hook: {token}")

for forbidden in ("trader_autoinject.script", "zz_GunTemp.script"):
    if (GAMEDATA / "scripts" / forbidden).exists():
        fail(f"full upstream override must not be shipped: {forbidden}")

print("Addon source validation passed.")
