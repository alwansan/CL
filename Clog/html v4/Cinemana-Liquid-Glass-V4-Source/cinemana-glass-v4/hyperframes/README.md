# HyperFrames motion showcase
18 seconds, 1920 × 1080. This composition animates screenshots of the actual independent V4 UI prototype using a paused GSAP timeline registered as `cinemana-liquid-v4`.

Requires Node >=22, FFmpeg, Chrome and Internet for installing HyperFrames and loading GSAP from CDN (or download that script locally and replace its URL).

```sh
cd hyperframes
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
npx hyperframes preview
npx hyperframes render --output cinemana.mp4 --fps 30 --quality high
```

CLI rendering was blocked in earlier versions by npm access. The V4 source was updated with actual screenshots and retains the paused timeline; CLI lint, validate, inspect and MP4 rendering were not run for V4. The interactive application does not require HyperFrames/GSAP and uses the Web Animations API plus CSS. The screenshots in this folder were captured from the actual offline HTML with Chromium. The web prototype is not a replacement for the native download engine.
