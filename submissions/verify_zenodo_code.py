"""Verify this published software anonymously, without modifying its metadata.

Operational provenance helper, outside the immutable computational H. Python
standard library + read-only local Git are required. No vault/authentication,
source PDF, browser or scientific producer is used. Download requests are serial.
Pass explicit local archive/cache locations; public output omits local paths.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RECORD = 23784871
DOI = '10.5281/zenodo.23784871'
TITLE = 'Computational evidence for Equation consistency in electron-only reconnection manuscripts'
PROJECT = 'Equation consistency in electron-only reconnection'
H = '83583b1524778b8bb4e5c78482ae7f4f104856cc'
TREE = '7bf82539dd5224ec9328dc94848b2a62dc6b4029'
FILES = 55
FILENAME = 'electron-only-equation-audit-code-v1.0.0.zip'
ZIP_BYTES = 393818
ZIP_SHA = 'd0444c832c21b8a2e60ebd02e576c4ad2077388dfeb9e412590b7049d1e5aabc'
ZIP_MD5 = 'ed245136dea9d446645372c7471e3af9'
ORCID = '0009-0003-9000-9315'
SELF_BYTES = Path(__file__).read_bytes()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def clean_url(url):
    u = urllib.parse.urlsplit(url)
    require(u.scheme == 'https' and not u.username and not u.password and not u.query and not u.fragment,
            'Public proof requires ordinary HTTPS URLs without credentials or query strings.')
    require(u.hostname in {'zenodo.org', 'api.datacite.org', 'doi.org', 'codeload.github.com'},
            'Unexpected download/redirect origin.')
    return url


def fetch(url, cache, filename, limit, observations):
    clean_url(url)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Taylor-Kalin-Electron-Only-Software-Verification/1.0',
        'Accept': 'application/json, application/zip, text/html;q=0.8, */*;q=0.5'})
    with urllib.request.urlopen(req, timeout=60) as response:
        status = response.status
        final_url = clean_url(response.geturl())
        body = response.read(limit + 1)
    require(status == 200 and len(body) <= limit, 'Anonymous retrieval failed or exceeded the explicit byte cap.')
    stamp = now()
    (cache / filename).write_bytes(body)
    observations.append({'url': url, 'status': status, 'bytes': len(body),
                         'sha256': sha(body), 'final_url': final_url, 'checked_at_utc': stamp})
    return body


def git(repo, *args):
    result = subprocess.run(['git', '-C', str(repo), *args], check=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout


def git_blobs(repo):
    require(git(repo, 'rev-parse', H + '^{tree}').decode().strip() == TREE, 'Code commit/tree mismatch.')
    records = []
    for line in git(repo, 'ls-tree', '-r', '-z', H).split(b'\0'):
        if not line:
            continue
        header, path = line.split(b'\t', 1)
        mode, kind, object_id = header.decode('ascii').split()
        require(mode in {'100644', '100755'} and kind == 'blob', 'Unexpected non-regular computational member.')
        name = path.decode('utf-8')
        records.append((name, object_id))
    require(len(records) == FILES and len({p for p, _ in records}) == FILES, 'Expected exactly 55 immutable Git blobs.')
    return {name: git(repo, 'cat-file', 'blob', oid) for name, oid in records}


def zip_members(data, expected):
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        items = archive.infolist()
        names = [i.filename for i in items]
        require(len(names) == len(set(names)), 'Duplicate ZIP member.')
        for info in items:
            path = PurePosixPath(info.filename)
            require(not path.is_absolute() and '..' not in path.parts and not info.flag_bits & 1,
                    'Unsafe/encrypted ZIP member.')
        files = [i for i in items if not i.is_dir()]
        require(len(files) == FILES, 'Wrong regular ZIP member count.')
        if {i.filename for i in files} == set(expected):
            prefix = ''
        else:
            first = {i.filename.split('/', 1)[0] for i in files}
            require(len(first) == 1, 'Unexpected public archive wrapper.')
            prefix = first.pop() + '/'
            require({i.filename[len(prefix):] for i in files} == set(expected), 'ZIP members differ from exact Git tree.')
        result = {i.filename[len(prefix):]: archive.read(i) for i in files}
        return result, archive.comment.decode('ascii'), prefix


def plain(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', text))).strip()


def orcid(value):
    return str(value).removeprefix('https://orcid.org/').removeprefix('http://orcid.org/')


def verify_metadata(record):
    require(record.get('id') == RECORD and record.get('doi') == DOI, 'Wrong Zenodo record/DOI.')
    require(record.get('state') == 'done' and record.get('submitted') is True,
            'Zenodo does not report this record as published/submitted.')
    meta = record['metadata']
    require(meta.get('title') == TITLE and meta.get('version') == '1.0.0', 'Wrong software title/version.')
    require(meta.get('publication_date') == '2026-10-29', 'Wrong software publication date.')
    require(meta.get('resource_type', {}).get('type') == 'software', 'Resource is not Software.')
    creators = meta.get('creators', [])
    require(len(creators) == 1 and creators[0].get('name') == 'Kalin, Taylor'
            and orcid(creators[0].get('orcid')) == ORCID, 'Wrong creator/ORCID.')
    description_html = meta.get('description', '')
    description = plain(description_html)
    source_url = 'https://github.com/Teylersf/electron-only-equation-audit/tree/' + H
    require(H in description and source_url in html.unescape(description_html),
            'Published description lacks exact code H/repository.')
    require('MIT' in description and re.search(r'CC\s*BY\s*4\.0', description, re.I),
            'Description must retain the separate MIT-code/CC-BY-text licensing scope.')
    files = record.get('files', [])
    require(len(files) == 1, 'Expected one published software ZIP.')
    item = files[0]
    require(item.get('key') == FILENAME and item.get('size') == ZIP_BYTES
            and item.get('checksum') == 'md5:' + ZIP_MD5, 'Published file metadata mismatch.')
    return meta, description


def main():
    if sys.flags.optimize:
        raise RuntimeError('Use ordinary Python, not -O.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--cache-dir', type=Path, required=True)
    parser.add_argument('--repository', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path, default=ROOT / 'submissions/zenodo-code-v1.0.0.json')
    args = parser.parse_args()
    cache = args.cache_dir.resolve()
    require(not cache.is_relative_to(args.repository.resolve()), 'Keep downloaded primary evidence outside the public study.')
    require(not args.output.exists(), 'Preserve existing verification receipts; use a fresh explicit output for rechecks.')
    cache.mkdir(parents=True, exist_ok=True)
    observations = []
    local = args.archive.read_bytes()
    require(args.archive.name == FILENAME and len(local) == ZIP_BYTES and sha(local) == ZIP_SHA
            and hashlib.md5(local).hexdigest() == ZIP_MD5, 'Local frozen ZIP mismatch.')
    expected = git_blobs(args.repository)
    local_members, comment, _ = zip_members(local, expected)
    require(comment == H and local_members == expected, 'Local software archive differs from immutable Git blobs.')

    # A newly published record can briefly propagate. Retry only 404/503 twice,
    # retaining those bounded observations; never republish or alter metadata.
    record_url = f'https://zenodo.org/api/records/{RECORD}'
    for attempt in range(3):
        try:
            record_raw = fetch(record_url, cache, 'zenodo-record.json', 2_000_000, observations)
            break
        except urllib.error.HTTPError as error:
            observations.append({'url': record_url, 'status': error.code, 'checked_at_utc': now(),
                                 'scope': 'Initial public propagation observation; no response body or headers published.'})
            if error.code not in (404, 503) or attempt == 2:
                raise
            time.sleep(3)
    record = json.loads(record_raw)
    meta, description = verify_metadata(record)
    download_url = f'https://zenodo.org/api/records/{RECORD}/files/{FILENAME}/content'
    downloaded = fetch(download_url, cache, FILENAME, ZIP_BYTES + 1, observations)
    require(downloaded == local, 'Anonymous Zenodo ZIP is not byte-identical to the frozen local archive.')
    remote_members, remote_comment, _ = zip_members(downloaded, expected)
    require(remote_members == expected and remote_comment == H, 'Zenodo members differ from Git H.')

    public_url = f'https://codeload.github.com/Teylersf/electron-only-equation-audit/zip/{H}'
    public_zip = fetch(public_url, cache, 'github-commit.zip', 2_000_000, observations)
    public_members, public_comment, public_prefix = zip_members(public_zip, expected)
    require(public_members == expected and public_comment == H, 'Anonymous public Git archive differs from local immutable H.')

    manifest = json.loads(expected['data/computational-artifact-manifest.json'])
    rows = manifest['files']
    require(manifest.get('file_count_excluding_manifest') == FILES - 1 and len(rows) == FILES - 1,
            'Wrong self-excluded manifest count.')
    require({r['path'] for r in rows} == set(expected) - {'data/computational-artifact-manifest.json'},
            'Manifest does not cover every other Git/archive member exactly.')
    for row in rows:
        data = expected[row['path']]
        require(row['bytes'] == len(data) and row['sha256'] == sha(data), 'Manifest member size/hash mismatch.')
    code_license = expected['LICENSE-CODE'].decode('utf-8')
    text_license = expected['LICENSE-MANUSCRIPT'].decode('utf-8')
    require(code_license.startswith('MIT License') and 'Taylor Kalin' in code_license
            and 'Project: ' + PROJECT in code_license, 'Code license title/author/scope mismatch.')
    require(text_license.startswith(PROJECT) and 'Taylor Kalin' in text_license
            and 'https://creativecommons.org/licenses/by/4.0/' in text_license
            and 'third-party' in text_license, 'Text/figure license title/author/exclusions mismatch.')

    datacite_url = 'https://api.datacite.org/dois/' + DOI
    dc = json.loads(fetch(datacite_url, cache, 'datacite.json', 2_000_000, observations))['data']['attributes']
    require(dc.get('doi', '').lower() == DOI.lower() and dc.get('state') == 'findable', 'DataCite DOI is not findable.')
    require(any(t.get('title') == TITLE for t in dc.get('titles', [])), 'DataCite title mismatch.')
    require(dc.get('version') == '1.0.0' and dc.get('types', {}).get('resourceTypeGeneral') == 'Software',
            'DataCite software version/type mismatch.')
    dc_creators = dc.get('creators', [])
    require(len(dc_creators) == 1 and dc_creators[0].get('name') == 'Kalin, Taylor'
            and any(orcid(i.get('nameIdentifier')) == ORCID for i in dc_creators[0].get('nameIdentifiers', [])),
            'DataCite creator/ORCID mismatch.')
    agency_url = 'https://doi.org/ra/' + DOI
    agency = json.loads(fetch(agency_url, cache, 'registration-agency.json', 100_000, observations))
    require(len(agency) == 1 and agency[0].get('DOI', '').lower() == DOI.lower()
            and agency[0].get('RA') == 'DataCite', 'DOI registration agency mismatch.')
    resolver_url = 'https://doi.org/' + DOI
    resolved = fetch(resolver_url, cache, 'resolved-record.html', 2_000_000, observations)
    require(observations[-1]['final_url'].rstrip('/') == f'https://zenodo.org/records/{RECORD}'
            and TITLE in plain(resolved.decode('utf-8')), 'DOI resolver does not reach this published software record.')
    require(Path(__file__).read_bytes() == SELF_BYTES, 'Verifier source changed during the command.')

    proof = {
        'schema_version': 1, 'all_checks_passed': True, 'checked_at_utc': now(),
        'record_id': RECORD, 'record_status': 'published', 'doi': DOI,
        'record_url': f'https://zenodo.org/records/{RECORD}', 'title': TITLE,
        'version': '1.0.0', 'publication_date': '2026-10-29', 'resource_type': 'Software',
        'creator': {'name': 'Kalin, Taylor', 'orcid': ORCID},
        'snapshot_commit': H, 'tested_tree': TREE, 'archive_files': FILES,
        'manifest_members_verified': FILES - 1,
        'file': {'filename': FILENAME, 'public_relative_delivery_path': 'output/archives/' + FILENAME,
                 'bytes': ZIP_BYTES, 'sha256': ZIP_SHA, 'md5': ZIP_MD5,
                 'files_compared': FILES, 'all_bytes_identical_to_commit': True, 'zip_comment': H},
        'direct_download_url': download_url, 'archive_sha256': ZIP_SHA,
        'anonymous_Zenodo_ZIP_byte_identical_to_local_archive': True,
        'all_55_local_and_Zenodo_members_equal_immutable_Git_blobs': True,
        'anonymous_GitHub_archive': {'url': public_url, 'bytes': len(public_zip),
            'sha256': sha(public_zip), 'wrapper_prefix': public_prefix, 'zip_comment': public_comment,
            'all_55_members_equal_local_Git_and_Zenodo': True},
        'license_title_correct': True, 'license_project_title': PROJECT,
        'license_title_scope': 'Frozen licenses use the same computational project title without the final manuscript-label suffix; no earlier-study title. Original strings are retained exactly.',
        'component_licenses': {'code': 'MIT', 'original_text_and_figures': 'CC BY 4.0',
            'third_party_rights_excluded': True, 'description_retains_separate_component_scope': True,
            'LICENSE-CODE_sha256': sha(expected['LICENSE-CODE']),
            'LICENSE-MANUSCRIPT_sha256': sha(expected['LICENSE-MANUSCRIPT']),
            'Zenodo_record_license': meta.get('license')},
        'published_description': description,
        'published_source_url': 'https://github.com/Teylersf/electron-only-equation-audit/tree/' + H,
        'DataCite': {'state': 'findable', 'registration_agency': 'DataCite', 'title_matches': True,
                     'Software_version_and_creator_ORCID_match': True},
        'anonymous_record_download_registry_and_resolver_checks': observations,
        'verifier': {'path': 'submissions/verify_zenodo_code.py', 'sha256': sha(SELF_BYTES),
                     'runtime': sys.version.split()[0], 'standard_library_only': True,
                     'Git_operations_read_only': True, 'credentials_or_vault_used': False,
                     'metadata_mutations': 0, 'publisher_submission_calls': 0},
        'verified_files': [{'path': name, 'bytes': len(data), 'sha256': sha(data)}
                           for name, data in sorted(expected.items())],
        'scope': 'Anonymous software identity, component licensing, exact archival/public-Git bytes and DOI availability; not manuscript publication, source-simulation reproduction or scientific correctness.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(proof, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')
    print(json.dumps({'all_checks_passed': True, 'doi': DOI, 'files': FILES,
                      'manifest_members': FILES - 1, 'archive_sha256': ZIP_SHA,
                      'receipt_sha256': sha(args.output.read_bytes())}))


if __name__ == '__main__':
    main()
