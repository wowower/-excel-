"""Render the project's limited Markdown source to accessible printable HTML.

Only Python's standard library is needed. HTML is escaped before inline links
and emphasis are rendered; source text is not treated as active markup.
"""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent

STYLE = '''
*{box-sizing:border-box}body{margin:0;background:#e8ecee;color:#171717;font-family:"Microsoft YaHei","Noto Sans CJK SC","SimSun",sans-serif;font-size:11pt;line-height:1.7}
.docbar{padding:16px 24px;background:white;position:sticky;top:0;z-index:2;font-size:14px}.docbar a{margin-right:20px;color:#194b59}.docbar button{padding:10px 18px;background:#194b59;color:white;border:0;border-radius:5px;cursor:pointer}
.sheet{position:relative;background:white;width:210mm;height:297mm;padding:18mm 20mm 16mm;margin:22px auto;box-shadow:0 3px 18px #0002;overflow:visible}.running{font-size:8pt;line-height:1.5;color:#555;margin-bottom:7mm;min-height:5mm}.content{padding-bottom:7mm}h1,h2,h3{color:#000;line-height:1.5;break-after:avoid}h1{font-size:25pt;font-weight:700;margin:7mm 0 10mm}h2{font-size:15pt;margin:0 0 5mm}h3{font-size:11.5pt;margin:5mm 0 2mm}p{margin:0 0 4mm;text-align:left;overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;table-layout:fixed;margin:5mm 0 6mm;font-size:9pt;line-height:1.6}th,td{border:1px solid #d9d9d9;padding:2.3mm 2.5mm;vertical-align:middle;overflow-wrap:anywhere}th{background:#36434c;color:#fff;font-weight:600}tbody tr:nth-child(even){background:#f3f5f6}tr{break-inside:avoid}thead{display:table-header-group}a{color:#173b45;text-decoration:underline;text-underline-offset:2px}ul,ol{padding-left:1.3em;margin:0 0 4mm}li{margin:2mm 0}code{font-family:Consolas,monospace;font-size:.9em;overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:9pt;background:#f5f5f5;padding:3mm}.page-footer{position:absolute;bottom:8mm;left:20mm;right:20mm;display:flex;justify-content:space-between;font-size:8pt;color:#555}.cover h1{margin-top:15mm;font-size:25pt}.cover .running{margin-bottom:13mm}.continuous{height:auto;min-height:297mm}.continuous .content{padding-bottom:14mm}
@page{size:A4;margin:0}@media print{body{background:white}.docbar{display:none}.sheet{margin:0;box-shadow:none;break-after:page;page-break-after:always}.sheet:last-child{break-after:auto;page-break-after:auto}a{color:inherit}th{-webkit-print-color-adjust:exact;print-color-adjust:exact}tbody tr:nth-child(even){-webkit-print-color-adjust:exact;print-color-adjust:exact}.continuous{height:auto}.continuous .page-footer{display:none}}
@media screen and (max-width:850px){.sheet{width:100%;height:auto;min-height:0;padding:25px;margin:15px 0}.page-footer{position:static;margin-top:30px}.docbar{position:static}table{font-size:10pt}h1{font-size:24pt}}
'''

def inline(s):
    value = html.escape(s, quote=True)
    value = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+|\.?\.?/[^\s)]+|[^\s():]+\.(?:json|md|html|pdf))\)', lambda m: '<a href="'+m[2]+'">'+m[1]+'</a>', value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)

def markdown(src):
    out=[]; rows=src.splitlines(); i=0
    while i<len(rows):
        line=rows[i].strip()
        if not line:
            i+=1; continue
        if line.startswith('```'):
            content=[]; i+=1
            while i<len(rows) and not rows[i].strip().startswith('```'):
                content.append(rows[i]); i+=1
            out.append('<pre><code>'+html.escape('\n'.join(content))+'</code></pre>'); i+=1; continue
        if line.startswith('|'):
            table=[]
            while i<len(rows) and rows[i].strip().startswith('|'):
                cells=[x.strip() for x in rows[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells): table.append(cells)
                i+=1
            if table:
                count=len(table[0]);first=table[0][0]
                widths={2:[28,72],3:[25,40,35],4:[21,13,36,30],5:[16,25,15,28,16],6:[16,12,18,18,18,18]}.get(count,[100/count]*count)
                if first=='编号': widths=[10,45,45]
                if first=='科目': widths=[27,53,20]
                if first=='模块': widths=[19,45,36]
                if first=='角色': widths=[19,49,32]
                cols='<colgroup>'+''.join(f'<col style="width:{w}%">' for w in widths)+'</colgroup>'
                out.append('<table>'+cols+'<thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in table[0])+'</tr></thead><tbody>')
                for row in table[1:]:
                    cells=[]
                    for j,c in enumerate(row):
                        numeric=('元' in table[0][j] or '点位数' in table[0][j]) and bool(re.fullmatch(r'[-\d,]+',c))
                        alignment=' style="text-align:right"' if numeric else ''
                        cells.append('<td'+alignment+'>'+inline(c)+'</td>')
                    out.append('<tr>'+''.join(cells)+'</tr>')
                out.append('</tbody></table>')
            continue
        heading=re.match(r'^(#{1,3})\s+(.*)',line)
        if heading:
            n=len(heading[1]); out.append(f'<h{n}>'+inline(heading[2])+f'</h{n}>');i+=1;continue
        if line.startswith('- '):
            out.append('<ul>')
            while i<len(rows) and rows[i].strip().startswith('- '):
                out.append('<li>'+inline(rows[i].strip()[2:])+'</li>');i+=1
            out.append('</ul>');continue
        parts=[line];i+=1
        while i<len(rows) and rows[i].strip() and not rows[i].lstrip().startswith(('#','|','- ','```')):
            parts.append(rows[i].strip());i+=1
        out.append('<p>'+inline(' '.join(parts))+'</p>')
    return '\n'.join(out)

def build(name):
    src=(ROOT/'docs'/f'{name}.md').read_text(encoding='utf-8')
    title=src.splitlines()[0].lstrip('# ').strip()
    pages=src.split('<!-- page -->')
    sections=[]
    for n,page in enumerate(pages,1):
        cls='sheet'+(' cover' if n==1 else '')+(' continuous' if name=='guide' else '')
        sections.append(f'<section class="{cls}" aria-label="第 {n} 页"><div class="running">共达 Common Access　/　{html.escape(title)}</div><div class="content">{markdown(page)}</div><div class="page-footer"><span>2026年11月　共达项目资料</span><span>{n} / {len(pages)}</span></div></section>')
    result='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+STYLE+'</style></head><body><nav class="docbar" aria-label="文档操作"><a href="../index.html#help">返回工具箱</a><a href="'+name+'.md">查看可编辑原文</a><button onclick="window.print()">打印或另存为 PDF</button></nav><main>'+''.join(sections)+'</main></body></html>'
    (ROOT/'docs'/f'{name}.html').write_text(result,encoding='utf-8')
    return {'name':name,'planned_pages':len(pages)}

if __name__=='__main__':
    import json
    print(json.dumps([build(n) for n in ['research','application','prospects','guide']],ensure_ascii=False))
