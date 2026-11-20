# Cinemana Pro / Obsidian 04 — Design System

## Style prompt
Arabic RTL, cinema-first, warm black obsidian, ivory text, coral highlights. Let the poster tell the story. Glass belongs primarily to a floating navigation and interaction layer, not the content itself. A premium, quiet, immersive feel; readable during long download operations.

## Tokens
- Canvas `#090A0D`; content surface `#17191E`; foreground `#F8F4EE`; muted `#B5B7C1`; coral `#FF786F`.
- Primary CTA on art: ivory `#F7F3EC` on charcoal `#141416`. Other controls use accent contrast-aware solid fills.
- Arabic font fallback: Tahoma / Arial / system. Monospace page counters. No online font dependency.
- Spacing: 4/8/12/16/20/24 px. Major touch targets 44 px or more; dock 72 px. Main content corners 13–26 px; floating dock 34 px; sheet 31 px.
- Dark, light, OLED; coral, ruby, ice; density comfortable/compact; glass Eco/Balanced/Prism; high contrast, reduced motion.

## Motion + material
- Page entrance ~380 ms; localized transform/opacity; dock selector ~440 ms spring-like easing; hero reveal 1 s finite. Manual and OS reduced-motion respected for entrance and pointer reflection.
- Eco/contrast/glass-off: opaque dock; Balanced: CSS backdrop blur; Prism: optional SVG displacement + blur on live backdrop if syntax is supported. Feature detection does not guarantee correct rendering; use Balanced if artifacts or stutter.
- Lab has WebGL attempt and Canvas 2D actual pixel sampling fallback. Texture lab is a generated sample; dock filter is a separate live browser effect. No native Apple-renderer equivalence implied.
- Queue pages cap rendered rows at 24; update visible progress via indexed lookup. Simulator is intentionally separate from page state but not a native background service.

## Do not
- Do not blur every poster or layer glass on glass; avoid neon outlines on all cards.
- Do not show unsupported download/playback claims; all queue and player data simulated.
- Do not claim phone FPS or performance without measurement. No writes to CP, no APK without owner approval.
