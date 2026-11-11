"""Print the three formal HTML documents using installed headless Edge."""
from pathlib import Path
import subprocess
import json

ROOT=Path(__file__).resolve().parent
EDGE=Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')

def main():
    out=ROOT/'docs/pdf';out.mkdir(exist_ok=True)
    for name in ['research','application','prospects']:
        profile=ROOT/'.qa'/('edge-'+name)
        cmd=[str(EDGE),'--headless','--disable-gpu','--no-first-run','--disable-extensions',
             '--no-pdf-header-footer','--disable-background-networking',
             '--user-data-dir='+str(profile),'--print-to-pdf='+str(out/(name+'.pdf')),
             (ROOT/'docs'/(name+'.html')).as_uri()]
        result=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60,
                              creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        (ROOT/'.qa'/(name+'-print.log')).write_bytes(result.stderr)
        target=out/(name+'.pdf')
        if result.returncode or not target.exists() or target.stat().st_size<5000:
            raise RuntimeError('Printing failed for '+name+'; see .qa log')
        print(json.dumps({'document':name,'bytes':target.stat().st_size}),flush=True)

if __name__=='__main__':main()
