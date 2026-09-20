# Changelog

## 1.1.0 — 2026-09-21

- Replaced the centered per-character weapon diagnostic typewriter with stable one-shot phase messages.
- Removed the 100 Hz diagnostic hold refresh loop from the active display path.
- Added proper cancellation of the compatibility diagnostic timer on weapon actions and inventory changes.
- Kept the original two diagnostic phases, timing, severity colors and inspection animation.

## 1.0.0 — 2026-09-21

- Added a complete WPO parts set for BaS FN Five-seveN.
- Added WPO parts mapping for the suppressed Karabiner 98k section.
- Corrected KS-23 classification for WPOO long-gun mechanics.
- Added runtime support for WPOO suppressor heat, carbon and RPM multipliers on integral suppressors.
- Restored BaS `tm_custom` cleanup and Sakharov trader handling alongside WPO `trader_autoinject`.
- Documented Gauss Rifle as an intentional upstream-compatible WPO exemption.
- Added CI source-tree validation and release packaging inherited from the addon template.
