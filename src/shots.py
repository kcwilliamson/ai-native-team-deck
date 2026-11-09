import asyncio,sys
F='/home/claude/fs/fonts/node_modules/@fontsource'
css=f"""
@font-face{{font-family:'Newsreader';font-weight:400;font-style:normal;src:url(file://{F}/newsreader/files/newsreader-latin-400-normal.woff2)}}
@font-face{{font-family:'Newsreader';font-weight:400;font-style:italic;src:url(file://{F}/newsreader/files/newsreader-latin-400-italic.woff2)}}
@font-face{{font-family:'Hanken Grotesk';font-weight:400;src:url(file://{F}/hanken-grotesk/files/hanken-grotesk-latin-400-normal.woff2)}}
@font-face{{font-family:'Hanken Grotesk';font-weight:600;src:url(file://{F}/hanken-grotesk/files/hanken-grotesk-latin-600-normal.woff2)}}
@font-face{{font-family:'DM Mono';font-weight:400;src:url(file://{F}/dm-mono/files/dm-mono-latin-400-normal.woff2)}}
"""
from playwright.async_api import async_playwright
async def main():
    ns=[int(x) for x in sys.argv[1:]] or list(range(1,47))
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1600,'height':900})
        await pg.add_init_script("try{sessionStorage.setItem('deckok','1')}catch(e){}")
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file:///mnt/user-data/outputs/ai-enabling-a-team.html',wait_until='domcontentloaded')
        await pg.add_style_tag(content=css)
        await pg.wait_for_timeout(800)
        for n in ns:
            await pg.evaluate(f'window.__deck.jump({n})')
            await pg.wait_for_timeout(3400 if n in (0,) else 3400)
            await pg.screenshot(path=f'/home/claude/work/deck/s{n:02d}.png')
        print(errs[:10])
        await b.close()
asyncio.run(main())
