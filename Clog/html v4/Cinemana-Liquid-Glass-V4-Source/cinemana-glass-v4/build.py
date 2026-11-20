from pathlib import Path
import base64,re
p=Path(__file__).parent
s=(p/'index.html').read_text().replace('<link rel="stylesheet" href="style.css">','<style>'+ (p/'style.css').read_text()+'</style>').replace('<script src="app.js"></script>','<script>'+ (p/'app.js').read_text()+'</script>')
s=s.replace('<script src="optics.js"></script>','<script>'+ (p/'optics.js').read_text()+'</script>')
assets={x.stem:'data:image/jpeg;base64,'+base64.b64encode(x.read_bytes()).decode() for x in (p/'assets').glob('*.jpg')}
import json
s=s.replace('const img=id=>`assets/${id}.jpg`;','const EMBEDDED='+json.dumps(assets)+';const img=id=>EMBEDDED[id]||"";')
(p.parent/'Cinemana-Liquid-Glass-V4.html').write_text(s)
