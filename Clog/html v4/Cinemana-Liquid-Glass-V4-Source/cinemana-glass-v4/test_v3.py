from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
html=(p.parent/'Cinemana-Liquid-Glass-V4.html').read_text()
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);ctx=b.new_context(viewport={'width':412,'height':915},device_scale_factor=1,has_touch=True);page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 shim='<script>window.testStorage=window.testStorage||{};Object.defineProperty(window,"localStorage",{configurable:true,value:{getItem:k=>window.testStorage[k]??null,setItem:(k,v)=>window.testStorage[k]=String(v)}});</script>';page.set_content(html.replace('<head>','<head>'+shim));page.locator('[data-action=glass-lab]').click();page.wait_for_timeout(500)
 assert page.locator('#lens-status').inner_text() in ['CANVAS / REFRACTION','WEBGL / GLSL'];status=page.locator('#lens-status').inner_text();lens=page.locator('#optical-lens');r=lens.bounding_box();before=lens.evaluate('e=>e.toDataURL()');page.mouse.move(r['x']+r['width']*.8,r['y']+r['height']*.55);page.wait_for_timeout(150);after=lens.evaluate('e=>e.toDataURL()');assert before!=after,'lens pixels must react to pointer'
 page.locator('[data-glass-mode=eco]').click();assert page.locator('#lens-status').inner_text()=='CSS / ECO';page.locator('[data-glass-mode=prism]').click();assert page.locator('#lens-status').inner_text() in ['CANVAS / REFRACTION','WEBGL / GLSL'];page.locator('[data-lab-toggle=motion]').click();assert page.locator('body').evaluate("e=>e.classList.contains('motion-off')");page.locator('[data-action=close]').click();stored=page.evaluate('JSON.stringify(window.testStorage)');page.close();page=ctx.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.set_content(html.replace('<head>','<head><script>window.testStorage='+stored+'</script>'+shim));assert page.locator('body').get_attribute('data-glass-mode')=='prism';assert page.locator('body').evaluate("e=>e.classList.contains('motion-off')");page.locator('[data-hero="1"]').click();assert '02 / 03' in page.locator('.hero-pagination').inner_text();page.locator('.resume-card').click();assert page.locator('#modal').is_visible();page.locator('[data-action=close]').click()
 for width in [320,360,412,768]:
  page.set_viewport_size({'width':width,'height':850})
  for name in ['home','library','search','downloads','account']:
   page.locator(f'.dock [data-page={name}]').click();assert page.evaluate('document.body.scrollWidth<=innerWidth+1'),(width,name)
 assert not errors,errors;b.close();print('PASS V4: optical pixel response ('+status+'), ECO fallback, prism, motion disable, storage shim reload, hero counter, resume preview, 20 viewport/page combinations, no uncaught JS errors.')
