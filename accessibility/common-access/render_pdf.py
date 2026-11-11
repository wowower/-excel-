"""Render PDF pages with a verified PDFium binary kept in .qa/pdfium.

This helper is for document QA only, not needed to run the application.
PDFium: https://github.com/bblanchon/pdfium-binaries ; retain its license.
"""
import argparse
import ctypes as c
import json
from pathlib import Path
from PIL import Image

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('pdf')
    parser.add_argument('--out', required=True)
    parser.add_argument('--scale',type=float,default=1.6)
    args=parser.parse_args()
    lib=c.CDLL(str(Path(__file__).resolve().parent/'.qa/pdfium/pdfium.dll'))
    def bind(name,restype,argtypes):
        f=getattr(lib,name);f.restype=restype;f.argtypes=argtypes;return f
    bind('FPDF_InitLibrary',None,[])()
    load=bind('FPDF_LoadDocument',c.c_void_p,[c.c_char_p,c.c_char_p])
    close=bind('FPDF_CloseDocument',None,[c.c_void_p])
    count=bind('FPDF_GetPageCount',c.c_int,[c.c_void_p])
    loadpage=bind('FPDF_LoadPage',c.c_void_p,[c.c_void_p,c.c_int])
    closepage=bind('FPDF_ClosePage',None,[c.c_void_p])
    width=bind('FPDF_GetPageWidthF',c.c_float,[c.c_void_p])
    height=bind('FPDF_GetPageHeightF',c.c_float,[c.c_void_p])
    create=bind('FPDFBitmap_Create',c.c_void_p,[c.c_int,c.c_int,c.c_int])
    fill=bind('FPDFBitmap_FillRect',None,[c.c_void_p,c.c_int,c.c_int,c.c_int,c.c_int,c.c_uint32])
    render=bind('FPDF_RenderPageBitmap',None,[c.c_void_p,c.c_void_p,c.c_int,c.c_int,c.c_int,c.c_int,c.c_int,c.c_int])
    buffer=bind('FPDFBitmap_GetBuffer',c.c_void_p,[c.c_void_p])
    stride=bind('FPDFBitmap_GetStride',c.c_int,[c.c_void_p])
    destroy=bind('FPDFBitmap_Destroy',None,[c.c_void_p])
    textload=bind('FPDFText_LoadPage',c.c_void_p,[c.c_void_p])
    textcount=bind('FPDFText_CountChars',c.c_int,[c.c_void_p])
    textget=bind('FPDFText_GetText',c.c_int,[c.c_void_p,c.c_int,c.c_int,c.POINTER(c.c_ushort)])
    textclose=bind('FPDFText_ClosePage',None,[c.c_void_p])
    doc=load(str(Path(args.pdf).resolve()).encode('utf-8'),None)
    if not doc: raise RuntimeError('PDFium failed to load PDF')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True);pages=[]
    try:
        for i in range(count(doc)):
            page=loadpage(doc,i)
            w,h=round(width(page)*args.scale),round(height(page)*args.scale)
            bitmap=create(w,h,0);fill(bitmap,0,0,w,h,0xffffffff)
            render(bitmap,page,0,0,w,h,0,1)
            raw=c.string_at(buffer(bitmap),stride(bitmap)*h)
            image=Image.frombytes('RGB',(w,h),raw,'raw','BGRX',stride(bitmap))
            image.save(out/f'page-{i+1:02}.png')
            t=textload(page);n=textcount(t);buf=(c.c_ushort*(n+1))();textget(t,0,n,buf)
            value=bytes(buf).decode('utf-16-le').rstrip('\x00')
            (out/f'page-{i+1:02}.txt').write_text(value,encoding='utf-8')
            pages.append({'page':i+1,'width':w,'height':h,'characters':n})
            textclose(t);destroy(bitmap);closepage(page)
    finally: close(doc)
    (out/'manifest.json').write_text(json.dumps(pages,indent=2),encoding='utf-8')
    print(json.dumps({'file':str(Path(args.pdf).name),'pages':len(pages),'characters':sum(x['characters'] for x in pages)}))

if __name__=='__main__': main()
