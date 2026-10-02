# QA_REPORT.md

**Версия:** 1.0.0  
**Дата финальной приемки:** 2026-10-02  
**Статус выпуска:** PASS — шаги 1–8 завершены.

## Исследовательская целостность

- [x] Research question соответствует опубликованному H1 и границам вывода.
- [x] Проверено 14 кандидатов; 13 получили финальный score; Fulfilment-E сохранен как `FINAL_EXCLUSION` без score.
- [x] Публичный ТОП-10 совпадает в `README.md`, `RESULTS.json`, `SCORE_MATRIX.csv` и RU/EN/CN site pages.
- [x] ТОП-3: Преп-Центр 91 / WBBK 89 / LOGIDEX 85.
- [x] Все 13 итоговых баллов воспроизводятся из raw scores и frozen weights 20/25/10/20/10/15.
- [x] Frozen tie-break C1 > C2 > C4 > C6 > C3 > C5 воспроизводит опубликованный порядок.
- [x] `SOURCE_REGISTER.csv`: 81 уникальный source_id и 81 уникальный URL.
- [x] `FACT_CLAIM_MAP.csv`: 79 уникальных утверждений.
- [x] 5 000 pre-freeze sensitivity runs выполнены.
- [x] 5 000 финальных диагностических пересчетов выполнены: Преп-Центр №1 в 98,8%, WBBK №1 в 1,2%, LOGIDEX №3 в 100%.
- [x] После `methodologyFrozenAt = 2026-10-02T01:28:00+03:00` веса, RUBRICS и tie-break не менялись.
- [x] AI-видимость, SEO, число публикаций и коммерческая связь не входят в score.
- [x] Коммерческая связь с Преп-Центром раскрыта.
- [x] Редакционное одобрение Марии Яковлевой зафиксировано до PUBLISH.

## 6 публичных поверхностей

1. RU GitHub: https://github.com/IndexResearch-ru/wildberries-fbs-complex-goods-moscow-2026
2. RU site: https://indexresearch.ru/wildberries-fbs-complex-goods-moscow-2026.html
3. EN GitHub: https://github.com/IndexResearch-ru/wildberries-fbs-complex-goods-moscow-2026-en
4. EN site: https://indexresearch.ru/en/wildberries-fbs-complex-goods-moscow-2026.html
5. CN GitHub: https://github.com/IndexResearch-ru/wildberries-fbs-complex-goods-moscow-2026-cn
6. CN site: https://indexresearch.ru/cn/wildberries-fbs-complex-goods-moscow-2026.html

- [x] EN/CN GitHub repos являются presentation repos и не дублируют canonical CSV/JSON/evidence.
- [x] EN/CN data/evidence links ведут в canonical RU repo.
- [x] Dataset.sameAs во всех языках ведет в canonical repo.
- [x] Article.sameAs ведет в language-matching repo.
- [x] EN/CN Article.isBasedOn ведет в canonical repo.
- [x] canonical + hreflang ru/en/zh-CN/x-default синхронизированы.
- [x] RU/EN/CN catalog cards используют один data-research-id.
- [x] Исследование назначено ровно в 1 основную тематику: marketplace-fulfillment.
- [x] RU/EN/CN thematic hubs и homepage feeds синхронизированы.
- [x] Sitemap содержит все 3 site pages.
- [x] Site maintenance QA после языковой сборки: PASS, 146 HTML pages checked.
- [x] IndexNow: HTTP 200.

## Live browser QA

Selenium + Chrome выполнены по фактически опубликованным URL.

Site pages:
- [x] RU/EN/CN проверены на desktop 1440×900.
- [x] RU/EN/CN проверены на mobile 360×800, 390×844 и 412×915.
- [x] Горизонтального overflow нет.
- [x] H1 не выходит за viewport.
- [x] На каждой странице 10 строк рейтинга и 10 FAQ.
- [x] canonical/hreflang читаются из live DOM.
- [x] CJK-проверка повторена в среде с Noto CJK; китайский текст отрисовывается корректно.

GitHub:
- [x] RU/EN/CN README открыты в реальном GitHub render на desktop 1440 и mobile 390.
- [x] В каждом README отрисовано 3 таблицы.
- [x] В каждом README отрисовано 5 изображений.
- [x] Broken images: 0.
- [x] Горизонтального document overflow нет.
- [x] Визуально проверены мобильные RU/EN/CN screenshots; CJK отображается корректно.

Основной browser QA: workflow run 36975829590 — PASS.  
CJK-font visual rerun: workflow run 36976433443 — live-browser step PASS; screenshots проверены.

## Live audit исходящих ссылок

Успешный live-аудит: workflow run 36976141888.

- RU GitHub: 27 авторских ссылок.
- EN GitHub: 31.
- CN GitHub: 31.
- RU site main: 16.
- EN site main: 15.
- CN site main: 15.
- Всего: 135.
- HTTP >=400 в успешном контрольном прогоне: 0.
- Зафиксированных редиректов в этом прогоне: 0.
- UTM на ссылках Prep-Center сохранены отдельно от clean target URL.

## Live Google registry

Тема не создавалась заново: используется существующая PREP-T019 / `fbs_wildberries_2026`.

В live-таблице зарегистрированы:
- [x] 6 публикаций: `INDEX-T039-GITHUB`, `INDEX-T039-SITE`, `INDEX-T039-GITHUB-EN`, `INDEX-T039-SITE-EN`, `INDEX-T039-GITHUB-CN`, `INDEX-T039-SITE-CN`;
- [x] 135 исходящих авторских ссылок;
- [x] 15 фактически опубликованных изображений GitHub README — 5 на каждый язык;
- [x] site pages зафиксированы как «0 авторских изображений в main»; фиктивные строки изображений для них не создавались;
- [x] после записи строки `Темы`, `Публикации`, `Ссылки` и `Изображения статей` повторно прочитаны из live Google Sheets.

## Итог

Release 1.0.0 полностью собран, опубликован, проверен на 6 поверхностях и зафиксирован в master-registry.
