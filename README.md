# bible

성경 연구 저장소. https://bible.busangames.com

- 글은 `docs/` 아래 마크다운. 폴더가 곧 차례다 (구약·신약·주제·원어).
- 새 글: `docs/템플릿.md` 를 복사해 채우고 `main` 에 커밋한다. GitHub Actions 가
  [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 로 지어 `gh-pages` 에 올린다.
- 로컬 미리보기:

  ```bash
  pip install -r requirements.txt
  mkdocs serve
  ```

## 처음 한 번

1. 저장소 Settings → Pages → Source 를 **Deploy from a branch / `gh-pages` / `/ (root)`** 로.
   (`docs/CNAME` 이 함께 올라가므로 Custom domain 은 자동으로 `bible.busangames.com` 이 된다.)
2. `busangames.com` DNS 에 CNAME 레코드: `bible` → `davidrheetaekyoung.github.io`
3. 인증서가 잡히면(몇 분~한 시간) Pages 에서 **Enforce HTTPS** 를 켠다.
