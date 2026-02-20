#!/usr/bin/env python3
import csv
import json
import re
from pathlib import Path
from typing import Iterable, Set
from datetime import datetime

HOMEPAGE = "https://github.com/GloomyD/blocklists"

UBL_META = {
    "ingerences": {
        "name": "Foreign interference (Viginum)",
        "description": "Domains linked to foreign interference operations (source: Viginum + manual additions).",
    },
    "complotistes": {
        "name": "Conspiracy content",
        "description": "Domains repeatedly sharing conspiracy/fake news content (manually curated).",
    },
    "ia-seo": {
        "name": "AI Slop / SEO spam",
        "description": "Domains producing low-quality AI-generated or SEO-spam content (manually curated).",
    },
}

DOMAIN_RE = re.compile(
    r"^(?:\*\.)?([a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?)+)$",
    re.IGNORECASE,
)

def normalize_domain(s: str) -> str | None:
    s = (s or "").strip()
    if not s or s.startswith("#"):
        return None

    # allow pasted uBlock style or URLs; extract domain-ish part
    s = s.replace("||", "").split("^", 1)[0].split("$", 1)[0].strip()
    s = s.replace("http://", "").replace("https://", "")
    s = s.split("/", 1)[0]
    s = s.split(":", 1)[0]
    s = s.lstrip(".").lower()
    if s.startswith("www."):
        s = s[4:]
    if s.startswith("*."):
        s = s[2:]

    # VIGINUM / IOC notations
    s = s.replace("[.]", ".").replace("(.)", ".")
    s = s.replace("[dot]", ".").replace("(dot)", ".")
    s = s.replace("[", "").replace("]", "")

    m = DOMAIN_RE.match(s)
    if not m:
        return None
    return m.group(1).lower()

def read_source_txt(path: Path) -> Set[str]:
    out: Set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        d = normalize_domain(line)
        if d:
            out.add(d)
    return out

def read_csv_domains(path: Path) -> Set[str]:
    """
    Tries to extract domains from CSV. Works for:
    - one-domain-per-line CSV
    - column named 'domain'/'domaine'/'ndd'
    - otherwise first column
    """
    out: Set[str] = set()
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        reader = csv.reader(f, dialect)
        rows = list(reader)

    if not rows:
        return out

    header = [c.strip().lower() for c in rows[0]]
    data_rows = rows[1:] if any(h for h in header) else rows

    idx = None
    for key in ("domain", "domaine", "ndd", "fqdn", "host"):
        if key in header:
            idx = header.index(key)
            break

    for r in data_rows:
        if not r:
            continue
        cell = r[idx] if idx is not None and idx < len(r) else r[0]
        d = normalize_domain(cell)
        if d:
            out.add(d)
    return out

def read_stix_json_domains(path: Path) -> Set[str]:
    """
    Extract domains from STIX-like JSON:
    looks for objects where type == 'domain-name' and uses 'value' field.
    Also tries to find any keys named 'value' that look like domains.
    """
    out: Set[str] = set()
    try:
        obj = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return out

    # STIX bundles often have {"objects":[...]}
    candidates: Iterable = []
    if isinstance(obj, dict) and "objects" in obj and isinstance(obj["objects"], list):
        candidates = obj["objects"]
    elif isinstance(obj, list):
        candidates = obj
    elif isinstance(obj, dict):
        candidates = [obj]

    def walk(o):
        if isinstance(o, dict):
            # STIX domain-name
            if o.get("type") == "domain-name" and isinstance(o.get("value"), str):
                d = normalize_domain(o["value"])
                if d:
                    out.add(d)
            # generic: any string values that look like domains
            for k, v in o.items():
                if isinstance(v, str) and k.lower() in ("value", "domain", "domaine", "host", "fqdn"):
                    d = normalize_domain(v)
                    if d:
                        out.add(d)
                else:
                    walk(v)
        elif isinstance(o, list):
            for it in o:
                walk(it)

    for c in candidates:
        walk(c)

    return out

def write_nextdns(domains: Set[str], outpath: Path):
    outpath.write_text("\n".join(sorted(domains)) + "\n", encoding="utf-8")

def write_ublacklist(domains: Set[str], outpath: Path, *, name: str, description: str, homepage: str):
    generated_at = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    rules = [f"*://*.{d}/*" for d in sorted(domains)]

    # évite les YAML cassés si guillemets / antislash
    safe_name = name.replace("\\", "\\\\").replace('"', '\\"')
    safe_description = description.replace("\\", "\\\\").replace('"', '\\"')
    safe_homepage = homepage.replace("\\", "\\\\").replace('"', '\\"')

    with outpath.open("w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f'name: "{safe_name}"\n')
        f.write(f'description: "{safe_description}"\n')
        f.write(f'homepage: "{safe_homepage}"\n')
        f.write("license: CC-BY-4.0\n")
        f.write("version: 1\n")
        f.write(f"generated_at: {generated_at}\n")
        f.write(f"domains_count: {len(domains)}\n")
        f.write("---\n\n")
        f.write("\n".join(rules))
        f.write("\n")

def main():
    repo_root = Path(__file__).resolve().parents[1]
    sources = repo_root / "sources"
    dist = repo_root / "dist"
    dist.mkdir(exist_ok=True)

    # --- Build "ingerences" from VIGINUM + your extended adds
    ingerences: Set[str] = set()

    viginum_dir = sources / "viginum"
    if viginum_dir.exists():
        for p in viginum_dir.rglob("*"):
            if p.is_file() and p.suffix.lower() == ".csv":
                ingerences |= read_csv_domains(p)
            elif p.is_file() and p.suffix.lower() in (".json",):
                ingerences |= read_stix_json_domains(p)

    ext = sources / "ingerences_extended.source.txt"
    if ext.exists():
        ingerences |= read_source_txt(ext)

    # --- Other lists
    complotistes: Set[str] = set()
    p = sources / "complotistes.source.txt"
    if p.exists():
        complotistes |= read_source_txt(p)

    ia_seo: Set[str] = set()
    p = sources / "ia-seo.source.txt"
    if p.exists():
        ia_seo |= read_source_txt(p)

    # Outputs (NextDNS + uBlacklist)
    write_nextdns(ingerences, dist / "ingerences.nextdns.txt")
    write_ublacklist(
        ingerences,
        dist / "ingerences.ublacklist.txt",
        name=UBL_META["ingerences"]["name"],
        description=UBL_META["ingerences"]["description"],
        homepage=HOMEPAGE,
    )

    write_nextdns(complotistes, dist / "complotistes.nextdns.txt")
    write_ublacklist(
        complotistes,
        dist / "complotistes.ublacklist.txt",
        name=UBL_META["complotistes"]["name"],
        description=UBL_META["complotistes"]["description"],
        homepage=HOMEPAGE,
    )

    write_nextdns(ia_seo, dist / "ia-seo.nextdns.txt")
    write_ublacklist(
        ia_seo,
        dist / "ia-seo.ublacklist.txt",
        name=UBL_META["ia-seo"]["name"],
        description=UBL_META["ia-seo"]["description"],
        homepage=HOMEPAGE,
    )

    print("OK:")
    print(f"- ingerences:  {len(ingerences)}")
    print(f"- complotistes:{len(complotistes)}")
    print(f"- ia-seo:      {len(ia_seo)}")
    print(f"Generated in: {dist}")

if __name__ == "__main__":
    main()