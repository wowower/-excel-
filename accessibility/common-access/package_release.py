"""Build a reproducible manifest and a clean delivery archive outside the app."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parent

def main():
    excluded_dirs={'.qa','__pycache__','.git'}
    files=sorted(p for p in ROOT.rglob('*') if p.is_file()
                 and not any(part in excluded_dirs for part in p.relative_to(ROOT).parts)
                 and p.suffix not in {'.log','.zip','.pyc'}
                 and p.name not in {'MANIFEST.json','SPEC.md'})
    manifest={'version':'0.1.0','files':[{'path':p.relative_to(ROOT).as_posix(),
              'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
              for p in files]}
    manifest_path=ROOT/'MANIFEST.json'
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    files.append(manifest_path)
    destination=ROOT.parent/'CommonAccess-完整交付.zip'
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as archive:
        for p in files:
            archive.write(p,'common-access/'+p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(destination) as archive:
        assert len(archive.namelist())==len(files)
        assert archive.testzip() is None
        for item in manifest['files']:
            data=archive.read('common-access/'+item['path'])
            assert hashlib.sha256(data).hexdigest()==item['sha256']
    print(json.dumps({'archive':str(destination),'files':len(files),'bytes':destination.stat().st_size},ensure_ascii=True))

if __name__=='__main__':main()
